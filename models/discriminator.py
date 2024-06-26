import tensorflow as tf


def create_discriminator_model():
    disc_model = tf.keras.Sequential()

    # Input Layer: 1
    disc_model.add(tf.keras.layers.
                   Conv2D(64, (5, 5), strides=(2, 2), padding='same', input_shape=[100, 100, 3])
                   )
    disc_model.add(tf.keras.layers.LeakyReLU())
    disc_model.add(tf.keras.layers.Dropout(0.3))

    # Hidden Layer: 1
    disc_model.add(tf.keras.layers.
                   Conv2D(128, (5, 5), strides=(2, 2), padding='same')
                   )
    disc_model.add(tf.keras.layers.LeakyReLU())
    disc_model.add(tf.keras.layers.Dropout(0.3))

    # Layer 2
    disc_model.add(tf.keras.layers.Conv2D(256, (5, 5), strides=(2, 2), padding='same'))
    disc_model.add(tf.keras.layers.LeakyReLU())
    disc_model.add(tf.keras.layers.Dropout(0.3))

    # Additional Layer for better feature extraction
    disc_model.add(tf.keras.layers.Conv2D(512, (5, 5), strides=(2, 2), padding='same'))
    disc_model.add(tf.keras.layers.LeakyReLU())
    disc_model.add(tf.keras.layers.Dropout(0.3))

    # Output Layer
    disc_model.add(tf.keras.layers.Flatten())
    disc_model.add(tf.keras.layers.Dense(1))

    return disc_model
