# -*-encoding: utf-8-*-
import random

class Node:
    def __init__(self, attr_list=[], criteria_attribute=None, group_value=None, data=[]):
        self.parent = None
        self.attribute_list = [v for v in attr_list if not v == criteria_attribute]     # splitting attribute_list remaining
        self.criteria_attribute = criteria_attribute
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

        self.attribute_list.remove(selected_attribute)


        return 0

