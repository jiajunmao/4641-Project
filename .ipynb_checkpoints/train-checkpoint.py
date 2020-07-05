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
python3 train.py [PATH TO fruits-360]
"""

#### CONSTANTS ####
IMAGE_W = 224
IMAGE_H = 224
IMAGE_CHANNELS = 3
BATCH_SIZE = 32
EPOCHS = 6

if __name__ == "__main__":
    path = sys.argv[1]
    train_image_generator = keras.preprocessing.image.ImageDataGenerator(rescale=1./255) 
    test_image_generator = keras.preprocessing.image.ImageDataGenerator(rescale=1./255) 

    train_data_gen = train_image_generator.flow_from_directory(
        directory=path + "Training",
        target_size=(IMAGE_H, IMAGE_W),
        class_mode='binary',
        batch_size=BATCH_SIZE
        # save_to_dir="Train_data_gen",
        # save_format='jpg'
    )

    test_data_gen = test_image_generator.flow_from_directory(
        directory=path + "Test",
        target_size=(IMAGE_H, IMAGE_W),
        batch_size=BATCH_SIZE,
        class_mode='binary'
        # save_to_dir="Test_data_gen",
        # save_format='jpg'
    )
    
    print("Using model MobileNetV2")
    mobilenet_model = keras.applications.MobileNetV2()
    for i in range(len(mobilenet_model.layers) - 1):
        mobilenet_model.layers[i].trainable = False
    mobilenet_model.compile(loss='binary_crossentropy', metrics=['accuracy'])
    mobilenet_model.summary()

    mobilenet_model.fit(
        train_data_gen,
        # steps_per_epoch=2000,
        epochs=EPOCHS,
        validation_data=test_data_gen
        # validation_steps=800
    )

    mobilenet_model.save("temp/model1")