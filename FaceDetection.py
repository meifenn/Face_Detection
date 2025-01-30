#load an image: imread
#scale an image: cv.resize
#crop an image: cv.getRectSubPix
#rotate an image: cv.getRotationMatrix2d,cv.warpAffine
#replace some part of an image: img1[0:300,0:300]=img2

#detect a human face
#located a human face

import cv2 as cv 
import argparse

parser=argparse.ArgumentParser(description='image')
parser.add_argument("-i",'--image',required=True,help="Path to the iamge to be scanned")
args=parser.parse_args()

img=cv.imread(args.image)
if img is None:
    raise ValueError("The Image is missing")

face_cascade= cv.CascadeClassifier('haarcascade_frontalface_default.xml')

bg= cv.imread('ID_card_bg.png')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces= face_cascade.detectMultiScale(gray,1.1,4)

if len(faces)>0:
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    largest_face = max(faces, key=lambda rect: rect[2] * rect[3])  
    x, y, w, h = largest_face
        # x, y, w, h = faces[0]  
        
    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cropped_face = img[y:y + h, x:x + w]
    face_width, face_height = 190, 190
    resized_face = cv.resize(cropped_face, (face_width, face_height))

    start_x, start_y = 145, 250 
    end_x, end_y = start_x + face_width, start_y + face_height

    bg[start_y:end_y, start_x:end_x]=resized_face
elif len(faces)==0:
    print("No face detected. Image rejected.")
    exit()

print(faces) 
cv.imshow('face',img)
cv.imshow("Cropped Face", cropped_face)
cv.imshow("Pokemon Trainer ID", bg)
cv.waitKey(0)
cv.destroyAllWindows()