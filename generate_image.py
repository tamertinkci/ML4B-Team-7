import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from models.gan import gan
import tensorflow as tf
from matplotlib.backends.backend_agg import FigureCanvasAgg

""" API for UI 
"""

noise = tf.random.normal([32, 100])


def generate_and_plot():
    image = _generate_image()
    return_image = _plot_image(image)

    return return_image


def _generate_image():
    image = gan.generate_image(noise)

    return image


def _plot_image(image):
    # batch_size, height, width, channels = image.shape

    fig, ax = plt.subplots(1, 1)
    im = ax.imshow(image[0, :, :, 0] * 127.5 + 127.5)
    canvas = FigureCanvasAgg(fig)
    canvas.draw()

    renderer = canvas.get_renderer()

    image_set = im.make_image(renderer)

    image_pil = Image.fromarray(image_set[0])

    return image_pil


if __name__ == "__main__":
    img = generate_and_plot()
    img.show()

    img_2 = _generate_image()

    pred = gan.make_image_prediction(img_2)

    print(f'Prediction: {pred}')
