# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='kaggle',
    version='0.1.0',
    description='Project I',
    long_description=readme,
    author='Arturo Mora',
    author_email='luartmgr@gmail.com',
    url='https://github.com/luartmg/pc-i-kaggle.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)