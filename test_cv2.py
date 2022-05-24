import requests
import base64
import numpy as np
import cv2
import os

for opop in range(30):
    x= requests.get("http://challenge01.root-me.org/programmation/ch8/")
    img=x.text.split("base64,")[1].split('" /><br><br><form action=""')[0]
    img=base64.b64decode(img)
    jpg_as_np = np.frombuffer(img, dtype=np.uint8)
    img = cv2.imdecode(jpg_as_np, flags=1)


    gray = cv2.medianBlur(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),3)
    #cv2.imshow('gray', gray)

    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    #cv2.imshow('thresh', thresh)

    ctrs, hier = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs = sorted(ctrs, key=(lambda ctr: cv2.boundingRect(ctr)[0]))
    print("boucle?")
    #print("Number of contours:" + str(len(ctrs)))
    iname=1
    liste = os.listdir('lettres/')
    for name in liste:
        if int(name.split('.')[0])>iname:
            iname = int(name.split('.')[0])

    for i, ctr in enumerate(sorted_ctrs):
        x, y, w, h = cv2.boundingRect(ctr)

        roi = img[y:y + h, x:x + w]

        area = w*h

        if 100 < area < 400:
            #rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            dim =(28,28)
            resizedim = cv2.resize(roi,dim)
            cv2.imwrite('lettres/'+str(iname)+'.png',resizedim)
            iname+=1


