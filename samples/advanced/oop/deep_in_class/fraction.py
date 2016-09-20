#!/usr/bin/env python
# -*-coding: utf-8-*-
'''
定制类：显示分数
'''


class Fraction(object):
    def __init__(self, number, denom=1):
        self.number = number
        self.denom = denom

    def __str__(self):
        return str(self.number) + '/' + str(self.denom)

    __repr__ = __str__


if __name__ == "__main__":
    f = Fraction(2, 3)
    print f
