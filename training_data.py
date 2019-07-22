from __future__ import absolute_import, division, print_function, unicode_literals
import pandas as pd  # Python Data Analysis Library
import numpy as np
import ast  # Abstrast Syntax Trees

resize_percentage = 0.2
width = int(640 * resize_percentage)
height = int(400 * resize_percentage)
channels = 9

skip_count = 0
recording_filename = "data/recording.csv"
test_filename = "data/test.csv"


def get_file_size():
    global recording_filename

    with open(recording_filename) as f:
        size = sum(1 for line in f)

    return size


def get_batch(count):
    global skip_count
    global recording_filename

    df = pd.read_csv(recording_filename, skiprows=skip_count, nrows=count)
    skip_count = skip_count + count
    data = df.to_numpy()
    raw_data = list(map(lambda row: ast.literal_eval(row[0]), data))
    training_data = list(map(lambda row: list(map(lambda cell: cell / 255, row)), raw_data))

    labels = list(map(lambda row: ast.literal_eval(row[1]), data))

    return training_data, labels


def get_test_data_and_labels():
    global test_filename

    df = pd.read_csv(test_filename)
    data = df.to_numpy()
    raw_data = list(map(lambda row: ast.literal_eval(row[0]), data))
    training_data = list(map(lambda row: list(map(lambda cell: cell / 255, row)), raw_data))

    labels = list(map(lambda row: ast.literal_eval(row[1]), data))

    return training_data, labels
