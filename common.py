import functools
from PIL import ImageGrab, Image
import math
import tensorflow as tf

resize_percentage = 0.2


def get_screenshot_data():
    img = ImageGrab.grab()  # grab full screen
    img = img.convert("L")  # convert to greyscale
    img = img.resize((math.floor(img.width * resize_percentage),
                      math.floor(img.height * resize_percentage)),
                     Image.BILINEAR)

    pixels = img.getdata()

    return list(pixels)


def define_scope(function):
    attribute = '_cache_' + function.__name__

    @property
    @functools.wraps(function)
    def decorator(self):
        if not hasattr(self, attribute):
            with tf.variable_scope(function.__name__):
                setattr(self, attribute, function(self))
        return getattr(self, attribute)

    return decorator
