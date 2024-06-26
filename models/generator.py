import tensorflow as tf


def create_generator_model():
    gen_model = tf.keras.Sequential()

    # Input
    gen_model.add(tf.keras.layers.Dense(25 * 25 * 256, use_bias=False, input_shape=(100,)))
    gen_model.add(tf.keras.layers.BatchNormalization())
    gen_model.add(tf.keras.layers.LeakyReLU())

    gen_model.add(tf.keras.layers.Reshape((25, 25, 256)))
    _check_shape(gen_model, "Input_Layer", (None, 25, 25, 256))

    # Upsampling Layers: Layer 1
    gen_model.add(tf.keras.layers.Conv2DTranspose(128, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    _check_shape(gen_model, "1st_Upsampling", (None, 50, 50, 128))
    gen_model.add(tf.keras.layers.BatchNormalization())
    gen_model.add(tf.keras.layers.LeakyReLU())

    # Layer 2
    gen_model.add(tf.keras.layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    _check_shape(gen_model, "2nd_Upsampling", (None, 100, 100, 64))
    gen_model.add(tf.keras.layers.BatchNormalization())
    gen_model.add(tf.keras.layers.LeakyReLU())

    # Output layer
    gen_model.add(
        tf.keras.layers.Conv2DTranspose(3, (5, 5), strides=(1, 1), padding='same', use_bias=False, activation='tanh'))
    _check_shape(gen_model, "Output_Layer", (None, 100, 100, 3))

    return gen_model


def _check_shape(model, location, shape):
    if model.output_shape != shape:
        print("Location: " + location)
        print("Expected {0} but found {1}".format(shape, model.output_shape))
