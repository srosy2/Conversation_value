# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:15:06 2019

@author: MIF
"""
from abc import ABC

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import pyqtSignal
# from Utility.Observer import Observer
from Utility.Meta import Meta
from View.MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, ABC, metaclass=Meta):
    def __init__(self, inController, inModel, inModel2, parent=None):
        """
        Конструктор принимает ссылки на модель и контроллер.
        """
        # SIGNAL = pyqtSignal
        super(QMainWindow, self).__init__(parent)
        self.mController = inController
        self.mModel = inModel
        self.mModel2 = inModel2

        # подключаем визуальное представление
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        self.modelIsChanged()

    def initUI(self):
        self.ui.pushButton_0.clicked.connect(self.mController.percent_many_ruble)
        self.ui.pushButton_1.clicked.connect(self.mController.odd_many_ruble)
        self.ui.pushButton_2.clicked.connect(self.mController.add_many_ruble)
        self.ui.pushButton_3.clicked.connect(self.mController.change_many_ruble)
        self.ui.pushButton_4.clicked.connect(self.mController.percent_many_dollar)
        self.ui.pushButton_5.clicked.connect(self.mController.odd_many_dollar)
        self.ui.pushButton_6.clicked.connect(self.mController.add_many_dollar)
        self.ui.pushButton_7.clicked.connect(self.mController.change_many_dollar)

    def modelIsChanged(self):
        sum1 = str(int(self.mModel.many))
        sum2 = str(int(self.mModel.few))
        sum = sum1 + "," + sum2
        sum3 = str(int(self.mModel2.many))
        sum4 = str(int(self.mModel2.few))
        sum5 = sum3 + ',' + sum4
        self.ui.rubles.setText(sum)
        self.ui.dollars.setText(sum5)
