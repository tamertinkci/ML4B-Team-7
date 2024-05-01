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
# Laden des MNIST-Datensatzes
mnist = tf.keras.datasets.mnist
(train_images, _), (_, _) = mnist.load_data()

# Normalisieren der Bilddaten auf den Bereich [0, 1]
train_images = train_images / 255.0

# Reshape der Bilddaten für den Generator
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1).astype('float32')

# Trainingsschritte
for epoch in range(num_epochs):
    # Schleife über den Datensatz
    for image_batch in train_images:
        # Trainiere den Generator
        noise = tf.random.normal([batch_size, noise_dim])
        with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
            generated_images = generator(noise, training=True)

            real_output = discriminator(image_batch, training=True)
            fake_output = discriminator(generated_images, training=True)

            gen_loss = generator_loss(fake_output)
            disc_loss = discriminator_loss(real_output, fake_output)

        gradients_of_generator = gen_tape.gradient(gen_loss, generator.trainable_variables)
        gradients_of_discriminator = disc_tape.gradient(disc_loss, discriminator.trainable_variables)

        generator_optimizer.apply_gradients(zip(gradients_of_generator, generator.trainable_variables))
        discriminator_optimizer.apply_gradients(zip(gradients_of_discriminator, discriminator.trainable_variables))
