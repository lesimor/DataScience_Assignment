# -*-encoding: utf-8-*-
import random

class Node:
    def __init__(self, attr_list=[], group_value=None, data=[]):
        self.parent = None
        self.attribute_list = attr_list     # splitting attribute_list remaining
        self.group_value = group_value      # 하나로 묶어주는 값
        self.splitting_criterion = None     # 분할 기준 -> attribute_selection_method함수로 결정.
        self.data = data                    # 분할 기준에 따라 묶인 데이터들.
        self.label = None                   # 최종 클래스 라벨, non-terminal인 경우 None값.
        self.children = {}

    def generate_successors(self):
        # 더이상 나눌 기준이 없다면 중단.
        if len(self.attribute_list):
            return None
        selected_attribute = random.choice(self.attribute_list)

        selected_attribute_modified = self.attribute_list.remove(selected_attribute)



        return 0

    def hello(self):
        print "hello"
        print self.attribute_list


