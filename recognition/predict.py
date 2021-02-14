import numpy as np
import keras
import tensorflow as tf
import matplotlib.pyplot as plt

from keras.preprocessing.image import ImageDataGenerator

"""
[USAGE]: python3 predict.py
This one used model4_dropout.h5.
This is the overall best version.
"""

### CONSTANTS ###
IMG_SIZE = (224, 224)  # MobileNetV2 Input Size

if __name__ == "__main__":

    classes = np.load("classes.npy")  # loading classes list
    classes.sort()
    # print(classes)

    model = keras.models.load_model("model4_dropout.h5")
    # model.summary()

    image_gen_val = ImageDataGenerator(rescale=1./255)
    # [BUG] We cannot directly load local jpg files to predict, the pixel colors will be
    # distorted that way. Therefore we use ImageDataGenerator, like we do in the training

    val_data_gen = image_gen_val.flow_from_directory(
        batch_size=1,  # since we are predicting one at a time
        directory="test_images",
        target_size=IMG_SIZE,
        class_mode='categorical'
    )

    # let ImageDataGenerator generate the image for predition
    img, label = next(val_data_gen)  # label is just a placeholder
    
    plt.imshow(img[0])
    plt.show()

    results = model.predict(img, batch_size=1)
    results = tf.squeeze(results).numpy()

    index = np.argmax(results, axis=-1)
    # print(results.shape, index.shape, index)
    print("predicted: ", classes[index])
