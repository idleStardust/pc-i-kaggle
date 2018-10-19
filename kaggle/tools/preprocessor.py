import pandas as pd	
import numpy as np

class Preprocessor:

    def __init__(self):
    	self.dataset = None

    def load(self, filename):
    	self.dataset = pd.read_csv(filename)

    def normalization(self):
    	pass

    def encoding(self):
    	serie = pd.Series()
    	pass