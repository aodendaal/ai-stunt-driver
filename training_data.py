import pandas as pd  # Python Data Analysis Library
import numpy as np
import ast  # Abstrast Syntax Trees

resize_percentage = 0.2
width = int(640 * resize_percentage)
height = int(400 * resize_percentage)
channels = 9


def get_data_and_labels():
    df = pd.read_csv("data/recording.csv")
    data = df.to_numpy()
    raw_data = list(map(lambda row: ast.literal_eval(row[0]), data))
    training_data = list(map(lambda row: list(map(lambda cell: cell / 255, row)), raw_data))

    labels = list(map(lambda row: ast.literal_eval(row[1]), data))

    return training_data, labels


def get_test_data_and_labels():
    df = pd.read_csv("data/test.csv")
    data = df.to_numpy()
    raw_data = list(map(lambda row: ast.literal_eval(row[0]), data))
    training_data = list(map(lambda row: list(map(lambda cell: cell / 255, row)), raw_data))

    labels = list(map(lambda row: ast.literal_eval(row[1]), data))

    return training_data, labels
