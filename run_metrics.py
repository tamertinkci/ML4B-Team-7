from models.gan import gan
import training.training_loop as trainer
# import testing.testing as tester
import tensorflow as tf

BUFFER_SIZE = 541  # Size of the training dataset
BATCH_SIZE = 32
NOISE_DIM = 100
EPOCHS = 100

noise = tf.random.normal([BATCH_SIZE, NOISE_DIM])


def gan_training(directory):
    dataset = trainer.load_data(directory, BATCH_SIZE, BUFFER_SIZE)

    print("Staring training... ")

    generator = gan.get_generator()
    discriminator = gan.get_discriminator()

    # with tf.device("/gpu:0"):
    trainer.train(
        generator,
        discriminator,
        dataset,
        noise,
        EPOCHS
    )

    print("Ending training...")


"""
def gan_testing(directory):
    dataset = trainer.load_data(directory, BATCH_SIZE, BUFFER_SIZE, purpose='testing')
    pass
"""

if __name__ == "__main__":
    train_directory = './data/Train'
    # test_directory = './data/Test'

    result = gan.generate_image_with_prediction(noise)
    print(f'{result[1]}')

    # gan_training(train_directory)
    # gan_testing(test_directory)
