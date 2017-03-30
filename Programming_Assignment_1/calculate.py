# encoding: utf-8
import calculate
import itertools


# get statistic information of set in file
def set_stat(_file, _set):
    _file.seek(0)  # initialize cursor
    frequency = 0  # initialize frequency variable
    transaction_count = 0   # count all transaction size
    result_obj = {}         # variable for result value

    # read by line
    for line in _file:
        transaction_count += 1
        transaction = map(int, line.split())    # convert transaction string into integer list
        transaction_set = set(transaction)      # convert list into set
        if _set.issubset(transaction_set):      # add frequency if parameter set belongs to transaction set
            frequency += 1
    result_obj["frequency"] = frequency
    result_obj["transaction_count"] = transaction_count
    result_obj["support"] = (float(frequency) / float(transaction_count)) * 100
    return result_obj


# passing item_set value and associative_item_set value
# calculate support and confidence
def associative_set_stat(_file, item_set, associative_item_set):
    # item_set frequency
    item_set_frequency = set_stat(_file, item_set)["frequency"]

    # generate union set of item set and associative item set
    union_set = item_set.union(associative_item_set)

    # get frequency of union set
    confidence_frequency = set_stat(_file, union_set)["frequency"]

    return {
        'support': set_stat(_file, union_set)["support"],
        'confidence': (float(confidence_frequency) / float(item_set_frequency)) * 100
    }


# join and prune method
def join_and_prune(_file, set_list, min_sup, step):
    result_set_list = []    # variable for return value
    for index, s in enumerate(set_list):
        for x in range(index + 1, len(set_list)):
            union_set = s.union(set_list[x])

            # add on result only if length of union set is equal to step and support of union set is higher than min_sup
            if len(union_set) == step and calculate.set_stat(_file,
                                                             union_set)[
                "support"] >= min_sup and union_set not in result_set_list:
                result_set_list.append(union_set)
    # return result set list if the list's size is more than zero
    if len(result_set_list) > 0:
        return result_set_list
    # return None if result set list's size is zero
    else:
        return None


# generate item set and associative set among parameter set
def generate_item_associative(_set):
    set_size = len(_set)
    combination_list = []
    for size in range(1, set_size):
        # generate combination of set by size
        items = map(set, itertools.combinations(list(_set), size))

        for item in items:
            item_set = item
            associative_set = _set - item_set

            # append item set and associative set pair on combination list
            combination_list.append([item_set, associative_set])

    return combination_list


# generate all subset of parameter set
def generate_all_subsets(_set):
    # get length of parameter set
    set_size = len(_set)

    # variable for return value
    subset_list = []

    # generate subset of each total size
    for size in range(1, set_size + 1):
        items = map(set, itertools.combinations(list(_set), size))
        subset_list += items    # append item on subset list
    return subset_list
