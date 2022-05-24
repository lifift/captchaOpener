import requests
import base64
import numpy as np
import cv2

x= requests.get("http://challenge01.root-me.org/programmation/ch8/")

img=x.text.split("base64,")[1].split('" /><br><br><form action=""')[0]
img=base64.b64decode(img)
jpg_as_np = np.frombuffer(img, dtype=np.uint8)
img = cv2.imdecode(jpg_as_np, flags=1)
cv2.imshow('img',img)
