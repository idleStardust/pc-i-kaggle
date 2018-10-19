#!/usr/bin/env python3
"""
Module Docstring
"""
from prediction_model import PredictionModel

class RandomForestModel(PredictionModel):
    
    def __init__(self, pruning_threshold):
        self.pruning_threshold = pruning_threshold

    def fit_data(self, data_train, data_class):
        pass

    def predict_data(self, data_test):
        pass

    def report_result(self):
        pass