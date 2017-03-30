# encoding: utf-8
import itertools


class Set:
    # represent set element
    element = set()
    frequency = 0

    def __init__(self, _file, _element):
        self.element = set(_element)
        self.frequency = 0
        _file.seek(0)  # 커서를 초기화
        for line in _file:
            transaction = map(int, line.split())
            transaction_set = set(transaction)
            if self.element.issubset(transaction_set):
                self.frequency += 1

    def gen_subset(self, size):
        return map(set, itertools.combinations(self.element, size))
