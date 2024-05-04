import cv2
import  face_recognition
#import numpy as np  
import os
global user_encoding,user_image,failornot
def facerecon():
    x=[]
    
    failornot = False
    user_image_list=[]
    known_face_encoding=[]
    capture =  cv2.VideoCapture(0)
    for i in os.listdir("/home/blackcrypt/projects/imagebase"):
        if i.endswith(".jpg"):
            user_image_list.append(i)
    for j in user_image_list:        
        user_image =face_recognition.load_image_file("imagebase/"+str(j))
        user_encoding = face_recognition.face_encodings(user_image)[0]
        known_face_encoding.append(user_encoding)
    s=True
    while True:
            ret,frame = capture.read()
            small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
                #rgb_small_frame = small_frame[:,:,::-1]
                #face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(small_frame)
            if len(face_encodings)>0:
                for k in known_face_encoding:
                    matches = face_recognition.compare_faces(k,face_encodings)
                    if matches[0]:
                         failornot=True
            else:
                pass
                #print("No face Detected")
    print("ok done")
#facerecon()
    