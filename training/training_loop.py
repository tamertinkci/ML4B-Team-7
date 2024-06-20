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


# change grayscale to rbg if pictures are not colored
def load_data(image_dir, batch_size, buffer_size, purpose='training'):
    if purpose == 'training':
        image_dataset, val_set = tf.keras.utils.image_dataset_from_directory(
            image_dir,
            image_size=IMAGE_SIZE,
            color_mode='rgb',
            batch_size=batch_size,
            shuffle=True,
            seed=42,
            validation_split=0.15,
            subset='both'
        )

        image_dataset = image_dataset.map(preprocess_image)
        val_set = val_set.map(preprocess_image)
        image_dataset = image_dataset.shuffle(buffer_size, seed=42).prefetch(tf.data.AUTOTUNE)

        # return validation set too
        return image_dataset, val_set

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
    # End of function


'''
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
    # End of function
'''


# I use 'epoch + 1' because range(x) in from 0 to x-1
def train(generator, discriminator, train_dataset, val_dataset, noise, epochs):
    gen_optimizer = loss_calc.optimization()
    disc_optimizer = loss_calc.optimization()
    gen_loss_metric = loss_calc.loss_metric()
    disc_loss_metric = loss_calc.loss_metric()
    gen_loss = 0
    disc_loss = 0

    for epoch in range(epochs):
        start_time = time.time()

        # training
        for image_batch in train_dataset:
            gen_loss, disc_loss = _train_step(generator, discriminator,
                                              gen_optimizer, disc_optimizer, image_batch, noise)

        # Validation
        for images in val_dataset:
            _validation_step(generator, discriminator, gen_loss_metric,
                             disc_loss_metric, images, noise)

        # Print image // Not necessary // Just for fun!!!
        display.clear_output(wait=True)
        _generate_and_save_images(
            generator,
            noise,
            epoch + 1
        )

        # Save checkpoint
        if epoch % 20 == 0 and epoch != 0:
            _save_checkpoint(generator, discriminator, gen_optimizer, disc_optimizer)

        # Print progress
        _print_info(epoch + 1, start_time, gen_loss, disc_loss)

    # Generate after the final epoch
    display.clear_output(wait=True)
    _generate_and_save_images(generator, noise, epochs)
    # End of  train function


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


# @tf.function    # Improves efficiency
def _validation_step(gen_model, disc_model, gen_loss_metric, disc_loss_metric, images, noise):
    generated_images = gen_model(noise, training=False)
    real_output = disc_model(images[0], training=False)
    fake_output = disc_model(generated_images, training=False)

    disc_loss = loss_calc.discriminator_loss(real_output, fake_output)
    gen_loss = loss_calc.generator_loss(fake_output)

    gen_loss_metric.update_state(gen_loss)
    disc_loss_metric.update_state(disc_loss)
    # return gen_loss, disc_loss
    # End of function


def _generate_and_save_images(model, noise, epoch):
    generated_images = model(noise, training=False)

    num_images = min(generated_images.shape[0], 16)
    plt.figure(figsize=(4, 4))

    for index in range(num_images):
        plt.subplot(4, 4, index + 1)
        plt.imshow(generated_images[index, :, :, 0] * 127.5 + 127.5)
        plt.axis('off')

    plt.savefig('./data/train_generated/image_at_epoch_{:03d}.png'.format(epoch))
    # End of function


def _save_checkpoint(generator, discriminator, gen_optimizer, disc_optimizer):
    checkpoint_dir = './training_checkpoints'
    checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
    checkpoint = tf.train.Checkpoint(generator_optimizer=gen_optimizer,
                                     discriminator_optimizer=disc_optimizer,
                                     generator=generator,
                                     discriminator=discriminator
                                     )
    checkpoint.save(file_prefix=checkpoint_prefix)
    # End of function


def _print_info(epoch, start_time, gen_loss, disc_loss):
    elapsed_time = time.time() - start_time

    print(f'Epoch: {epoch}, Time: {elapsed_time}s, '
          f'Gen Loss: {gen_loss}, Disc Loss: {disc_loss}')
    # End of function
