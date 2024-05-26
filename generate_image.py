import matplotlib.pyplot as plt

from models.gan import gan
import tensorflow as tf

noise = tf.random.normal([32, 100])


def generate_and_plot():
    image = _generate_image()
    _plot_image(image)


def download_image():
    pass


def _generate_image():
    image = gan.generate_image(noise)

    return image


def _plot_image(image):
    plt.figure(figsize=(4, 4))
    plt.subplot(1, 1, 1)
    plt.imshow(image[0, :, :, 0] * 127.5 + 127.5, cmap='viridis')
    plt.axis('off')

    plt.show()


if __name__ == "__main__":
    generate_and_plot()
