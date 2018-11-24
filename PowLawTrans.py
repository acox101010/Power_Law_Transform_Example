# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import imageio

#Modify for your image file path
im1path = (r"C:\Users\Reaper124\.spyder-py3\Scripts\PowerLawTrans\screenshot.png")

#open Image and apply transformation
im = cv2.imread(im1path)
#scale pixel intensities
im = im/255.0
#Modify gamma level to suit your needs
im_pow_law_trans = cv2.pow(im,0.6)

#Display images and transfer
cv2.imshow("original",im)
cv2.imshow("Gamma_Correct",im_pow_law_trans)
cv2.waitKey(0)

img = mpimg.imread(im1path)
imgplot = plt.imshow(im_pow_law_trans)

lum_img = img[:,:,0]
imgplothot = plt.imshow(lum_img, cmap="hot")

#save converted file to existing directory
imageio.imwrite('corrected.png',im_pow_law_trans)