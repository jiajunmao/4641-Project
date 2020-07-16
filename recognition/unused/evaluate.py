import tensorflow as tf
import keras
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import cv2
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array


def predict(path):
    try:
        image = load_img(path, target_size=(224, 224))
    except FileNotFoundError:
        print("wrong file name")
        return
    
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    print("image shape: ", image.shape)

    model = keras.models.load_model("temp/model1")
    model.summary()
    model.predict(image)

    yhat = model.predict(image)
    # label = model.decode_predictions(yhat, top=1000)
    # label = label[0][0]

    # print("Model: %s (%.2f%%)" % (label[1], label[2] * 100))
    print(yhat, len(yhat[0]))

if __name__ == "__main__":
    while True:
        path = input("path:")
        predict(path)

