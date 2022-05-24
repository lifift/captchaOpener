from tensorflow.keras import models, layers, utils, backend as K, datasets
from PIL import Image as I
from PIL import ImageOps
import matplotlib.pyplot as plt
import numpy as np
import os
#ATTENTION PAS DE L minuscule, 0 et 1
tmpchars="abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ23456789"
chars={}
k=1
for char in list(tmpchars):
    code = []
    for i in range (len(tmpchars)):
        if i+1 == k:
            code.append(1.0)
        else :
            code.append(0.0)
    k+=1
    chars[char]=np.asarray(code)

    

imageset = []
labelset = []
liste_images = os.listdir('lettres_label/')

for name in liste_images:
    with I.open('lettres_label/'+name,'r') as im:
        gray = 1-((np.asarray(ImageOps.grayscale(im)))/255.0)
        imageset.append(gray)
    labelset.append(chars[ name.split('.')[0].split( ' (')[0] ])

imageset=np.asarray(imageset).astype('float32')
labelset=np.asarray(labelset).astype('float32')


model = models.Sequential()
model.add(layers.Flatten(input_shape=(28,28)))
model.add(layers.Dense(564,activation='relu'))
model.add(layers.Dense(59,activation='softmax'))# output ?

model.compile(optimizer='adam', loss='categorical_crossentropy',metrics=['accuracy'])


model.fit(imageset,labelset, epochs=50) # training / epochs = nb train full data
"""
valLo, valAcc = model.evaluate(imageset,labelset)
print("accuracy : " + str(valAcc))
print("test loss : "+str(valLo))


"""
model.save('current_model')
