# -*-encoding: utf-8-*-
import random

class Node:
    def __init__(self, attr_list=[], criteria_attribute=None, data=[]):
        self.parent = None
        self.attribute_list = [v for v in attr_list if not v == criteria_attribute]     # splitting attribute_list remaining
        self.criteria_attribute = criteria_attribute
        self.data = data                    # 분할 기준에 따라 묶인 데이터들.
        self.label = None                   # 최종 클래스 라벨, non-terminal인 경우 None값.
        self.children = {}
        self.classifying_attribute = None

    def following_node(self, datum):
        pointing_node = self

        while(pointing_node.label == None):
            current_criteria = pointing_node.classifying_attribute
            value = datum[current_criteria]
            pointing_node = pointing_node.children[value]

        return pointing_node.label


    def set_current_node_criteria(self, attr):
        self.classifying_attribute = attr

