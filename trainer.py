import tensorflow as tf
import cnn_model
import training_data

print('loading training data')
data, labels = training_data.get_data_and_labels()
print('finished loading training data')
print('records found: {0}'.format(len(data)))

with tf.Session() as session:
    x = tf.placeholder(tf.float32, shape=[None, training_data.width * training_data.height])
    y = tf.placeholder(tf.float32, shape=[None, training_data.channels])

    model = cnn_model.Model(training_data.width, training_data.height, training_data.channels, x, 0.9, y)

    init = tf.global_variables_initializer()
    session.run(init)

    session.run(model.optimize, feed_dict={x: data, y: labels})

    test_data, test_labels = training_data.get_test_data_and_labels()

    result = session.run(model.error, feed_dict={x: test_data, y: test_labels})
    print("Accuracy: {0}%".format(int(result * 100)))

    saver = tf.train.Saver()
    save_path = saver.save(session, "tmp/cnn.ckpt")
