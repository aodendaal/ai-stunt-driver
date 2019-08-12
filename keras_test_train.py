from __future__ import absolute_import, division, print_function, unicode_literals
import image_training_data as training_data
from tensorflow.keras import datasets, layers, models


def main():
    train_images, train_labels = training_data.load_data()

    train_images = train_images.reshape((723, 80, 128, 1))
    train_images = train_images / 255.0

    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(80, 128, 1)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))

    model.summary()

    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(9, activation='softmax'))

    model.summary()

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(train_images, train_labels, epochs=5)

    test_loss, test_acc = model.evaluate(train_images, train_labels)

    model.save('./kerasmodel.h5')

    print(test_acc)


if __name__ == "__main__":
    main()
