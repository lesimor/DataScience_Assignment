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
for idx, attribute in enumerate(attribute_list):
    attribute_label_set[attribute] = []

transactions = []

for line in f:
    transaction = map(str, line.split())

    # 딕셔너리로 변환
    dict = {}

    for idx, col in enumerate(transaction):
        dict[attribute_list[idx]] = col

    transactions.append(dict)

    for idx, value in enumerate(transaction):
        if value not in attribute_label_set[attribute_list[idx]]:
            attribute_label_set[attribute_list[idx]] += [value]
    print transaction

print attribute_label_set
print transactions

root_node = classes.Node(attribute_list, None, transactions)


attr_list = root_node.attribute_list
selected_attribute = random.choice(attr_list)
selected_attribute_modified = attr_list.remove(selected_attribute)

# 해당 attribute의 라벨 종류를 가져온다.
labels_of_selected_attribute = attribute_label_set[selected_attribute]

for label in labels_of_selected_attribute:
    data = m.filter(root_node.data, selected_attribute, label)
    new_node = classes.Node(selected_attribute_modified, label, data)
    root_node.children[label] = new_node

print '-----'
for key, child in root_node.children.iteritems():
    print '--------------'
    print key
    print child.data

