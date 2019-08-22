from __future__ import absolute_import, division, print_function, unicode_literals
import training_data
from tensorflow.keras import datasets, layers, models
import screenshot_taker as st


def main():
    print('loading training data...')
    train_images, train_labels = training_data.load_data()

    train_size = training_data.get_record_count()
    train_images = train_images / 255.0

    print('generating model...')
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(train_size, st.get_height(), st.get_width(), st.channels)))
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

    print('fitting data...')
    model.fit(train_images, train_labels, epochs=5)

    print('loading test data...')
    test_images, test_labels = training_data.load_test_data()
    test_images = test_images / 255.0

    print('evaluationg trained model...')
    test_loss, test_acc = model.evaluate(test_images, test_labels)

    print('saving model...')
    model.save('./tmp/kerasmodel.h5')

    print('Loss Value: {0}, Accuracy: {1}'.format(test_loss, test_acc))


if __name__ == "__main__":
    main()
