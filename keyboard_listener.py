from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
from pynput import keyboard
from pynput.keyboard import Key, Controller

has_started = True
is_listening = False
current_keys = set()
pressed_keys = set()


def on_press(key):
    global has_started
    global is_listening

    current_keys.add(key)

    if key == Key.f10:
        is_listening = not is_listening
        if is_listening:
            print('Listening...')
        else:
            print('Stopped listening.')
    if key == Key.f12:
        has_started = False
        print('App Stopped')


def on_release(key):
    current_keys.discard(key)


def setup_keyboard_listening():
    listen = keyboard.Listener(on_press=on_press, on_release=on_release)

    listen.start()
    print('App Started')


def press_keys(keys):
    keyboard = Controller()

    for key in pressed_keys:
        keyboard.release(key)

    for key in keys:
        pressed_keys.add(key)
        keyboard.press(key)


def clear_pressed_keys():
    press_keys([])  # clear any pressed keys


def get_current_keys():
    result = ''
    for key in current_keys:
        if hasattr(key, 'char'):
            result = result + key.char + '+'
        else:
            result = result + str(key) + '+'

    return result[:-1]


def get_keys_to_press(one_hot):
    found = np.argmax(one_hot)
    if (found == 0):
        return '', 'nothing'
    if (found == 1):
        return [Key.up, Key.left], 'up+left'
    elif (found == 2):
        return [Key.up], 'up'
    elif (found == 3):
        return [Key.up, Key.right], 'up+right'
    elif (found == 4):
        return [Key.left], 'left'
    elif (found == 5):
        return [Key.right], 'right'
    elif (found == 6):
        return [Key.down, Key.left], 'down+left'
    elif (found == 7):
        return [Key.down], 'down'
    elif (found == 8):
        return [Key.down, Key.right], 'down+right'
    else:
        return '', 'FUCK UP!'
