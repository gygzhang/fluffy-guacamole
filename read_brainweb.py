from __future__ import print_function
import numpy as np
import sys
import cv2
from matplotlib import pyplot as plt
import re

def read_brainweb(path,file,num_z):
    with open(file, "rb") as rawbs:
        ib_l = []
        ib_l = rawbs.read(181 * 217 * 181)
        #print ib_l.__len__()
        temp = np.array(list(ib_l))

        #method one of matrix divsion
        #img_write = temp.reshape(181 * 217 ,181)
        # img_write = img_write[181 * 217 * num_z:181 * 217 * (num_z + 1)]

        #method two
        img_write = temp.reshape(181 , 181* 217)
        #get the num_zth image of the 3d image
        img_write = img_write[num_z,:]
        img_write = np.array(img_write).reshape(217, 181)

        #normalize the image to 0-255
        cv2.normalize(img_write, img_write, 0, 255, cv2.NORM_MINMAX)

       # plt.imshow(img_write, cmap='gray', interpolation='bicubic')
       # plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
        #plt.show()
        fn1 = re.split("\\\\",file)[-1]
        sip = re.split("_",fn1)
        filename = sip[0]+"_"+sip[-2]+"_"
        #print(sip)
        cv2.imwrite(path+"\\"+filename+str(num_z)+".png", img_write)