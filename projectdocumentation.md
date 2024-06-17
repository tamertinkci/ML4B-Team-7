# Apple Detection and Generation

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
1. Introduction
2. Related Work
3. Methodology
4. Results
5. Discussion
6. Conclusion

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
The dataset consists of images containing fruits, vegetables and nuts and is sourced from Kaggle, which allows for commercial use. There are two different datasets available, and for our project, we have chosen the "fruit-360_dataset." However, for our project, we only use the apple subdirectories.

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
- Augmentation: Applying transformations like scaling
- Normalization: Scaling pixel values to the range [-1,1] to facilitate model training
- Data Cleaning: removing the irrelevant folders like nuts, vegetable and fruits except apples


### 3.3 Modeling and Evaluation
Describe the model architecture(s) you selected

Describe how you train your models

Describe how you evaluate your models/ which metrics you use

## *4 Results*
Describe what artifacts you have build
### Artifact(s):



### Libraries and Tools
- Python Libraries:  
tensorflow, matplotlib.plyplot, pandas, numpy, ipython, toml, pillow, streamlit, streamlit_option_menu
(For the specific version see: [requirements.txt](https://github.com/tamertinkci/ML4B-Team-7/blob/6c39151c31b06cd42060cd027c787e0f4d3e3b49/requirements.txt))
- Tools:  
Anaconda, PyCharm, Visual Studio Code (VSC), Github

### App Concept
The Streamlit app enables users to generate an apple and view their generated images in the Gallery section during the session. Additionally, users have the option to switch the app between dark mode and light mode under Settings.

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


### Further Research
What could be next steps for other researchers (specific research questions)

## *6 Conclusion*
Short summary of your findings and outlook
