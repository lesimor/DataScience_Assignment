# encoding: utf-8
import calculate


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
    return result_obj


def get_confidence(_file, item_set, associative_item_set):
    # item_set 발생 빈도수
    item_set_frequency = set_stat(_file, item_set)["frequency"]

    # item_set U associative_item_set 빈도수
    confidence_frequency = set_stat(_file, item_set.union(associative_item_set))["frequency"]

    return float(confidence_frequency) / float(item_set_frequency)


def join_and_prune(_file, set_list, min_sup, step):
    result_set_list = []
    for index, s in enumerate(set_list):
        for x in range(index + 1, len(set_list)):
            union_set = s.union(set_list[x])
            if len(union_set) == step and calculate.set_stat(_file,
                                                             union_set) >= min_sup and union_set not in result_set_list:
                result_set_list.append(union_set)
    if len(result_set_list) > 0:
        return result_set_list
    else:
        return None
