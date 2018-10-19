#!/usr/bin/env python3
"""
Module Docstring
"""
from abc import ABC, abstractmethod

class PredictionModel(ABC):
    data_train = []
    data_class = ""

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def fit_data(self, data_train, data_class):
        pass

    @abstractmethod
    def predict_data(self, data_test):
        pass

    @abstractmethod
    def report_result(self):
        pass