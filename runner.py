from pynput import keyboard
from pynput.keyboard import Key, Controller
from PIL import ImageGrab, Image
import tensorflow as tf
import numpy as np
import time
import math
import cnn_model

is_running = True
is_playing = False

tf.reset_default_graph()

input_length = 10240
ouput_length = 9

frames_per_second = 5
resize_percentage = 0.2

current_keys = set()

width = int(640 * 0.2)
height = int(400 * 0.2)
channels = 9

x = tf.placeholder(tf.float32, shape=[None, width * height])
y = tf.placeholder(tf.float32, shape=[None, channels])
model = cnn_model.Model(width, height, channels, x, 1.0, y)


def load_model(session):
    print("Loading model...")

    saver = tf.train.Saver()
    saver.restore(session, "tmp/cnn.ckpt")


def calculate_one_hot(session, data):
    formatted = list(map(lambda cell: cell / 255, data))

    result = session.run(model.prediction, {x: [formatted]})

    return result[0]


def get_direction(one_hot):
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
        print('nothing {0}|{1}'.format(found, one_hot))
        return ''


def setup_keyboard_listening():

    def on_press(key):
        global is_running
        global is_playing

        if key == Key.f10:
            is_playing = not is_playing
            if is_playing:
                print('Playing started...')
            else:
                print('Playing stopped.')
        if key == Key.f12:
            is_running = False
            print('App Stopped')

    listen = keyboard.Listener(on_press=on_press)

    listen.start()


def get_screenshot_data():
    img = ImageGrab.grab()  # grab full screen
    img = img.convert("L")  # convert to greyscale
    img = img.resize((math.floor(img.width * resize_percentage),
                      math.floor(img.height * resize_percentage)), Image.BILINEAR)

    pixels = img.getdata()

    return list(pixels)


def press_keys(keys):
    keyboard = Controller()

    for key in current_keys:
        keyboard.release(key)

    for key in keys:
        current_keys.add(key)
        keyboard.press(key)
        # print(key)


print('Starting...')
setup_keyboard_listening()

with tf.Session() as session:
    load_model(session)
    while is_running:
        while is_playing:
            data = get_screenshot_data()
            one_hot = calculate_one_hot(session, data)
            direction_keys = get_direction(one_hot)

            press_keys(direction_keys)

            time.sleep(1 / frames_per_second)
        press_keys([])  # clear any pressed keys

    press_keys([])  # clear any pressed keys

print("Complete.")
