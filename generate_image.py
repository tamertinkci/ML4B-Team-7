import matplotlib.pyplot as plt
from PIL import Image
from models.gan import gan
import tensorflow as tf
from matplotlib.backends.backend_agg import FigureCanvasAgg


noise = tf.random.normal([32, 100])


def generate_and_plot():
    image = _generate_image()
    return_image = _plot_image(image)

    return return_image


def download_image():
    pass


def _generate_image():
    image = gan.generate_image(noise)

    return image


def _plot_image(image):
    fig, ax = plt.subplots(1, 1)
    im = ax.imshow(image[0, :, :, 0] * 127.5 + 127.5, cmap='viridis')
    canvas = FigureCanvasAgg(fig)
    canvas.draw()

    renderer = canvas.get_renderer()

    image_set = im.make_image(renderer)

    image_pil = Image.fromarray(image_set[0])

    return image_pil


if __name__ == "__main__":
    generate_and_plot()
