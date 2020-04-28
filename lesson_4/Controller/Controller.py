# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:20:14 2019

@author: MIF
"""
import sys

from PyQt5.QtWidgets import QApplication
from View.View import MainWindow


class Controller:
    """
    Класс CplusDController представляет реализацию контроллера.
    Согласовывает работу представления с моделью.
    """

    def __init__(self, inModel, inModel2):
        """
        Конструктор принимает ссылку на модель.
        Конструктор создаёт и отображает представление.
        """
        self.mModel = inModel
        self.mModel2 = inModel2
        self.mView = MainWindow(self, self.mModel, self.mModel2)

        self.mView.show()

    def odd_many_ruble(self):
        self.mModel.odd = (float(self.mView.ui.textEdit_2.toPlainText()))
        self.mView.modelIsChanged()
        self.mView.ui.textEdit_2.setText('0')

    def add_many_ruble(self):
        self.mModel.add = (float(self.mView.ui.textEdit_3.toPlainText()))
        self.mView.modelIsChanged()
        self.mView.ui.textEdit_3.setText('0')

    def percent_many_ruble(self):
        a = self.mView.ui.textEdit.toPlainText()
        self.mModel.percent = int(a)
        b = self.mModel.percent
        self.mView.ui.textEdit_2.setText(b)
        self.mView.ui.textEdit_3.setText(b)
        self.mView.ui.textEdit_4.setText(b)
        self.mView.ui.textEdit.setText('0')

    def change_many_ruble(self):
        a = float(self.mView.ui.textEdit_4.toPlainText())
        self.mModel.change = (a, self.mModel.currency)
        d = int(self.mModel.change)
        self.mModel2.few += d % 100
        self.mModel2.many += d // 100
        self.mView.modelIsChanged()
        self.mView.ui.textEdit_4.setText('0')

    def percent_many_dollar(self):
        a = self.mView.ui.textEdit_5.toPlainText()
        self.mModel2.percent = int(a)
        b = self.mModel2.percent
        self.mView.ui.textEdit_6.setText(b)
        self.mView.ui.textEdit_7.setText(b)
        self.mView.ui.textEdit_8.setText(b)
        self.mView.ui.textEdit_5.setText('0')

    def odd_many_dollar(self):
        self.mModel2.odd = (float(self.mView.ui.textEdit_6.toPlainText()))
        self.mView.modelIsChanged()
        self.mView.ui.textEdit_6.setText('0')

    def add_many_dollar(self):
        self.mModel2.add = (float(self.mView.ui.textEdit_7.toPlainText()))
        self.mView.modelIsChanged()
        self.mView.ui.textEdit_7.setText('0')

    def change_many_dollar(self):
        a = float(self.mView.ui.textEdit_8.toPlainText())
        print(a)
        self.mModel2.change = (a, self.mModel2.currency)
        print(self.mModel2.change)
        d = int(self.mModel2.change)
        print(d)
        self.mModel.few += d % 100
        self.mModel.many += d // 100
        self.mView.modelIsChanged()
        self.mView.ui.textEdit_8.setText('0')
