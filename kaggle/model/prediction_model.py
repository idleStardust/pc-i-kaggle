#!/usr/bin/env python3
"""
Module Docstring
"""
from abc import ABC, abstractmethod

class PredictionModel(ABC):

    def __init__(self):
        dataset = None
        super().__init__()

    @abstractmethod
    def fit_data(self):
        pass

    @abstractmethod
    def predict_data(self):
        pass

    @abstractmethod
    def report_result(self):
        pass