import cv2
cam=cv2.VideoCapture(0)
alg="hs.xml"
hash=cv2.CascadeClassifier(alg)
while True:
    _,img=cam.read()
    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=hash.detectMultiScale(grey,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),3)
        text="face detected"
        cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2)
        cv2.imshow("hi",img)
        key=cv2.waitKey(10)
        if key==ord("q"):
            break
cam.release()
cv2.destroyAllWindows()    
