
"""
CSCI431.01 Final Project
Name : Compress
Authors : Christopher Zealand Miller
Email : Czm6134@g.rit.edu
Description : this is the program part of the final - better description needed
"""


import os
import sys
import numpy as np
import scipy
import matplotlib
from matplotlib import pyplot as plt


def getfile(filepath):
    picture = plt.imread(filepath)
    return picture


def show_img(img):
    plt.imshow(img, cmap=plt.get_cmap("gray"))
    plt.show()


def save_img(img, name):
    plt.imsave(name, img)


def get_size(name):
    cwd = os.getcwd() + '\\' + name
    size = os.path.getsize(cwd)
    print("The size of {} is : {:,} in bytes".format(name, size))


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


def main():
    name = 'lenna.jpg'
    img = getfile(name)
    show_img(img)
    get_size(name)
    greyimg = rgb2gray(img)
    show_img(greyimg)
    save_img(greyimg, 'grey_lenna.jpg')
    get_size('grey_lenna.jpg')


if __name__ == "__main__":
    main()