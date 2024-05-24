import tensorflow as tf
import matplotlib.pyplot as plt
import os.path
import time
import random

from IPython import display

import loss_calculator as loss_calc

BUFFER_SIZE = 320
BATCH_SIZE = 64
NOISE_DIM = 100


# Remove 2nd part (purpose == testing)t if test package is needed
def load_data(image_dir, image_size=(256, 256), purpose='training'):
    image_dataset = []

    if purpose == 'training':
        image_dataset = tf.keras.utils.image_dataset_from_directory(
            image_dir,
            image_size=image_size,
            batch_size=BATCH_SIZE,
            shuffle=True,
            seed=123,
            validation_split=0.2,
            subset=purpose
        )

        image_dataset = image_dataset.map(lambda image, label: (2.0 * image / 255.0 - 1.0, label))
        image_dataset = image_dataset.shuffle(buffer_size=BUFFER_SIZE).batch(BATCH_SIZE)

    elif purpose == 'testing':
        image_dataset = tf.keras.utils.image_dataset_from_directory(
            image_dir,
            image_size=image_size,
            batch_size=BATCH_SIZE,
            shuffle=False
        )

        # Might be problematic later for whatever reason -> more than one implementation for map() and Batch()
        image_dataset = image_dataset.map(lambda image, label: (2.0 * image / 255.0 - 1.0, label))
        image_dataset = image_dataset.batch(BATCH_SIZE)

    return image_dataset


# For visual tests
# Not really necessary otherwise
def load_and_show(image_dir, image_size=(256, 256), purpose='training'):
    dataset = load_data(image_dir, image_size, purpose)
    index = random.randint(0, len(dataset))

    for images, labels in dataset.take(index):
        # Display some information
        print("Image batch shape: ", images.shape)
        print("Image batch data type: ", images.dtype)

        # Display image
        plt.imshow(images[0])
        plt.axis('off')
        plt.show()


# @tf.function // Not sure whether to compile this here (?)
# TODO: update if more functions are added to loss_calculation
def _train_step(gen_model, disc_model, gen_optimizer, disc_optimizer, images, noise):
    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        generated_images = gen_model(noise, training=True)

        real_output = disc_model(images, training=True)
        fake_output = disc_tape(generated_images, training=True)

        gen_loss = loss_calc.generator_loss(fake_output)
        disc_loss = loss_calc.discriminator_loss(real_output, fake_output)

    generator_gradients = gen_tape.gradient(gen_loss, gen_model.trainable_variables)
    discriminator_gradients = disc_tape.gradient(disc_loss, disc_model.trainable_variables)

    gen_optimizer.apply_gradients(generator_gradients, gen_model.trainable_variables)
    disc_optimizer.apply_gradients(discriminator_gradients, disc_model.trainable_variables)


def train(generator, discriminator, dataset, epochs):
    gen_optimizer = loss_calc.optimization()
    disc_optimizer = loss_calc.optimization()
    noise = tf.random.normal([BATCH_SIZE, NOISE_DIM])

    for epoch in range(epochs):
        start_time = time.time()

        for image_batch in dataset:
            _train_step(generator, discriminator, gen_optimizer, disc_optimizer, image_batch, noise)

        # Print image // Not necessary (Just for fun!!!)
        display.clear_output(wait=True)
        _generate_and_save_images(
            generator,
            noise,
            epoch + 1
        )

        if (epoch + 1) % 15 == 0:
            _save_checkpoint(generator, discriminator, gen_optimizer, disc_optimizer)

        _print_elapsed_time(epoch, start_time)

    display.clear_output(wait=True)
    _generate_and_save_images(generator, noise, epochs)


def _generate_and_save_images(model, noise, epoch):
    generated_images = model(noise, training=False)

    fig = plt.figure(figsize=(4, 4))

    for index in range(generated_images.shape[0]):
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


def _print_elapsed_time(epoch, start_time):
    original_time = time.time() - start_time
    record = []
    time_in_secs = original_time

    while time_in_secs >= 60:
        z = time_in_secs % 60
        record.append(z)
        time_in_secs = time_in_secs / 60

        if len(record) > 3:
            break

    if len(record) == 3:
        print(
            "Time for epoch {} is {} hours: {} minutes: {} seconds".format(epoch + 1, record[2], record[1], record[0]))
    elif len(record) == 2:
        print("Time for epoch {} is {}: minutes: {} seconds".format(epoch + 1, record[1], record[0]))
    else:
        print("Time for epoch {} is {} seconds".format(epoch + 1, record[0]))
