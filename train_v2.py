import tensorflow as tf
import keras
import os
import sys
import matplotlib.pyplot as plt
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input,Dense, Conv2D, Flatten, Dropout, MaxPooling2D,GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras import regularizers
from tensorflow.keras.models import Model

"""Dependencies
- tensorflow v2.2
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
IMAGE_SHAPE = (IMAGE_H, IMAGE_W, IMAGE_CHANNELS)
BATCH_SIZE = 32
EPOCHS = 30

if __name__ == "__main__":
    path = sys.argv[1]
    train_image_generator = keras.preprocessing.image.ImageDataGenerator(rescale=1./255) 
    test_image_generator = keras.preprocessing.image.ImageDataGenerator(rescale=1./255) 

    train_data_gen = train_image_generator.flow_from_directory(
        directory=path + "Training",
        target_size=(IMAGE_H, IMAGE_W),
        class_mode='categorical',
        batch_size=BATCH_SIZE
    )

    test_data_gen = test_image_generator.flow_from_directory(
        directory=path + "Test",
        target_size=(IMAGE_H, IMAGE_W),
        batch_size=BATCH_SIZE,
        class_mode='categorical'
    )

    base_model = keras.applications.MobileNetV2(
        input_shape=IMAGE_SHAPE,
        include_top=False,
        weights='imagenet'
        )

    base_model.summary()
    print("input type: ", base_model.input)

    for layer in base_model.layers:
        layer.trainable = False

    # x = base_model.output
    # x = GlobalAveragePooling2D()(x)
    # x = Dense(256, activation='relu')(x)
    # x = Dropout(0.2)(x)
    # out = Dense(5, activation='softmax')(x)
    # complete_model = Model(base_model.input, out

    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(256, activation='relu')(x)
    x = Dropout(0.2)(x)
    out = Dense(5, activation='softmax')(x)

    complete_model = Model(base_model.input, out)
    complete_model.compile(
        optimizer='adam', 
        loss='categorical_crossentropy',
        metrics=["accuracy"]
        )  

    complete_model.summary()

    complete_model.fit(
        train_data_gen,
        epochs=EPOCHS,
        steps_per_epoch=np.floor(52428 / BATCH_SIZE),
        validation_data=test_data_gen,
        batch_size=BATCH_SIZE
        )
    
    sample_val_images, label = next(test_data_gen) 
    predicted_batch = complete_model.predict(sample_val_images)
    predicted_batch = tf.squeeze(predicted_batch).numpy()
    predicted_ids = np.argmax(predicted_batch, axis=-1)
    classes = np.array([i for i in range(42)])
    predicted_class_names = classes[predicted_ids]
    print(predicted_class_names)

    real_class=classes[np.argmax(label,axis=1)]

    print(real_class)