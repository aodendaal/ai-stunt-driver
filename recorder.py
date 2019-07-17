from pynput import keyboard
from pynput.keyboard import Key
from PIL import ImageGrab, Image
import common

import time
import datetime
import os
import csv
import math

is_running = True
is_recording = False
current_keys = set()

output_filename = 'data/recording.csv'
frames_per_second = 5


def setup_keyboard_listening():

    def on_press(key):
        global is_running
        global is_recording
        global current_keys

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
        global current_keys

        current_keys.remove(key)

    listen = keyboard.Listener(on_press=on_press, on_release=on_release)

    listen.start()


def get_current_keys():
    result = ''
    for key in current_keys:
        if hasattr(key, 'char'):
            result = result + key.char + '+'
        else:
            result = result + str(key) + '+'

    return result[:-1]


def direction_to_onehot(input):
    if input == 'Key.up+Key.left' or input == 'Key.left+Key.up':
        return [1, 0, 0, 0, 0, 0, 0, 0, 0]
    elif input == 'Key.up':
        return [0, 1, 0, 0, 0, 0, 0, 0, 0]
    elif input == 'Key.up+Key.right' or input == 'Key.right+Key.up':
        return [0, 0, 1, 0, 0, 0, 0, 0, 0]
    elif input == 'Key.left':
        return [0, 0, 0, 1, 0, 0, 0, 0, 0]
    elif input == 'Key.right':
        return [0, 0, 0, 0, 1, 0, 0, 0, 0]
    elif input == 'Key.down+Key.left' or input == 'Key.left+Key.down':
        return [0, 0, 0, 0, 0, 1, 0, 0, 0]
    elif input == 'Key.down':
        return [0, 0, 0, 0, 0, 0, 1, 0, 0]
    elif input == 'Key.down+Key.right' or input == 'Key.right+Key.down':
        return [0, 0, 0, 0, 0, 0, 0, 1, 0]
    else:
        return [0, 0, 0, 0, 0, 0, 0, 0, 1]


def start_recorder():
    print('App Started')
    with open(output_filename, 'a', newline='\n') as recording_file:
        writer = csv.writer(recording_file)
        while is_running:
            while is_recording:
                data = common.get_screenshot_data()
                writer.writerow(
                    [data, direction_to_onehot(get_current_keys())])

                time.sleep(1 / frames_per_second)

    recording_file.close()


setup_keyboard_listening()
start_recorder()
