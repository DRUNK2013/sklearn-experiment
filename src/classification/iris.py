#!/bin/python3

# Created by shuangfu on 17-3-16.
# Author : Kane
# email :len1988.zhang@gmail.com

import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sb

class Iris(object):

    def __init__(self, path):
        self.iris_data = pd.read_csv(path)
        self.iris_data.columns = ['sepal_length_cm', 'sepal_width_cm', 'petal_length_cm', 'petal_width_cm', 'class']

    def show_image(self,path):
        img=Image.open(path)
        plt.imshow(img)
        plt.show()