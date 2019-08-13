from __future__ import absolute_import, division, print_function, unicode_literals
import training_data
from tensorflow.keras import datasets, layers, models


def main():
    print('loading training data...')
    train_images, train_labels = training_data.load_data()
    print('training data loaded')

    train_size = training_data.get_record_count()
    train_images = train_images.reshape((train_size, 80, 128, 1))
    train_images = train_images / 255.0

    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(80, 128, 1)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))

    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(9, activation='softmax'))

    model.summary()

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(train_images, train_labels, epochs=5)

    # Testing
    test_images, test_labels = training_data.load_test_data()

    test_size = training_data.get_test_record_count()
    test_images = test_images.reshape((test_size, 80, 128, 1))
    test_images = test_images / 255.0

    test_loss, test_acc = model.evaluate(test_images, test_labels)

    model.save('./tmp/kerasmodel.h5')

    print(test_loss, test_acc)


if __name__ == "__main__":
    main()
