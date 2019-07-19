import tensorflow as tf
import cnn_model
import training_data
import numpy as np

with tf.Session() as session:
    x = tf.placeholder(tf.float32, shape=[None, training_data.width * training_data.height])
    y = tf.placeholder(tf.float32, shape=[None, training_data.channels])

    model = cnn_model.Model(training_data.width, training_data.height, training_data.channels, x, 0.9, y)

    init = tf.global_variables_initializer()
    session.run(init)

    data_total = training_data.get_file_size()
    count = 0

    while True:
        batch_size = np.minimum(data_total, 100)
        data_total = data_total - batch_size
        print('Processing batch {0} - {1} rows remaining'.format(count, data_total))

        data, labels = training_data.get_batch(batch_size)
        session.run(model.optimize, feed_dict={x: data, y: labels})

        count = count + 1

        if (data_total == 0):
            break

    print('Testing accuracy')
    test_data, test_labels = training_data.get_test_data_and_labels()

    result = session.run(model.error, feed_dict={x: test_data, y: test_labels})
    print('Accuracy: {0}%'.format(int(result * 100)))

    saver = tf.train.Saver()
    save_path = saver.save(session, 'tmp/cnn.ckpt')
