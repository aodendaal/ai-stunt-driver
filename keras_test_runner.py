from __future__ import absolute_import, division, print_function, unicode_literals
import keyboard_listener as kb
import numpy as np
from pynput.keyboard import Key
import screenshot_taker as st
from tensorflow.keras import datasets, layers, models
import time


model = None
frames_per_second = 5


def get_model():
    global model

    model = models.load_model('./kerasmodel.h5')


def get_prediction(data):
    if model == None:
        get_model()

    data = data.reshape(1, 80, 128, 1)
    prediction = model.predict(data)

    return prediction


def get_keys_to_press(one_hot):
    found = np.argmax(one_hot)
    if (found == 0):
        print('up+left')
        return [Key.up, Key.left]
    elif (found == 1):
        print('up')
        return [Key.up]
    elif (found == 2):
        print('up+right')
        return [Key.up, Key.right]
    elif (found == 3):
        print('left')
        return [Key.left]
    elif (found == 4):
        print('right')
        return [Key.right]
    elif (found == 5):
        print('down+left')
        return [Key.down, Key.left]
    elif (found == 6):
        print('down')
        return [Key.down]
    elif (found == 7):
        print('down+right')
        return [Key.down, Key.right]
    else:
        print('nothing')
        return ''


def main():
    kb.setup_keyboard_listening()

    while kb.is_running:
        if (kb.is_running):
            data = st.get_screenshot_array()
            prediction = get_prediction(data)
            keys = get_keys_to_press(prediction)
            kb.press_keys(keys)

        time.sleep(1 / frames_per_second)


if __name__ == "__main__":
    main()
