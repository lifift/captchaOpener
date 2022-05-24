from tensorflow.keras import models, layers, utils, backend as K, datasets
from PIL import Image as I
import PIL
import matplotlib.pyplot as plt
import numpy as np

#Init
((trainIm,trainLab),(testIm,testLab)) = datasets.mnist.load_data()
trainIm = trainIm/255.0
testIm = testIm/255.0

print(trainIm[0])

#first display

"""
#simpli NNr

model = models.Sequential()
model.add(layers.Flatten(input_shape=(28,28)))
model.add(layers.Dense(128,activation='relu'))
model.add(layers.Dense(10,activation='softmax'))# output ?

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])


model.fit(trainIm,trainLab, epochs=3) # training / epochs = nb train full data

valLo, valAcc = model.evaluate(testIm,testLab)
print("accuracy : " + str(valAcc))
print("test loss : "+str(valLo))

#saving models

model.save('first_model')

# load model
"""
model = models.load_model('first_model')

plt.imshow(trainIm[0],cmap='gray')
plt.show()
res=model.predict(trainIm[0].reshape(1,28,28))
print(res)
with I.open('im.png','r') as im:
    imG=(np.asarray(PIL.ImageOps.grayscale(im)))/255.0
    res=model.predict(imG.reshape(1,28,28))
    print(res)
    plt.imshow(imG,cmap='gray')
    plt.show()
