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

    model = models.load_model('./tmp/kerasmodel.h5')


def get_prediction(data):
    if model == None:
        get_model()

    data = data.reshape(1, 80, 128, 1)
    prediction = model.predict(data)

    return prediction


def main():
    get_model()

    kb.setup_keyboard_listening()

    count = 0
    while kb.has_started:
        if (kb.is_listening):
            data = st.get_screenshot_array()
            prediction = get_prediction(data)
            key, key_desc = kb.get_keys_to_press(prediction)
            print(count, key_desc)
            count = count + 1
            kb.press_keys(key)
        else:
            kb.clear_pressed_keys()

        time.sleep(1 / frames_per_second)

    kb.clear_pressed_keys()


if __name__ == "__main__":
    main()
