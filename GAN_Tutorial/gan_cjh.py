import tensorflow as tf
import numpy as np

batch_size = 1024
hidden_size = 512
minibatch_bool = False
num_steps = 5000



def linear(input, output_dim, scope=None, stddev=1.0):
    """
    :param input: X
    :param output_dim: dim
    :param scope:
    :param stddev:
    :return: XW + B
    :description;

    """
    with tf.variable_scope(scope or 'linear'):
        w = tf.get_variable(
            'w',
            shape=[input.get_shape()[1], output_dim],
            initializer=tf.random_normal_initializer(stddev=stddev)
        ) # 현재의 variable scope에서 'w' 라는 이름을 갖고 있는 tf varaible을 가져온다.
        b = tf.get_variable(
            'b',
            [output_dim],
            initializer=tf.constant_initializer(0.0)
        )
        return tf.matmul(input, w) + b


def discriminator(input, h_dim, minibatch_layer=True):
    h0 = tf.nn.relu(linear(input, h_dim*2, 'd0'))
    h1 = tf.nn.relu(linear(h0, h_dim*2, 'd1'))

    if minibatch_layer:
        h2 = minibatch(h1)
    else:
        h2 = tf.nn.relu(linear(h1,h_dim*2,scope='d2'))

    h3 = tf.sigmoid(linear(h2, 1, scope='d3'))
    return h3


def optimizer(loss, var_list, learning_rate=0.001):
    step = tf.Variable(0, trainable=False)
    optimizer = tf.train.AdamOptimizer(learning_rate).minimize(
        loss,
        global_step=step,
        var_list=var_list
    )
    return optimizer




def minibatch(input, num_kernels=5, kernel_dim=3):
    x = linear(input, num_kernels * kernel_dim, scope='minibatch', stddev=0.02)
    activation = tf.reshape(x, (-1, num_kernels, kernel_dim))
    diffs = tf.expand_dims(activation,3) - \
        tf.expand_dims(tf.transpose(activation,[1,2,0]), 0)
    abs_diffs = tf.reduce_sum(tf.abs(diffs), axis=2)
    minibatch_features = tf.reduce_sum(tf.exp(-abs_diffs), axis=2)
    return tf.concat([input, minibatch_features], axis=1)


def generator(input, h_dim):

    h0 = tf.nn.softplus(linear(input, h_dim, 'g0')) # log(exp(features) + 1)를 계산함.
    h1 = linear(h0, 1, 'g1')
    return h1


def log(value):
    """
    :param value: value to log
    :return: loged value (Numerically stable)
    """
    return tf.log(tf.maximum(value, 1e-5))


class GAN(object):

    def __init__(self):

        # Generator Network : Noise로부터 sample을 생성
        #
        with tf.variable_scope('Generator'):
            self.z = tf.placeholder(tf.float32, shape=(batch_size, 1))
            self.G = generator(self.z, hidden_size)


        # Discriminator Network는 정답 데이터 (self.x)와 생성 데이터(self.z)를 구분하려 한다.
        self.x = tf.placeholder(tf.float32, shape=(batch_size, 1))
        with tf.variable_scope('Discriminator'):
            self.D1 = discriminator(
                self.x,
                hidden_size,
                minibatch_bool
            )
        with tf.variable_scope('Discriminator', reuse=True):
            self.D2 = discriminator(
                self.G,
                hidden_size,
                minibatch_bool
            )

        # 각 Network의 Loss를 정의한다
        self.loss_d = tf.reduce_mean(-log(self.D1) - log(1-self.D2))
        self.loss_g = tf.reduce_mean(-log(self.D2))

        vars = tf.trainable_variables()
        self.d_params = [v for v in vars if v.name.startswith('D/')]
        self.g_params = [v for v in vars if v.name.startswith('G/')]

        self.opt_d = optimizer(self.loss_d, self.d_params)
        self.opt_g = optimizer(self.loss_g, self.g_params)


def train(model, data, gen, params):

    with tf.Session() as session:
        tf.local_variables_initializer().run()
        tf.global_variables_initializer().run()

        for step in range(num_steps + 1):
            x = data.sample(batch_size)
            z = gen.sample(batch_size)
            loss_d, -, = session.run([model.loss_d, model.opt_d], {
                model.x: np.reshape(x, (batch_size, 1)),
                model.z: np.reshape(z, (batch_size, 1))
            })

