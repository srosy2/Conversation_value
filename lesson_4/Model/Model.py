# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 18:48:56 2019

@author: MIF
"""


class Money:
    def __init__(self, many=0, few=0):
        self.many = many
        self.few = few

    @property
    def add(self):
        return self.many, self.few

    @add.setter
    def add(self, b=0):
        b = b * 100
        self.few += b % 100
        d = self.few // 100
        self.many = self.many + d + b // 100
        self.few -= d * 100

    @property
    def odd(self):
        return self.many, self.few

    @odd.setter
    def odd(self, b=0):
        b = b * 100
        self.few -= b % 100
        d = self.few // 100
        self.many = self.many + d - b // 100
        self.few -= d * 100

    @property
    def percent(self):
        return self._A

    @percent.setter
    def percent(self, b=0):
        self._A = str((self.many * 100 + self.few) * b / 10000)

    @property
    def change(self):
        return self._Summ

    @change.setter
    def change(self, x):
        d = 1
        if x[1] == "Dollars":
            d = 64
        if x[1] == "Rubles":
            d = 1/64
        self._Summ = x[0] * d * 100
        b = x[0] * 100
        self.few -= b % 100
        d = self.few // 100
        self.many = self.many + d - b // 100
        self.few -= d * 100
