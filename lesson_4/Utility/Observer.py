# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:03:25 2019

@author: MIF
"""

from abc import ABCMeta, abstractmethod

class Observer( metaclass = ABCMeta ):
    """
    Абстрактный суперкласс для всех наблюдателей.
    """
    @abstractmethod
    def modelIsChanged( self ):
        """
        Метод который будет вызван у наблюдателя при изменении модели.
        """
        pass