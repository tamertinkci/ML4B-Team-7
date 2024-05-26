import tensorflow as tf

import matplotlib

import matplotlib.pyplot as plt

import os.path
import time
import random

from IPython import display

import training.loss_calculator as loss_calc

matplotlib.use('Agg')

IMAGE_SIZE = (28, 28)


def preprocess_image(image, label):
    image = tf.cast(image, tf.float32)
    image = 2.0 * image / 255.0 - 1.0
    return image, label


# Remove 2nd part (purpose == testing)t if test package is needed
# change grayscale to rbg if pictures are not colored
def load_data(image_dir, batch_size, buffer_size, purpose='training'):
    if purpose == 'training':
        image_dataset = tf.keras.utils.image_dataset_from_directory(
            image_dir,
            image_size=IMAGE_SIZE,
            color_mode='grayscale',
            batch_size=batch_size,
            shuffle=True,
            seed=42,
            validation_split=0.2,
            subset=purpose
        )

        image_dataset = image_dataset.map(lambda image, label: preprocess_image(image, label))
        image_dataset = image_dataset.shuffle(buffer_size, seed=42).prefetch(tf.data.AUTOTUNE)

        return image_dataset

    elif purpose == 'testing':
        image_dataset = tf.keras.utils.image_dataset_from_directory(
            image_dir,
            image_size=IMAGE_SIZE,
            batch_size=batch_size,
            shuffle=False
        )

        image_dataset = image_dataset.map(lambda image, label: (2.0 * image / 255.0 - 1.0, label))
        image_dataset = image_dataset.prefetch(tf.data.AUTOTUNE)

        return image_dataset


# For visual tests
# Not really necessary otherwise
def load_and_show(image_dir, buffer_size, purpose='training'):
    dataset = load_data(image_dir, buffer_size, purpose)
    index = random.randint(0, len(dataset))

    for images, labels in dataset.take(index):
        # Display some information
        print("Image batch shape: ", images.shape)
        print("Image batch data type: ", images.dtype)

        # Display image
        plt.imshow(images[0])
        plt.axis('off')
        plt.show()


@tf.function  # Improves efficiency
def _train_step(gen_model, disc_model, gen_optimizer, disc_optimizer, images, noise):
    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        generated_images = gen_model(noise, training=True)

        real_output = disc_model(images[0], training=True)
        fake_output = disc_model(generated_images, training=True)

        gen_loss = loss_calc.generator_loss(fake_output)
        disc_loss = loss_calc.discriminator_loss(real_output, fake_output)

    generator_gradients = gen_tape.gradient(gen_loss, gen_model.trainable_variables)
    discriminator_gradients = disc_tape.gradient(disc_loss, disc_model.trainable_variables)

    gen_optimizer.apply_gradients(zip(generator_gradients, gen_model.trainable_variables))
    disc_optimizer.apply_gradients(zip(discriminator_gradients, disc_model.trainable_variables))

    return gen_loss, disc_loss


# I use 'epoch + 1' because range(x) in from 0 to x-1
def train(generator, discriminator, dataset, noise, epochs):
    gen_optimizer = loss_calc.optimization()
    disc_optimizer = loss_calc.optimization()
    gen_loss = 0
    disc_loss = 0

    for epoch in range(epochs):
        start_time = time.time()

        for image_batch in dataset:
            gen_loss, disc_loss = _train_step(generator, discriminator,
                                              gen_optimizer, disc_optimizer, image_batch, noise)

        # Print image // Not necessary // Just for fun!!!
        display.clear_output(wait=True)
        _generate_and_save_images(
            generator,
            noise,
            epoch + 1
        )

        if epoch % 20 == 0 and epoch != 0:
            _save_checkpoint(generator, discriminator, gen_optimizer, disc_optimizer)

        _print_info(epoch + 1, start_time, gen_loss, disc_loss)

    # Generate after the final epoch
    display.clear_output(wait=True)
    _generate_and_save_images(generator, noise, epochs)


def _generate_and_save_images(model, noise, epoch):
    generated_images = model(noise, training=False)

    num_images = min(generated_images.shape[0], 16)
    plt.figure(figsize=(4, 4))

    for index in range(num_images):
        plt.subplot(4, 4, index + 1)
        plt.imshow(generated_images[index, :, :, 0] * 127.5 + 127.5, cmap='viridis')
        plt.axis('off')

    plt.savefig('image_at_epoch_{:03d}.png'.format(epoch))
    plt.show()


def _save_checkpoint(generator, discriminator, gen_optimizer, disc_optimizer):
    checkpoint_dir = './training_checkpoints'
    checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
    checkpoint = tf.train.Checkpoint(generator_optimizer=gen_optimizer,
                                     discriminator_optimizer=disc_optimizer,
                                     generator=generator,
                                     discriminator=discriminator
                                     )
    checkpoint.save(file_prefix=checkpoint_prefix)


def _print_info(epoch, start_time, gen_loss, disc_loss):
    original_time = time.time() - start_time
    record = []
    time_in_secs = original_time

    while time_in_secs >= 60:
        z = time_in_secs % 60
        record.append(z)
        time_in_secs = time_in_secs / 60

        if len(record) > 3:
            break

    if len(record) > 0:
        if len(record) == 3:
            print(f'Epoch: {epoch}, Time: {record[2]}:{record[1]}:{record[0]}, '
                  f'Gen Loss: {gen_loss}, Disc Loss: {disc_loss}')
        elif len(record) == 2:
            print(f'Epoch: {epoch}, Time: {record[2]}:{record[1]}:{record[0]}, '
                  f'Gen Loss: {gen_loss}, Disc Loss: {disc_loss}')
    else:
        print(f'Epoch: {epoch}, Time: {original_time}, '
              f'Gen Loss: {gen_loss}, Disc Loss: {disc_loss}')
