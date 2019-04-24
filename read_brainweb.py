import numpy as np
import sys
import cv2
from skimage import data,filters
from matplotlib import pyplot as plt

def read_brain_web(path,file,num_z):
    rwabs = open(file, "rb")
    ib_l = []
    ib_l = rwabs.read(181 * 217 * 181)
    temp = np.array(list(ib_l))

    img_write = temp.reshape(181 * 217 * 181)
    img_write = img_write[181 * 217 * num_z:181 * 217 * (num_z + 1)]
    img_write = np.array(img_write).reshape(217, 181)

    cv2.normalize(img_write, img_write, 0, 255, cv2.NORM_MINMAX)

    plt.imshow(img_write, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

    cv2.imwrite(path+"\\1.png", img_write)