#!/usr/bin/env python3
"""
Module Docstring
"""

__author__  = 'Arturo Mora'
__version__ = '0.1.0'
__license__ = 'GNUv3'

from tools import preprocessor

def main(args):
    """ Main entry point of the app """
    print(args)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    p = preprocessor.Preprocessor()
    p.load('../data/breast_cancer_data_set.csv')
