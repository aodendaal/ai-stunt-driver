from __future__ import absolute_import, division, print_function, unicode_literals
from PIL import ImageGrab, Image
import datetime
import math
import numpy as np
import time
import window_location

_resize_percentage = 0.2
_form_name = "DOSBox 0.74"


def get_screenshot():
    global _resize_percentage
    global _form_name

    left, top, right, bottom = window_location.get_dimensions(_form_name)

    if (left == 0 and right == 0):
        img = ImageGrab.grab()  # grab full screen
    else:
        img = ImageGrab.grab(bbox=(left, top, right, bottom))  # grab specific window

    img = img.convert("L")  # convert to greyscale
    img = img.resize((math.floor(img.width * _resize_percentage),
                      math.floor(img.height * _resize_percentage)),
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
