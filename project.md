# Apple Detection and Generation

Stephen Nkwelle (StudOn-Username/Enrollment Number), Yamen Mohamad (StudOn-Username/Enrollment Number), Sabrin Souilah (ag63uhiz/23174787), Tamer Tinkci (ir38oreq)

## *1 Introduction*
### Motivation
The ability to automatically detect and generate images of apples has numerous practical applications in agriculture and the food industry. For example, accurate apple detection can help automate sorting in fruit packing facilities, while generating realistic images can aid in enhancing training datasets for machine learning models. Additionally, deploying this functionality in an interactive Streamlit app can provide an accessible tool for users to experiment with and apply these technologies.

### Research question
How can a Generative Adversarial Network (GAN) be utilized to detect and generate realistic images of apples, and how can this be effectively deployed in a Streamlit application?


### Structure of this Document
This document is structered as follows:
1. Introduction
2. Related Work
3. Methodology
4. Results
5. Discussion
6. Conclusion

## *2 Related Work*

### Existing Approaches
What have others done in your area of work/ to answer similar questions?

Research in the field of computer vision and machine learning has addressed tasks such as object detection and image generation. Some approaches have focused specifically on the fruit category.
Studies have shown that GANs can be effectively used for generating high-quality fruit images, enhancing datasets for training, and improving detection accuracy.


### Relevance to our work
Discussing existing work in the context of your work

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
The dataset consists of 850 apple images sourced from Kaggle, which allows for commercial use.
Link for the dataset:   https://www.kaggle.com/datasets/jayaprakashpondy/apple-fruit  

#### Structure and Size
- Size: 850 images
- Format: jpg and jpeg
- Structure: Divided into train and test folders, each with four subdirectories:
    - Blotch
    - Normal
    - Rot
    - Scab
- Image Sizes: Various dimensions

#### Specialities
- Diversity: Includes various apple types and conditions such as blotch, normal, rot, and scab

#### Data Preparation
- Augmentation: Applying transformations like scaling
- Normalization: Scaling pixel values to the range [-1,1] to facilitate model training


### 3.3 Modeling and Evaluation (Stephen)

Describe the model architecture(s) you selected

Describe how you train your models

Describe how you evaluate your models/ which metrics you use

## *4 Results*
Describe what artifacts you have build
### Artifact(s):
- Trained GAN Model:  
Capable of generating realistic apple images.


### Libraries and Tools
- Python Libraries:  
os.path, tensorflow, matplotlib.plyplot

- Tools:  
Anaconda, PyCharm, Visual Studio Code (VSC), Github

### App Concept
The streamlit app allows users to ...

### Achieved Results
Describe the results you achieve by applying your trained models on unseen data

Descriptive Language (no judgement, no discussion in this section -> just show what you built)

## *5 Discussion*
Now its time to discuss your results/ artifacts/ app 

### Limitations
Show the limitations : e.g. missing data, limited training ressources/ GPU availability in Colab, limitaitons of the app

### Ethical Considerations
Discuss your work from an ethics perspective:

Dangers of the application of your work (for example discrimination through ML models)

Transparency 



### Further Research
What could be next steps for other researchers (specific research questions)

## *6 Conclusion*
Short summary of your findings and outlook
