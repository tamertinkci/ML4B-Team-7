import streamlit as st
import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

st.title('Wir erstellen unsere erste Apple')
def generator_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(256, input_shape=(100,), activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dense(28*28*1, activation='tanh'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Reshape((28, 28, 1))
    ])
    return model

def discriminator_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28, 1)),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    return model

generator = generator_model()
discriminator = discriminator_model()

gan_input = tf.keras.Input(shape=(100,))
gan_output = discriminator(generator(gan_input))

gan = tf.keras.Model(gan_input, gan_output)

cross_entropy = tf.keras.losses.BinaryCrossentropy()

generator_optimizer = tf.keras.optimizers.Adam(learning_rate=0.0002, beta_1=0.5)
discriminator_optimizer = tf.keras.optimizers.Adam(learning_rate=0.0002, beta_1=0.5)

