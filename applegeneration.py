# Import and Preprocessing

import os
import cv2
import numpy as np

def load_dataset(directory):
    # Initialize empty lists to store images and labels
    images = []
    labels = []

     # Iterate over subdirectories for different categories of apple images
    for label, label_name in enumerate(["Normal_Apple", "Rot_Apple", "Scab_Apple", "Blotch_Apple"]):
        # Get the directory path for the current category
        label_directory = os.path.join(directory, label_name)
        
        # Iterate over image files in the current category directory
        for filename in os.listdir(label_directory):
            # Check if the file is an image file (ending with .jpg or .png)
            if filename.endswith('.jpg') or filename.endswith('.png'):
                # Construct the full path to the image file
                image_path = os.path.join(label_directory, filename)
                
                # Read the image using OpenCV
                image = cv2.imread(image_path)
                
                # Resize the image to a fixed size
                image = cv2.resize(image, (128, 128))
                
                # Append the resized image to the images list
                images.append(image)
                
                # Append the label (category) for the image to the labels list
                labels.append(label)

    # Convert the lists to numpy arrays for easier manipulation
    return np.array(images), np.array(labels)
)

# Load the training dataset directory
train_dir = r"C:\Users\sabri\OneDrive\Uni\ML4B\Apple-Fruit\Train"
train_images, train_labels = load_dataset(train_dir)

# Load the test dataset directory
test_dir = r"C:\Users\sabri\OneDrive\Uni\ML4B\Apple-Fruit\Test"
test_images, test_labels = load_dataset(test_dir)


