from __future__ import absolute_import, division, print_function, unicode_literals
from PIL import ImageGrab, Image
import datetime
import math
import time

resize_percentage = 0.2


def save_screenshot(path):
    img = ImageGrab.grab()  # grab full screen
    img = img.convert("L")  # convert to greyscale
    img = img.resize((math.floor(img.width * resize_percentage),
                      math.floor(img.height * resize_percentage)),
                     Image.BILINEAR)

    filename = "{0}/{1}.png".format(path, datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"))

    img.save(filename, "PNG")

    return filename


def get_screenshot_data():
    img = ImageGrab.grab()  # grab full screen
    img = img.convert("L")  # convert to greyscale
    img = img.resize((math.floor(img.width * resize_percentage),
                      math.floor(img.height * resize_percentage)),
                     Image.BILINEAR)

    pixels = img.getdata()

    return pixels


print(save_screenshot("./img"))