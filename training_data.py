from PIL import Image
import numpy as np
import pandas as pd

data_filename = 'data/recording.csv'
test_data_filename = 'data/test.csv'
image_path = './screenshots/'


def get_record_count():
    df = pd.read_csv(data_filename, header=None)
    return df[0].count()


def get_test_record_count():
    df = pd.read_csv(test_data_filename, header=None)
    return df[0].count()


def get_record(index):
    df = pd.read_csv(data_filename, header=None)

    filename = df.iloc[index, 0]

    image = get_image_data(image_path + filename)
    label = df.iloc[index, 1]

    return image, label


def get_test_record(index):
    df = pd.read_csv(data_filename, header=None)

    filename = df.iloc[index, 0]

    image = get_image_data(image_path + filename)
    label = df.iloc[index, 1]

    return image, label


def get_image_data(fullfilename):
    img = Image.open(fullfilename)
    arr = np.array(img)
    return arr


def load_data():
    df = pd.read_csv(data_filename, header=None)

    image_data = np.empty([0, 80, 128])
    label_data = np.empty([0, 1])

    for _, row in df.iterrows():
        arr = get_image_data(image_path + row[0])
        image_data = np.append(image_data, [arr], axis=0)
        label_data = np.append(label_data, [[row[1]]], axis=0)

    return image_data, label_data


def load_test_data():
    df = pd.read_csv(test_data_filename, header=None)

    image_data = np.empty([0, 80, 128])
    label_data = np.empty([0, 1])

    for _, row in df.iterrows():
        arr = get_image_data(image_path + row[0])
        image_data = np.append(image_data, [arr], axis=0)
        label_data = np.append(label_data, [[row[1]]], axis=0)

    return image_data, label_data


def main():
    image_data, label_data = load_data()

    print(image_data.shape)
    print(label_data.shape)

    test_image_data, test_label_data = load_test_data()

    print(test_image_data.shape)
    print(test_label_data.shape)


if __name__ == "__main__":
    main()
