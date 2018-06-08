import cv2
import os
import numpy as np
from PIL import Image

s = os.path.abspath(os.path.join('music', 'haarcascade_frontalface_default.xml'))
detector = cv2.CascadeClassifier(s)
recognizer = cv2.createLBPHFaceRecognizer()
def play_video(id):
    cam = cv2.VideoCapture(0)
    # Id = '14131A0580'
    Id = id
    folder = "webcam"
    ap = os.path.abspath(os.path.join('music', folder))
    if not os.path.exists(ap):
        os.makedirs(ap)
    sampleNum = 0
    while (True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY,0)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            sampleNum = sampleNum + 1
            b=folder+"/User." + str(Id) + '.' + str(sampleNum) + ".jpg"
            ap = os.path.abspath(os.path.join('music',b ))
            print ap
            cv2.imwrite(ap, gray[y:y + h, x:x + w])

        if sampleNum > 10:
            break
    cam.release()
    cv2.destroyAllWindows()

    webpath = os.path.abspath(os.path.join('music', folder))
    print id
    faces, Ids = getImagesAndLabels(webpath, Id)
    if Ids == []:
        print "it is empty"
    else:
        recognizer.train(faces, np.array(Ids))
        trainnerpath = os.path.abspath(os.path.join('/home/subhash/Desktop/openCV', 'trainner', "trainner.yml"))
        recognizer.save(trainnerpath)

def getImagesAndLabels(path, Id_1):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    #create empth face list
    faceSamples=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:

        pilImage=Image.open(imagePath).convert('L')

        imageNp=np.array(pilImage,'uint8')

        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        print Id,int(Id_1)
        faces=detector.detectMultiScale(imageNp)
        for (x,y,w,h) in faces:
            faceSamples.append(imageNp[y:y+h,x:x+w])
            Ids.append(Id)
    return faceSamples,Ids

