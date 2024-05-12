import tensorflow as tf


class Discriminator:
    def __int__(self):
        super().__init__()
        self.model = tf.keras.Sequential()

    def make_discriminator_model(self):
        #1st Network
        self.model.add(tf.keras.layers.
                       Conv2D(64, (5, 5), strides=(2, 2), padding='same', input_shape=[28, 28, 1])
                       )
        self.model.add(tf.keras.layers.LeakyReLU())
        self.model.add(tf.keras.layers.Dropout(0.3))

        #2nd Network
        self.model.add(tf.keras.layers.
                       Conv2D(128, (5, 5), strides=(2, 2), padding='same')
                       )
        self.model.add(tf.keras.layers.LeakyReLU())
        self.model.add(tf.keras.layers.Dropout(0.3))

        #3rd Network
        self.model.add(tf.keras.layers.Flatten())
        self.model.add(tf.keras.layers.Dense(1))

        return self.model
