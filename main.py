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
    group_action = parser.add_mutually_exclusive_group()
    group_action.add_argument("--arbol",
    	               action="store_true",
    	               help="Random forest")
    group_action.add_argument("--red-neuronal",
    	               action="store_true",
    	               help="Red Neuronal")
    group_action.add_argument("--regresion-lineal",
    	               action="store_true",
    	               help="Regresion lineal")
    parser.add_argument("--prefijo", 
                        help="Se agrega a archivos de corrida")
    parser.add_argument("--porcentaja-pruebas",
    	                help="Porcentaje restante usa funciones de prediccion")

    args = parser.parse_args()
    main(args)
