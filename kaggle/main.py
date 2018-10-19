#!/usr/bin/env python3
"""
Module Docstring
"""

__author__  = 'Arturo Mora'
__version__ = '0.1.0'
__license__ = 'MIT'

import argparse


def main(args):
    """ Main entry point of the app """
    print(args)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("arg", help="Required positional argument")

    args = parser.parse_args()
    main(args)
