from __future__ import absolute_import, division, print_function, unicode_literals
from tensorflow.keras import datasets, layers, models
import image_training_data as training_data
import numpy as np

model = None


def get_model():
    global model

    print('loading model')
    model = models.load_model('./kerasmodel.h5')


def get_prediction(data):
    if model == None:
        get_model()

    data = data.reshape(1, 80, 128, 1)
    prediction = model.predict(data)

    return prediction


def get_data(index):
    image, label = training_data.get_record(index)
    return image, label


def main():
    count = training_data.get_record_count()
    results = []
    for i in range(count):
        data, label = get_data(i)
        prediction = get_prediction(data)
        compare = np.argmax(prediction) == label
        if not compare:
            print(i, np.argmax(prediction), label)
        results.append(compare)

    print(np.mean(results))
    # print(results)
    #print(np.argmax(prediction), label)


if __name__ == "__main__":
    main()
