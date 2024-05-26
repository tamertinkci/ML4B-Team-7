import tensorflow as tf


def create_generator_model():
    gen_model = tf.keras.Sequential()

    # 1st Network
    gen_model.add(tf.keras.layers.
                  Dense(7 * 7 * 256, use_bias=False, input_shape=(100,))
                  )
    gen_model.add(tf.keras.layers.BatchNormalization())
    gen_model.add(tf.keras.layers.LeakyReLU())

    gen_model.add(tf.keras.layers.
                  Reshape((7, 7, 256))
                  )
    _check_shape(gen_model, "Dense_Layer", (None, 7, 7, 256))

    # 2nd Network
    gen_model.add(tf.keras.layers.
                  Conv2DTranspose(128, (5, 5), strides=(1, 1), padding='same', use_bias=False)
                  )
    _check_shape(gen_model, "1st Convolution", (None, 7, 7, 128))
    gen_model.add(tf.keras.layers.
                  BatchNormalization()
                  )
    gen_model.add(tf.keras.layers.LeakyReLU())

    # 3rd Network
    gen_model.add(tf.keras.layers.
                  Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False)
                  )
    _check_shape(gen_model, "2nd Convolution", (None, 14, 14, 64))
    gen_model.add(tf.keras.layers.
                  BatchNormalization()
                  )
    gen_model.add(tf.keras.layers.
                  LeakyReLU()
                  )

    # 4th Network
    gen_model.add(tf.keras.layers.
                  Conv2DTranspose(1, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='tanh')
                  )
    _check_shape(gen_model, "3rd Convolution & Activation", (None, 28, 28, 1))

    return gen_model


def create_discriminator_model():
    disc_model = tf.keras.Sequential()

    # 1st Network
    disc_model.add(tf.keras.layers.
                   Conv2D(64, (5, 5), strides=(2, 2), padding='same', input_shape=[28, 28, 1])
                   )
    disc_model.add(tf.keras.layers.LeakyReLU())
    disc_model.add(tf.keras.layers.Dropout(0.3))

    # 2nd Network
    disc_model.add(tf.keras.layers.
                   Conv2D(128, (5, 5), strides=(2, 2), padding='same')
                   )
    disc_model.add(tf.keras.layers.LeakyReLU())
    disc_model.add(tf.keras.layers.Dropout(0.3))

    # 3rd Network
    disc_model.add(tf.keras.layers.Flatten())
    disc_model.add(tf.keras.layers.Dense(1))

    return disc_model


def _check_shape(model, location, shape):
    if model.output_shape != shape:
        print("Location: " + location)
        print("Expected " + shape + " but found " + model.output_shape)
