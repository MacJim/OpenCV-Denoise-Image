# Reference: https://www.geeksforgeeks.org/python-denoising-of-colored-images-using-opencv/

import numpy as np
import cv2
from matplotlib import pyplot as plt


def denoiseFile(imageName):
    image = cv2.imread(imageName)
    denoisedImage = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 10, 15)
    # denoisedImage = cv2.fastNlMeansDenoisingColored(image, None, 8, 8, 7, 15)

    # plt.subplot(121)    # For some reason MatPlotLib adds a blue tint to my images when displaying them.
    # plt.imshow(image)
    # plt.subplot(122)
    # plt.imshow(denoisedImage)

    # plt.show()

    cv2.imshow("Pre", image)
    cv2.imshow("Post", denoisedImage)
    cv2.waitKey(0)


denoiseFile("inputs/1.png")
