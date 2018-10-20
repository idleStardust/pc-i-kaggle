#!/usr/bin/env python3
from abc import ABC, abstractmethod

class PredictionModel(ABC):
    """
    Module Docstring
    """
    def __init__(self):
        dataset = None
        super().__init__()

    @abstractmethod
    def build(self):
        pass
    
    @abstractmethod
    def fit(self):
        pass
    
    @abstractmethod
    def predict(self):
        pass