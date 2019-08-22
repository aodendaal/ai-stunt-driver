from PIL import Image
import numpy as np
import pandas as pd
import screenshot_taker as st

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


def load(filename):
    df = pd.read_csv(filename, header=None)

    total = get_record_count()

    image_data = np.empty([total, st.get_height(), st.get_width(), st.channels])
    label_data = np.empty([total, 1])

    for index, row in df.iterrows():
        arr = get_image_data(image_path + row[0])
        image_data[index] = arr
        label_data[index] = row[1]

    return image_data, label_data


def load_data():
    return load(data_filename)


def load_test_data():
    return load(test_data_filename)


def compile_data():
    df = pd.read_csv(data_filename, header=None)

    total = get_record_count()

    image_data = np.empty([total, 80, 128])
    label_data = np.empty([total, 1])

    for index, row in df.iterrows():
        arr = get_image_data(image_path + row[0])
        image_data[index] = arr
        label_data[index] = row[1]

    print("Saving image data")
    np.save('./data/image_data.npy', image_data)

    print("Saving label data")
    np.save('./data/label_data.npy', label_data)


def main():
    image_data, label_data = load_data()

    print(image_data.shape)
    print(label_data.shape)

    test_image_data, test_label_data = load_test_data()

    print(test_image_data.shape)
    print(test_label_data.shape)

    # compile_data()


if __name__ == "__main__":
    main()
