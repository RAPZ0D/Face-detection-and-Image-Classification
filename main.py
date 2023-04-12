import numpy as np 
import cv2 as cv #importing the libraries

face_cascade=cv.CascadeClassifier('frontal_face.xml')
#The number in the video capture represents your camera
cap=cv.VideoCapture(1) #You can change the number to 0,1 or 2 depending on the external camera attached

while(True):
    ret,frame=cap.read() #this captures the image frame by frame
    gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
    for (x,y,w,h) in faces:
        print(x,y,w,h) #this will print the co-ordinates of the face
        roi_color=frame[y:y+h, x:x+w] 
        color_img='colored_img.png' #we are saving the colored face image 
        cv.imwrite(color_img, roi_color)

        colour=(255,216,0) #BGR (Blue,Green,Red)
        thick=4 #thickness of the line
        width=x+w 
        height=y+h
        cv.rectangle(frame,(x,y),(width,height),color=colour,thickness=thick)
    
    cv.imshow('OpenCV Frontal Face',frame) # this function will display the image

    if cv.waitKey(20) & 0xFF == ord('q'): #Press Q to exit the video capture 
        break

cap.release()
cv.destroyAllWindows() 