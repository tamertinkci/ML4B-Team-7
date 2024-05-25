import models.model_definition as models


class GAN:
    generator = models.create_generator_model()
    discriminator = models.create_discriminator_model()

    def __int__(self):
        super().__init__()
        # self.generator = models.create_generator_model()
        # self.discriminator = models.create_discriminator_model()

    def get_generator(self):
        return self.generator

    def get_discriminator(self):
        return self.discriminator

    def generate_image(self, noise):
        image = self.generator(noise, training=False)
        return image

    def make_image_prediction(self, image):
        prediction = self.discriminator(image, training=False)
        return prediction

    def generate_image_with_prediction(self, noise):
        image = self.generate_image(noise)
        prediction = self.make_image_prediction(image)

        return image, prediction

    def generate_good_image(self, noise):
        while True:
            image = self.generate_image(noise)
            prediction = self.make_image_prediction(image)

            if prediction > 0.6:
                return image


# Global GAN Instance
gan = GAN()
