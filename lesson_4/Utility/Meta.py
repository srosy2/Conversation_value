# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:18:41 2019

@author: MIF
"""

"""
Модуль реализации метакласса, необходимого для работы представления.

pyqtWrapperType - метакласс общий для оконных компонентов Qt.
ABCMeta - метакласс для реализации абстрактных суперклассов.

Meta - метакласс для представления.
"""

from PyQt5 import QtCore
from abc import ABCMeta


class Meta(type(QtCore.QObject), ABCMeta): pass
