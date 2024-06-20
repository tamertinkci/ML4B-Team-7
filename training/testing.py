import tensorflow as tf
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


def evaluate_disc_model(model, dataset):
    true_labels = []
    predictions = []

    for images, labels in dataset:
        logits = model(images, training=False)
        preds = tf.round(tf.sigmoid(logits))

        true_labels.extend(labels.numpy())
        predictions.extend(preds.numpy())

    # TODO Check parameter 'average' again
    accuracy = accuracy_score(true_labels, predictions)
    precision = precision_score(true_labels, predictions, average='weighted', zero_division=1)
    recall = recall_score(true_labels, predictions, average='weighted')
    f1 = f1_score(true_labels, predictions, average='weighted')
    conf_matrix = confusion_matrix(true_labels, predictions)

    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1 Score: {f1}")
    print(f"Confusion Matrix:\n{conf_matrix}")
    # End of function


def evaluate_gen_model(model, dataset, noise):
    counter = 0

    for image in dataset:
        generated_images = model(noise, training=False)
        ssim_scores = tf.image.ssim(image[0], generated_images[0], max_val=2.0)
        mean_ssim = tf.reduce_mean(ssim_scores)

        if counter % 10 == 0 or counter == len(dataset) - 1:
            print(f"Mean SSIM: {mean_ssim}")

        counter += 1
    # End of function
