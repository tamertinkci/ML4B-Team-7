import random

import tensorflow as tf
import matplotlib.pyplot as plt

BUFFER_SIZE = 320
BATCH_SIZE = 64
EPOCHS = 50


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

        #Display image
        plt.imshow(images[0])
        plt.axis('off')
        plt.show()



def train_step(images):
    # actual code
    pass


def train(dataset, epochs):
    # actual code
    pass