# -*-encoding: utf-8-*-
import math


def filter(data, attr, value):
    results = []
    for datum in data:
        if datum[attr] == value:
            results.append(datum)
    return results


def pure_check(data, attr):
    print "pure check"
    print data
    if len(data) != 0:
        value = data[0][attr]
        for datum in data:
            if datum[attr] != value:
                return None
        return value
    else:
        return None


def info(data, attr):
    attr_dict = {}
    for datum in data:
        if datum[attr] in attr_dict.keys():
            attr_dict[datum[attr]] += 1
        else:
            attr_dict[datum[attr]] = 1

    frequency_list = attr_dict.values()

    total = float(sum(frequency_list))
    result_entropy = 0
    for freq in frequency_list:
        freq = float(freq)
        result_entropy -= (freq/total)*math.log((freq/total), 2)
    return result_entropy


def info_gain(data, attr, class_attr):
    # 클래스 정보값
    class_info = info(data, class_attr)

    # 해당 특성값의 정보값
    attr_info = 0.0
    attr_dict = {}
    for datum in data:
        if datum[attr] in attr_dict.keys():
            attr_dict[datum[attr]] += 1
        else:
            attr_dict[datum[attr]] = 1
    data_sum = float(len(data))
    for (key, value) in attr_dict.items():
        filtered_data = filter(data, attr, key)
        value = float(value)
        attr_info += (value / data_sum) * info(filtered_data, class_attr)

    return class_info - attr_info


def splitting_criteria_decision(data, attr_list, class_attr):
    attr_list.sort(key=lambda x: info_gain(data, x, class_attr), reverse=True)
    return attr_list[0]


