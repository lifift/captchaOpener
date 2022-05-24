from tensorflow.keras import models, layers, utils, backend as K, datasets
from PIL import Image as I
from PIL import ImageOps
import matplotlib.pyplot as plt
import numpy as np
import os


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
    

model = models.load_model('current_model')

with I.open('index.png','r') as im:
    imG=1-((np.asarray(ImageOps.grayscale(im)))/255.0)
    res=model.predict(imG.reshape(1,28,28))
    mostP=(0,0)
    for x in range(len(res[0])):
        if res[0][x]>mostP[1]:
            mostP=(x,res[0][x])
    print("le plus probable est le charactère : "+ list(tmpchars)[mostP[0]])
    print("La proba est : "+str(mostP[1]))
    plt.imshow(imG,cmap='gray')
    plt.show()

liste_images = os.listdir('lettres/')
for name in liste_images:
    with I.open('lettres/'+name,'r') as im:
        imG=1-((np.asarray(ImageOps.grayscale(im)))/255.0)
        res=model.predict(imG.reshape(1,28,28))
        mostP=(0,0)
        for x in range(len(res[0])):
            if res[0][x]>mostP[1]:
                mostP=(x,res[0][x])
        print("le plus probable est le charactère : "+ list(tmpchars)[mostP[0]])
        print("La proba est : "+str(mostP[1]))
        plt.imshow(imG,cmap='gray')
        plt.show()
