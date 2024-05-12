import tensorflow as tf


class Generator:
    def __int__(self):
        super().__init__()
        self.model = tf.keras.Sequential()

    def make_generator_model(self):
        # 1st Network
        self.model.add(tf.keras.layers.
                       Dense(7 * 7 * 256, use_bias=False, input_shape=(100,))
                       )
        self.model.add(tf.keras.layers.BatchNormalization())
        self.model.add(tf.keras.layers.LeakyReLU())

        self.model.add(tf.keras.layers.
                       Reshape((7, 7, 256))
                       )
        self._check_shape("Dense_Layer", (None, 7, 7, 256))

        # 2nd Network
        self.model.add(tf.keras.layers.
                       Conv2DTranspose(128, (5, 5), strides=(1, 1), padding='same', use_bias=False)
                       )
        self._check_shape("1st Convolution", (None, 7, 7, 128))
        self.model.add(tf.keras.layers.
                       BatchNormalization()
                       )
        self.model.add(tf.keras.layers.LeakyReLU())

        # 3rd Network
        self.model.add(tf.keras.layers.
                       Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False)
                       )
        self._check_shape("2nd Convolution", (None, 14, 14, 64))
        self.model.add(tf.keras.layers.
                       BatchNormalization()
                       )
        self.model.add(tf.keras.layers.
                       LeakyReLU()
                       )

        # 4th Network
        self.model.add(tf.keras.layers.
                       Conv2DTranspose(1, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='tanh')
                       )
        self._check_shape("3rd Convolution & Activation", (None, 28, 28, 1))

        return self.model

    def _check_shape(self, location, shape):
        if self.model.output_shape != shape:
            print("Location: " + location)
            print("Expected " + shape + " but found " + self.model.output_shape)
