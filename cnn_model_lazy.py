from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import numpy as np
import common


class Model:
    def __init__(self, width, height, output_channels, data, keep_prob, labels):
        self.width = width
        self.height = height
        self.output_length = output_channels

        self.data = data
        self.keep_prob = keep_prob
        self.labels = labels

        self._prediction = None
        self._optimize = None
        self._error = None

        self.prediction
        self.optimize
        self.error

    @property
    def prediction(self):
        if self._prediction == None:
            #x = tf.placeholder(tf.float32, shape=[None, flat])
            #y_ = tf.placeholder(tf.float32, shape=[None, output])

            x_image = tf.reshape(self.data, [-1, self.height, self.width, 1])  # [batch, in_height, in_width, in_channels]

            W_conv1 = tf.Variable(tf.truncated_normal([5, 5, 1, 32], stddev=0.1))
            b_conv1 = tf.Variable(tf.constant(0.1, shape=[32]))

            convolve1 = tf.nn.conv2d(x_image, W_conv1, strides=[1, 1, 1, 1], padding='SAME') + b_conv1
            h_conv1 = tf.nn.relu(convolve1)
            conv1 = tf.nn.max_pool(h_conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

            W_conv2 = tf.Variable(tf.truncated_normal([5, 5, 32, 64], stddev=0.1))
            b_conv2 = tf.Variable(tf.constant(0.1, shape=[64]))

            convolve2 = tf.nn.conv2d(conv1, W_conv2, strides=[1, 1, 1, 1], padding='SAME') + b_conv2
            h_conv2 = tf.nn.relu(convolve2)
            conv2 = tf.nn.max_pool(h_conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

            layer2_matrix = tf.reshape(conv2, [-1, 20 * 32 * 64])

            W_fc1 = tf.Variable(tf.truncated_normal([20 * 32 * 64, 1024], stddev=0.1))
            b_fc1 = tf.Variable(tf.constant(0.1, shape=[1024]))

            fcl = tf.matmul(layer2_matrix, W_fc1) + b_fc1
            h_fc1 = tf.nn.relu(fcl)

            #keep_prob = tf.placeholder(tf.float32)
            layer_drop = tf.nn.dropout(h_fc1, rate=1-self.keep_prob)

            W_fc2 = tf.Variable(tf.truncated_normal([1024, self.output_length], stddev=0.1))
            b_fc2 = tf.Variable(tf.constant(0.1, shape=[self.output_length]))

            fc = tf.matmul(layer_drop, W_fc2) + b_fc2

            self._prediction = tf.nn.softmax(fc)
        return self._prediction

    @property
    def optimize(self):
        if self._optimize == None:
            cross_entropy = tf.reduce_mean(-tf.reduce_sum(self.labels * tf.log(self.prediction), reduction_indices=[1]))
            self._optimize = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
        return self._optimize

    @property
    def error(self):
        if self._error == None:
            correct_prediction = tf.equal(tf.argmax(self.prediction, 1), tf.argmax(self.labels, 1))
            self._error = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        return self._error
