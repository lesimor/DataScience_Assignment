# encoding: utf-8
import calculate
import itertools


def set_stat(_file, _set):
    _file.seek(0)  # 커서를 초기화
    frequency = 0  # 빈도수 변수 초기화
    transaction_count = 0
    result_obj = {}
    for line in _file:
        transaction_count += 1
        transaction = map(int, line.split())
        transaction_set = set(transaction)
        if _set.issubset(transaction_set):
            frequency += 1
    result_obj["frequency"] = frequency
    result_obj["transaction_count"] = transaction_count
    result_obj["support"] = float(frequency) / float(transaction_count)
    return result_obj


def associative_set_stat(_file, item_set, associative_item_set):
    # item_set 발생 빈도수
    item_set_frequency = set_stat(_file, item_set)["frequency"]

    union_set = item_set.union(associative_item_set)
    # item_set U associative_item_set 빈도수
    confidence_frequency = set_stat(_file, union_set)["frequency"]

    return {
        'support': set_stat(_file, union_set)["support"],
        'confidence': float(confidence_frequency) / float(item_set_frequency)
    }


def join_and_prune(_file, set_list, min_sup, step):
    result_set_list = []
    for index, s in enumerate(set_list):
        for x in range(index + 1, len(set_list)):
            union_set = s.union(set_list[x])

            if len(union_set) == step and calculate.set_stat(_file,
                                                             union_set)[
                "frequency"] >= min_sup and union_set not in result_set_list:
                print str(union_set) + str(calculate.set_stat(_file, union_set)["frequency"])
                result_set_list.append(union_set)
    if len(result_set_list) > 0:
        return result_set_list
    else:
        return None


def generate_item_associative(_set):
    set_size = len(_set)
    combination_list = []
    for size in range(1, set_size):
        items = map(set, itertools.combinations(list(_set), size))
        for item in items:
            item_set = item
            associative_set = _set - item_set
            combination_list.append([item_set, associative_set])

    return combination_list


def generate_all_subsets(_set):
    set_size = len(_set)
    subset_list = []
    for size in range(1, set_size + 1):
        items = map(set, itertools.combinations(list(_set), size))
        subset_list += items
    return subset_list

