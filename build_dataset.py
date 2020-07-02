import tensorflow as tf
import keras
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import cv2

"""Dependencies
- tensorflow v2.2
- opencv-python v4.2
- matplotlib
- numpy
- keras

--- Usage
python3 build_dataset.py <PATH TO fruits-360/Training>
"""

#### CONSTANTS ####
IMAGE_W = 224
IMAGE_H = 224
IMAGE_CHANNELS = 3


def build(path):
    """[summary]
    Make sure you have Training as a subfolder of fruits-360
    Args:
        path ([str]): Path to fruits-360/Training 
    """    
    print("Root: " + path)
    training_labels = []
    training_samples = []
    for root, subdirs, files in os.walk(path):    
        # print("folder ", root)
        current_class = root[root.rfind("fruits-360/Training/") + 19:]
        # print(root)
        # print(files)
        for current_file in files:
            print("reading " + root + "/" + current_file)
            img = cv2.imread(root + "/" + current_file)
            if img.shape != (IMAGE_H, IMAGE_W, IMAGE_CHANNELS):
                img = cv2.resize(img, (IMAGE_H, IMAGE_W), interpolation=cv2.INTER_CUBIC)

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = np.reshape(img, (1, IMAGE_H, IMAGE_W, IMAGE_CHANNELS))
            
            training_samples.append(img)
            training_labels.append(current_class)

    training_labels = np.array(training_labels)
    training_samples = np.array(training_samples)
    print((training_labels))
    print(training_labels.shape)
    print((training_samples.shape))

    print("saving...")
    np.save("training_samples.npy", training_samples)
    np.save("training_labels.npy", training_labels)


if __name__ == "__main__":
    path = sys.argv[1]
    try:
        training_labels = np.load("training_labels.npy")
        training_samples = np.load("training_samples.npy")
    except FileNotFoundError:
        print("Building dataset from file")
        build(path)
        training_labels = np.load("training_labels.npy")
        training_samples = np.load("training_samples.npy")

    print("loaded training_labels: ", training_labels.shape)
    print("loaded training_samples: ", training_samples.shape)

    training_samples = tf.convert_to_tensor(training_samples)
    training_labels = tf.convert_to_tensor(training_labels)
    training_dataset = tf.data.Dataset.from_tensor_slices((training_samples, training_labels))

    print("Using model MobileNetV2")
    mobilenet_model = keras.applications.MobileNetV2()
    for i in range(len(mobilenet_model.layers) - 1):
        mobilenet_model.layers[i].trainable = False
    mobilenet_model.summary()

    mobilenet_model.compile(loss='binary_crossentropy', metrics=['accuracy'])
    mobilenet_model.fit(training_dataset, epochs=30, batch_size=16)
    



    # Test matching label and picture
    # plt.imshow(training_samples[55555])
    # plt.title(training_labels[55555])
    # plt.show()
    

