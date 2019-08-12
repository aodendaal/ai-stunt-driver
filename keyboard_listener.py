from __future__ import absolute_import, division, print_function, unicode_literals
from pynput import keyboard
from pynput.keyboard import Key, Controller

is_running = True
is_recording = False
current_keys = set()
pressed_keys = set()


def on_press(key):
    global is_running
    global is_recording

    current_keys.add(key)

    if key == Key.f10:
        is_recording = not is_recording
        if is_recording:
            print('Recording started...')
        else:
            print('Recording stopped.')
    if key == Key.f12:
        is_running = False
        print('App Stopped')


def on_release(key):
    current_keys.remove(key)


def setup_keyboard_listening():
    listen = keyboard.Listener(on_press=on_press, on_release=on_release)

    listen.start()


def press_keys(keys):
    keyboard = Controller()

    for key in pressed_keys:
        keyboard.release(key)

    for key in keys:
        pressed_keys.add(key)
        keyboard.press(key)


def get_current_keys():
    result = ''
    for key in current_keys:
        if hasattr(key, 'char'):
            result = result + key.char + '+'
        else:
            result = result + str(key) + '+'

    return result[:-1]
