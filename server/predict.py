import os
import sys
import numpy as np
import keras

import tensorflow as tf
import matplotlib
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input,Dense, Conv2D, Flatten, Dropout, MaxPooling2D,GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras import regularizers
from tensorflow.keras.models import Model

from keras.preprocessing.image import load_img, img_to_array
from scipy.special import softmax

from PIL import Image

IMG_SIZE = (224, 224)
IMG_SHAPE = 224

if __name__ == "__main__":
    # base_dir = sys.argv[1]
    # val_dir = os.path.join(base_dir, 'val')
    # train_dir = os.path.join(base_dir, 'train')

    classes = np.load("classes.npy")
    classes.sort()
    #print(classes)
    
    # model = keras.applications.VGG16()
    # model.load_weights("../Downloads/vgg16.h5")

    model = keras.models.load_model("model4_dropout.h5")
    #model.summary()

    # model.summary()
    # img = load_img("4_100_6.jpg", target_size=IMG_SIZE)
    # img = np.reshape(np.asarray(img), (1, 224, 224, 3))
    # result = model.predict(img)
    # print(classes)
    # print(result)

    # result_index = np.argmax(result, axis=1)
    # print(result_index)
    # print(classes[result_index[0]])

    image_gen_val = ImageDataGenerator(rescale=1./255)
    val_data_gen = image_gen_val.flow_from_directory(
        batch_size=1,
        directory="test_images",
        target_size=(224, 224),
        class_mode='categorical'
    )

    # for i in range(5):
    #     sample_val_images, label = next(val_data_gen) 
    #     np.save("test_" + str(i + 10), sample_val_images[5])

    # raise Exception
    # input_image = load_img("test.jpg", target_size=(224, 224))
    # one_img = np.array(input_image)

    sample_val_images, label = next(val_data_gen)
    one_img = sample_val_images
    #print(one_img.shape)

    # one_class = label[5]
    # print(one_img.shape)
    # np.save("test.npy", one_img)

    # one_img = np.load("test.npy")

    #plt.imshow(one_img[0])
    #plt.show()

    # plt.imshow(one_img)
    # plt.show()

    # matplotlib.image.imsave("test.bmp", one_img)
    # two_img = load_img("22_100_20.jpg", target_size=IMG_SIZE)
    # two_img = np.array(two_img)
    # two_img = two_img[:, :, ::-1]


    # print(two_img)

    # print(two_img.shape)
    # plt.imshow(two_img)
    # plt.show()

    # compare = one_img == two_img
    # print(compare.all())
    # print(np.sum(one_img - two_img))

    # one_img = np.ones((224, 224, 3)) * 255
    # two_img = np.expand_dims(two_img, axis=0)
    # one_img = np.expand_dims(one_img, axis=0)

    # plt.imshow(one_img[0])
    # plt.show()

    predicted_batch = model.predict(one_img, batch_size=1)
    predicted_batch = tf.squeeze(predicted_batch).numpy()

    # predicted_batch.sort()
    # print("TOP 5: ", predicted_batch[:5], classes[predicted_batch[:5]])

    # print(np.sum(predicted_batch))

    predicted_ids = np.argmax(predicted_batch, axis=-1)
    #print(predicted_batch.shape, predicted_ids.shape, predicted_ids)
    print(classes[predicted_ids], flush=True)

    # print("expected: ", classes[np.argmax(one_class)])
    # raise Exception

    # predicted_batch = model.predict(sample_val_images)
    # predicted_batch = tf.squeeze(predicted_batch).numpy()
    # predicted_ids = np.argmax(predicted_batch, axis=-1)

    # classes = np.array(classes)
    # np.save("classes.npy", classes)

    # predicted_class_names = classes[predicted_ids]
    # print(predicted_class_names)

    # real_class=classes[np.argmax(label,axis=1)]
    # print(real_class)

    # print("prediction")

    # plt.figure(figsize=(10,9))
    # for n in range(30):
    #     plt.subplot(6,5,n+1)
    #     plt.subplots_adjust(hspace = 0.3)
    #     plt.imshow(sample_val_images[n])
    #     plt.title(predicted_class_names[n].title())
    # plt.show()