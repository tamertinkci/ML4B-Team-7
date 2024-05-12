import os.path

import tensorflow as tf

import models.generator as gen
import models.discriminator as disc

cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=True)

""" Loss Functions """


def discriminator_loss(real_output, fake_output):
    real_loss = cross_entropy(tf.ones_like(real_output), real_output)
    fake_loss = cross_entropy(tf.zeros_like(fake_output), fake_output)
    total_loss = real_loss + fake_loss

    return total_loss


def generator_loss(fake_output):
    loss = cross_entropy(tf.ones_like(fake_output), fake_output)

    return loss


""" Optimization """


def optimization():
    optimizer = tf.keras.optimizers.Adam(1e-4)

    return optimizer


# Not sure about keeping this
""" Checkpoints """


def save_checkpoint():
    checkpoint_dir = './training_checkpoints'
    os.path.join(checkpoint_dir, "ckpt")
    checkpoint = tf.train.Checkpoint(generator_optimizer=optimization(),
                                     discriminator_optimizer=optimization(),
                                     generator=gen.Generator().make_generator_model(),
                                     discriminator=disc.Discriminator().make_discriminator_model())
    return checkpoint
