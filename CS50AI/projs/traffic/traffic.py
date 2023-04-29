import cv2
import numpy as np
import os
import sys
import tensorflow as tf

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])
    
    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """

    images = []
    labels = []
    
    for it in range(0, NUM_CATEGORIES):
        # Go to every mini folder in gtsrb
        pre_path = os.path.join(data_dir, str(it))

        # Goto every ppm files in above folder
        for ppm_file in os.listdir(pre_path):
            path = os.path.join(pre_path, ppm_file)

            # read ppm file by using cv2
            img = cv2.imread(path)

            img = np.array(img)

            # resized to (IMG_HEIGHT, IMG_WIDTH)
            resized_img = cv2.resize(img, (IMG_HEIGHT, IMG_WIDTH))

            resized_img = resized_img / 255.0

            # add current image to list of images
            images.append(resized_img)
            
            # add current label to list of labels
            labels.append(it)

    tf.keras.utils.to_categorical(labels, NUM_CATEGORIES, 'int')
    # return a tuple of images and labels
    return (np.array(images), np.array(labels))
            

def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """

    # choose model
    model_ = tf.keras.models.Sequential()

    # Add layers
    model_.add(tf.keras.layers.Conv2D(
        32, 
        (3, 3), 
        input_shape=(IMG_WIDTH, IMG_HEIGHT, 3), 
        activation="relu"
    ))

    model_.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2)))

    model_.add(tf.keras.layers.Conv2D(
        32,
        (10, 10),
        input_shape=(IMG_WIDTH, IMG_HEIGHT, 3),
        activation="relu"
    ))

    model_.add(tf.keras.layers.MaxPooling2D(pool_size=(4,4)))

    model_.add(tf.keras.layers.Flatten())

    model_.add(tf.keras.layers.Dense(256, activation="relu"))

    model_.add(tf.keras.layers.Dropout(0.5))

    model_.add(tf.keras.layers.Dense(256, activation="relu"))

    model_.add(tf.keras.layers.Dropout(0.4))

    # Add output layer
    model_.add(tf.keras.layers.Dense(NUM_CATEGORIES, activation="sigmoid"))

    # compile model
    model_.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    return model_


if __name__ == "__main__":
    main()
