#!/bin/python3

# Created by shuangfu on 17-3-16.
# Author : Kane
# email :len1988.zhang@gmail.com
import unittest
import os,sys
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from src.classification.iris import Iris

class TestIris(unittest.TestCase):

    def setUp(self):
        self.iris = Iris("../data/iris.data")

    def test___init__(self):
        print(os.path.join(os.getcwd(), os.path.pardir))
        print(self.iris.iris_data.head())
        print(self.iris.iris_data.shape)
        print("ok")

    def test_showImage(self):
        self.iris.show_image("../data/iris_test.jpg")

