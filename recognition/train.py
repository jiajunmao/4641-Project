import os
import sys
import numpy as np
import tensorflow as tf
import keras
import matplotlib.pyplot as plt

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, Model
from keras.layers import Input, Dense, Dropout, GlobalAveragePooling2D
from keras import regularizers

"""
[USAGE]: python3 train.py <PATH to fruits-360>
"""

### CONSTANTS ###
TRAIN_IMAGES = 19116
VAL_IMAGES = 6582
BATCH_SIZE = 32
IMG_SHAPE = (224, 224)
EPOCHS = 2  # training epochs

base_dir = sys.argv[1]
train_dir = os.path.join(base_dir, 'train')
val_dir = os.path.join(base_dir, 'val')

print(">>> Base Directory", base_dir)
print(">>> Training Dir", train_dir)
print(">>> Validation Dir", val_dir)

classes = os.listdir(train_dir)
num_classes = len(classes)
classes = np.array(classes)

print("Training on " + str(num_classes) + "classes")
print(classes)

#Image augmentations using ImageDataGenerator
image_gen_train = ImageDataGenerator(
    rescale=1./255,
    rotation_range=45,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    zoom_range=0.5,
)

train_data_gen = image_gen_train.flow_from_directory(
    batch_size=BATCH_SIZE,
    directory=train_dir,
    shuffle=True,
    target_size=IMG_SHAPE,
    class_mode='categorical'
)

# We never augment validation data
image_gen_val = ImageDataGenerator(rescale=1./255)

val_data_gen = image_gen_val.flow_from_directory(
    batch_size=BATCH_SIZE,
    directory=val_dir,
    target_size=IMG_SHAPE,
    class_mode='categorical'
)

base_model = keras.applications.MobileNetV2(
    input_shape=(224, 224, 3), 
    include_top=False
)

base_model.input

# Freeze MobileNetV2 weights besides last layer
for layer in base_model.layers:
    layer.trainable = False

# Create custom layers to base model
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(512, activation='relu', activity_regularizer=regularizers.l2(0.01))(x)
x = Dropout(0.5)(x)
out = Dense(28, activation='softmax', activity_regularizer=regularizers.l2(0.01))(x)

# Integrate with base model to get complete model
complete_model = Model(base_model.input, out)
complete_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["accuracy"])  
complete_model.summary()

history = complete_model.fit(
    train_data_gen,
    epochs=EPOCHS,
    steps_per_epoch=int(np.floor(TRAIN_IMAGES / BATCH_SIZE)),
    validation_data=val_data_gen,
    validation_steps=int(np.floor(VAL_IMAGES / BATCH_SIZE))
)

# Save model 
complete_model.save("model6_tatch1.h5")

# Visualize training results
loss = history.history['loss']
val_loss = history.history['val_loss']
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

epochs = range(EPOCHS)

plt.figure(figsize=(8, 8))
plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs, acc, label='Training Accuracy')
plt.plot(epochs, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs, loss, label='Training Loss')
plt.plot(epochs, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()
