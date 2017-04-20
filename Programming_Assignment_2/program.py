# -*-encoding: utf-8-*-
import sys      # 프로그램 실행 시 인자를 전달받기 위함
import classes
import random
import modules as m

input_file = "dt_train.txt"
# file open and read
f = open(input_file)

attribute_list = map(str, f.readline().split())

# 각 attribute별 라벨 종류를 generate
attribute_label_set = {}
idx_attr_map = []
for idx, attribute in enumerate(attribute_list):
    attribute_label_set[attribute] = []
    idx_attr_map += [attribute]

transactions = []

for line in f:
    transaction = map(str, line.split())

    # 딕셔너리로 변환
    dict = {}

    for idx, col in enumerate(transaction):
        dict[attribute_list[idx]] = col

    transactions.append(dict)

    for idx, value in enumerate(transaction):
        if value not in attribute_label_set[idx_attr_map[idx]]:
            attribute_label_set[idx_attr_map[idx]] += [value]
    # print transaction


# print attribute_label_set
# print transactions
root_node = classes.Node(attribute_list[:-1], None, None, transactions)
class_attribute = attribute_list[-1]


def generate_successors(node):
    print "\n\n\n"
    print "그룹 값이 " + str(node.group_value) + "인 노드가 generate_successors 호출"

    attr_list = list(node.attribute_list)

    if len(attr_list) == 0 or m.pure_check(node.data, class_attribute):
        leaf_label = m.pure_check(node.data, class_attribute)
        if not leaf_label:
            leaf_label = random.choice(attribute_label_set[class_attribute])
        node.label = leaf_label
        print "-------Leaf 노드입니다.-------"
        print "분류 기준이 " + node.criteria_attribute + "이고 그 값이 " + node.group_value + "인 데이터 노드"
        # 데이터가 있는 경우와 없는 경우 구분
        if len(node.data) != 0:
            for data in node.data:
                print data
                print "라벨은 " + leaf_label

        else:
            print "데이터가 없으므로 랜덤으로 배정합니다."
            print "라벨은 " + leaf_label
        print "---------------------------"
        return None
    else:
        # 최적의 attribute값을 찾는 로직 필요.
        selected_attribute = m.information_gain(node.data, attr_list, class_attribute)
        # selected_attribute = random.choice(attr_list)

        # 현재 노드의 분류 기준 세팅
        node.set_current_node_criteria(selected_attribute)
        print "노드 분류 기준 " + node.classifying_attribute
        print "남은 분류 기준 " + str(attr_list) + "중에 " + selected_attribute + " 선택!"
        # 해당 attribute의 라벨 종류를 가져온다.
        labels_of_selected_attribute = attribute_label_set[selected_attribute]

        print '해당 attribtute의 라벨 종류 가져오기'
        print labels_of_selected_attribute

        for label in labels_of_selected_attribute:
            data = m.filter(node.data, selected_attribute, label)
            new_node = classes.Node(attr_list, selected_attribute, label, data)
            print "분류 기준이 " + selected_attribute + "이고 그 값이 " + label + "인 데이터 노드 생성"
            if generate_successors(new_node):
                node.children[label] = new_node

    return node


tree = generate_successors(root_node)




print '-----'
# for key, child in root_node.children.iteritems():
#     print '--------------'
#     print key
#     print child.data


