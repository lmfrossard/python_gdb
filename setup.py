__author__ = 'ling'
from setuptools import setup, find_packages

setup(
      name="python_gdb",
      version="0.2",
      description="a cure linux debugger",
      author="Ling",
      author_email='ling_pro@163.com',
      url="http://www.github.com/MatrixLing/python_gdb",
      packages= find_packages(),
      scripts=["scripts/test.py"],
      )