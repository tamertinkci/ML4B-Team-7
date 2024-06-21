from models.gan import gan
import training.training_loop as trainer
import training.testing as tester
import tensorflow as tf

'''
All variables with ** could be changed to see how it affects performance
'''

BUFFER_SIZE = 3791  # Size of the training dataset **
BATCH_SIZE = 64     # **
NOISE_DIM = 100
EPOCHS = 100          # **

noise = tf.random.normal([BATCH_SIZE, NOISE_DIM])

'''
Possible reasons for ...
1. Model too small (x)
2. Data set not big enough (possibly)
3. Learn rate too big (?)

General TODOs
1. Check loss function (plot it) (maybe not necessary)

Next-In-Line TODOs
1. Reduce decrease in learn rate
2. Reduce or increase learn rate to see effect on pictures
3. Increase batch size
'''


def gan_training(directory):
    train_dataset, val_dataset = trainer.load_data(directory, BATCH_SIZE, BUFFER_SIZE)

    print("Staring training... ")

    generator = gan.get_generator()
    discriminator = gan.get_discriminator()

    discriminator.compile(optimizer='adam', loss='binary_crossentropy')
    generator.compile(optimizer='adam', loss='binary_crossentropy')

    with tf.device("/gpu:0"):
        trainer.train(
            generator,
            discriminator,
            train_dataset,
            val_dataset,
            noise,
            EPOCHS
        )

    print("Ending training...\n")
    print('Saving Models... ')

    generator.save(filepath='./artefacts/generator.h5')
    discriminator.save(filepath='./artefacts/discriminator.h5')

    print('models saved!\n')
    # End of function


def gan_testing(directory):
    print('Starting testing...')
    print('Loading dataset and models...')

    dataset = trainer.load_data(directory, BATCH_SIZE, BUFFER_SIZE, purpose='testing')
    gen_model = tf.keras.models.load_model(filepath='./artefacts/generator.h5')
    disc_model = tf.keras.models.load_model(filepath='./artefacts/discriminator.h5')

    print('Testing models...')

    tester.evaluate_disc_model(disc_model, dataset)
    tester.evaluate_gen_model(gen_model, dataset, noise)

    print('Testing Done!')
    # End of function


if __name__ == "__main__":
    train_directory = './data/Train'
    test_directory = './data/Test'

    # result = gan.generate_image_with_prediction(noise)
    # print(f'{result[1]}')

    gan_training(train_directory)
    gan_testing(test_directory)
    # End of function
