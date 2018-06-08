import cv2
import numpy as np
def function1():
	recognizer = cv2.createLBPHFaceRecognizer()
	recognizer.load('trainner/trainner.yml')
	cascadePath = "haarcascade_frontalface_default.xml"
	faceCascade = cv2.CascadeClassifier(cascadePath);
	cam = cv2.VideoCapture(0)
	font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
	counter_out_loop = 0
	counter_in_loop = 0
	while counter_out_loop <= 100:
    		ret, im =cam.read()
    		gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    		faces=faceCascade.detectMultiScale(gray, 1.2,5)
		temp = "Unknown"
    		for(x,y,w,h) in faces:
        		cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
       		        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
			print conf,(Id)
			counter_in_loop += 1
			temp = "UNknown"
        		if Id == 580:
				temp = str(Id)+"_subhash"
				counter_in_loop += 1
			elif Id == 584:
				temp = "pravalika"
				counter_in_loop += 1
			elif Id == 598:
				temp = "rupshika"
				counter_in_loop += 1
			elif Id == 5:
				temp = "aravind"
				counter_in_loop += 1
			else:
				counter_out_loop += 1
        		cv2.cv.PutText(cv2.cv.fromarray(im),str(temp), (x,y+h),font, 255)
    			cv2.imshow('im',im) 
    		if cv2.waitKey(10) and 0xFF==ord('q'):
        		break
    		if counter_in_loop >= 30:
			break
        counter_out_loop += 1 
	cam.release()
	cv2.destroyAllWindows()
        return counter_in_loop,Id
value,Id = function1()

