from __future__ import absolute_import, division, print_function, unicode_literals
from PIL import ImageGrab, Image
import datetime
import math
import numpy as np
import time

resize_percentage = 0.2


def get_screenshot():
    img = ImageGrab.grab()  # grab full screen
    img = img.convert("L")  # convert to greyscale
    img = img.resize((math.floor(img.width * resize_percentage),
                      math.floor(img.height * resize_percentage)),
                     Image.BILINEAR)

    return img


def save_screenshot(path):
    img = get_screenshot()

    filename = "{0}.png".format(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"))
    pahtfilename = "{0}/{1}".format(path, filename)

    img.save(pahtfilename, "PNG")

    return filename


def get_screenshot_data():
    img = get_screenshot()

    pixels = img.getdata()

    return pixels


def get_screenshot_array():
    img = get_screenshot()

    arr = np.array(img)

    return arr


def main():
    print(save_screenshot("./img"))


if __name__ == "__main__":
    main()
