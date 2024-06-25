# The Applegenerator 
Apple Detection and Generation

Stephen Nkwelle (qi74ximu/22712737), Yamen Mohamad (ge20xogu/22810361), Sabrin Souilah (ag63uhiz/23174787), Tamer Tinkci (ir38oreq/22942217)

## *1 Introduction*
### Motivation
The ability to automatically detect and generate images of apples has numerous practical applications in agriculture and the food industry. For example, accurate apple detection can help automate sorting in fruit packing facilities[^1], while generating realistic images can aid in enhancing training datasets for machine learning models[^2]. Additionally, deploying this functionality in an interactive Streamlit app can provide an accessible tool for users to experiment with and apply these technologies.

[^1]: Hu, T., Wang, W., Gu, J., Xia, Z., Zhang, J., & Wang, B. (2023). [Research on Apple Object Detection and Localization Method Based on Improved YOLOX and RGB-D Images. Agronomy, 13(7), 1816.](https://www.mdpi.com/2073-4395/13/7/1816)    

[^2]: Gordon, R. (2023, November 20). [Synthetic imagery sets new bar in AI training efficiency. MIT News | Massachusetts Institute of Technology.](https://news.mit.edu/2023/synthetic-imagery-sets-new-bar-ai-training-efficiency-1120)

### Research question
How can a Generative Adversarial Network (GAN) be utilized to detect and generate realistic images of apples, and how can this be effectively deployed in a Streamlit application?


### Structure of this Document
This document is structered as follows:
1. [Introduction](#1-introduction)
2. [Related Work](#2-related-work)
3. [Methodology](#3-methodology)
    1. [General Methodology](#31-general-methodology)
    2. [Data Understanding](#32-data-understanding-and-preparation)
    3. [Modeling and Evaluation](#33-modeling-and-evaluation)
4. [Results](#4-results)
    1. [Artifacts](#artifacts)
    2. [Libraries and Tools](#libraries-and-tools)
    3. [App Concept](#app-concept)
    4. [Achieved Results](#achieved-results)
5. [Discussion](#5-discussion)
    1. [Limitations](#limitations)
    2. [Ethical Considerations](#ethical-considerations)
    3. [Further Research](#further-research)
6. [Conclusion](#6-conclusion)

## *2 Related Work*

### Existing Approaches
Research in the field of computer vision and machine learning has addressed tasks such as object detection and image generation. Some approaches have focused specifically on the fruit category.
As highlighted in the research by Pieters and Wiering, "Generative adversarial networks (GANs) have demonstrated to be successful at generating realistic real-world images" (Pieters, M., & Wiering, M. (2018, March 24) [Comparing Generative Adversarial Network Techniques for Image Creation and Modification](https://doi.org/10.48550/arXiv.1803.09093). ArXiv.org). An illustrative project in this regard is the synthetic fruit image generator by Bird et al. [^3], which focuses on generating lemon images using GAN technology.  

[^3]: [Synthetic Fruit Image Generator](https://github.com/jordan-bird/synthetic-fruit-image-generator).


### Relevance to our work
While many studies have explored GANs for fruit detection, this project specifically addresses the detection and generation of apple images using a custom GAN model. Our aim is to create a functional programm that can also be deployed as a Streamlit app, making these advanced machine learning capabiliteis accessible and practical for users.

## *3 Methodology*
### 3.1 General Methodology

To achieve the project goals, we followed these steps:
1. **Litarature Review:** Understanding existing GAN models and their applications in image detection and generation.
2. **Data Collection & Preparation:** Finding a dataset of apple images for commerical use and preprocessing it for model training.
3. **Model Development:** Building and training the GAN model.
4. **Evaluation:** Assessing model performance using appropriate metrics.
5. **App Development:** Implementing the model in a Streamlit app for user interaction.

### 3.2 Data Understanding and Preparation
#### Dataset Introduction  
The dataset consists of images containing fruits, vegetables and nuts and is sourced from Kaggle, which allows for commercial use. There are two different datasets available, and for our project, we have chosen the "fruit-360_dataset". However, for our project, we only use the apple subdirectories.

Link for the dataset:   https://www.kaggle.com/datasets/moltean/fruits

#### Structure and Size
*Note: Only the apple directories are taken into account here*
- Size: 8169 images
- Structure: The test and training directories each contain 13 folders with the different types of apples
- Format: jpg
- Image Sizes: 100 x 100 pixels
- Preprocessing: The fruits are already extracted from the background and the background is filled with white

#### Speciality
- Rotation: contains rotated fruit including fruit which was rotated around the 3rd axis

#### Data Preparation
- Data Cleaning: removing the irrelevant folders like nuts, vegetable and fruits except apples
- Normalization: Scaling pixel values to the range [-1,1] to facilitate model training

### 3.3 Modeling and Evaluation
#### Model Architecture
We utilized a Generative Adversarial Network (GAN) to model and generate apple images. The architecture of our GAN consists of two primary components: a generator and a discriminator.

- *Generator:*  

    The generator is designed to create fake data (here: apple images) form random noise. Its job is to produce data that looks as real as possible.

- *Discriminator:*  

    The discriminator acts as a binary classifier that distinguishes between real data and those generated by the generator.

#### Model Training
![Basic GAN Architecture](https://i0.wp.com/semiengineering.com/wp-content/uploads/nn3.png?fit=756%2C558&ssl=1)
*(Basic GAN Architecture. Source: [Bryong Moyer/ Semiconductor Engineering](https://semiengineering.com/knowledge_centers/artificial-intelligence/neural-networks/generative-adversarial-network-gan/))*

Training the GAN model involves an iterative process where both the generator and discriminator are trained alternately. The steps are as follows:

*Discriminator Training:*
1. Sample Real Images: Sample a batch of real apple images from the training dataset.
2. Generate Fake Images: Generate a batch of fake iamges using the current generator.
3. Train Discriminator: Train the discriminator to crrectly classify the real image as real and the fake images as fake. This is achieved by minimizing the discriminator loss, which measures how well the discriminator can disthinguish between real and fake images.

*Generator Training:*
1. Generate Fake Images: Generate a batch of fake images using the current generator.
2. Train Generator: Pass these fake images to the discriminator and update the generator's weights to maximize the likelihood that the discriminator classifies these fake images as real. This is achieved by minimizing the generator loss, which is calculated based on the discriminator's output.

This alernating training process continues until the generator produces sufficiently realistic apple images or until a predefined number of epochs is reached.

#### Model Evaluation
We primarily rely on the loss values and visual inspection to evaluate the performance of our GAN model:

- *Loss Values:*  
The generator and discriminator losses are crucial indicators of model performance. We aim for a balance where the generator loss decreases over time while the discriminator maintains a steady ability to distinguish between real and fake images.

- *Visual Inspection:*  
Subjective evaluation of the generated images' realism by human observers

## *4 Results*
### Artifacts:
- *Trained GAN Model:* 
    A trained GAN model capable of generating realistic apple images.
- *Streamlit App:* 
    An interactive app for generating apple images.


### Libraries and Tools
- **Python Libraries:**  
(For the specific version see: [requirements.txt](https://github.com/tamertinkci/ML4B-Team-7/blob/6c39151c31b06cd42060cd027c787e0f4d3e3b49/requirements.txt))

    - tensorflow
    - matplotlib.plyplot
    - pandas
    - numpy
    - ipython
    - toml
    - pillow
    - streamlit
    - streamlit_option_menu

- **Tools:**  
    - Anaconda
    - PyCharm
    - Visual Studio Code (VSC)
    - Github

### App Concept
The Streamlit app enables users to generate an apple and view their generated images in the History section during the session. Additionally, users have the option to switch the app between dark mode and light mode under Settings.

### Achieved Results
Descriptive Language (no judgement, no discussion in this section -> just show what you built)

By applying the trained GAN model on the dataset, we achieved the following results:
- Successfully generated realistic apple images.
- The discriminator effectively distinguished between real and fake images.
- The Streamlit app provided an intuitive interface for generating and viewing apple images.

## *5 Discussion*
### Limitations

- **Training Resources:**  
 Limited access to high-performance GPUs affected the training time and potentially the performance of the model.
- **Model Performance Variability:**  
Due to the inherent variability in GAN training, the performance and quality of generated images may vary between training runs. This variability can impact the consistency and reliability of the model outputs.


### Ethical Considerations

- **Dataset Bias:**  
The dataset used for training the GAN may inadvertently reflect biases present in the data collection process. For instance, if the dataset predominantly includes images of certain types of apples.
- **Impact on Jobs:**  
Automation in agricultural settings, facilitated by technologies like AI, may impact traditional labor practices. Ethical considerations include addressing potential job displacement and ensuring equitable distribution of benefits from technological advancements.


### Further Research
Looking ahead, there are numerous promising possibilities for extending this work:

- **Real-Time Apple Detection:**  
Integrate camera sensors with the Streamlit app to enable real-time apple detection and classification. Users can point their camera at an apple, and the app wil classify the apple type.

- **Specific Apple Type Generation:**   
Implement Conditional GANs to generate images of specific apple types based on user input. This could also be further developed by allowing users to input specific charactersitics such as color, size, and texture of the generated apple.

- **Batch Processing:**  
Implement batch processing capabilities in the app to allow users to upload multiple images and classify them in one go. This can streamline the workflow in commercial settings.

- **Cross-Domain Applications:**  
    - *Transfer Learning:*  
    Explore the use of transfer learning to apply the trained GAN model to other types of fruits or vegetables.
    - *Integration with IoT:*  
    Connect the app to Internet of Things (IoT) devices in agricultural settings to monitor and manage apple crops more effectively. Sensors can collect data on apple growth and quality, feeding this information into the app for real-time analysis.

## *6 Conclusion*
In this project, we successfully developed a GAN model to generate realistic apple images. The model was integrated into a Streamlit app, providing an accessible tool for generating apple images. 
Future work can expand on this foundation to include more fruit types and enhance the app's funcionality through real-time detection for example. But also through transfer learning and IoT integration.
