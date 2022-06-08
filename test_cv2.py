#import requests
import base64
import numpy as np
import cv2
#import os


#x= requests.get("http://challenge01.root-me.org/programmation/ch8/")
#img=x.text.split("base64,")[1].split('" /><br><br><form action=""')[0]
#img=base64.b64decode(img)
#jpg_as_np = np.frombuffer(img, dtype=np.uint8)
#img = cv2.imdecode(jpg_as_np, flags=1)

img = cv2.imread('c:/Users/Eliott/Desktop/python/captchaOpener/captcha/3.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray = cv2.medianBlur(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),3)
#(thresh, bwimg) = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)
bwimg = gray

#cv2.imshow('thresh', thresh)
#bwimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bwimg = cv2.resize(bwimg,(3000,400))

kernel = np.ones((7,7), np.uint8)
kernel2 = np.ones((7,7), np.uint8)
bwimg = cv2.dilate(bwimg, kernel, iterations=1)
bwimg = cv2.medianBlur(bwimg,13)
cv2.imshow('image1', cv2.resize(bwimg,(900,350)))
cv2.waitKey(0)
bwimg= cv2.resize(bwimg,(250,50))
ret, thresh = cv2.threshold(bwimg, 0, 255, cv2.THRESH_OTSU)



ctrs, hier = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
sorted_ctrs = sorted(ctrs, key=(lambda ctr: cv2.boundingRect(ctr)[0]))

#print("Number of contours:" + str(len(ctrs)))
iname=1
letterlist=[]
poslist=[]
for i, ctr in enumerate(sorted_ctrs):
    x, y, w, h = cv2.boundingRect(ctr)
    roi = img[y:y + h, x:x + w]
    area = w*h
    if 70 < area < 500:
        #rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        dim =(28,28)
        resizedim = cv2.resize(roi,(28,28))
        cv2.imshow('l',resizedim)
        cv2.waitKey(0)
        #cv2.imwrite('lettres_tmp/'+list(tmpchars)[iname]+'.png',resizedim)
        letterlist.append(resizedim)
        poslist.append((x,y,w,h))
        iname+=1
        
### TOTRY
'''
for k in range(len(poslist)) :
    for pos in poslist :
        if (poslist[k][0]>pos[0]) and (poslist[k][0]<pos[0]+pos[2]) and (poslist[k][1]>pos[1]) and (poslist[k][1]<pos[1]+pos[3]) :
            #letterlist.del(k)
            break
            
iname=1           
for im in letterlist :
    if im is not None:
        cv2.imwrite('lettres_tmp/'+list(tmpchars)[iname]+'.png',resizedim)
        iname+=1
        


ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
#cv2.imshow('thresh', thresh)

ctrs, hier = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
sorted_ctrs = sorted(ctrs, key=(lambda ctr: cv2.boundingRect(ctr)[0]))
print("boucle?")
#print("Number of contours:" + str(len(ctrs)))
iname=1
''''''
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

'''
