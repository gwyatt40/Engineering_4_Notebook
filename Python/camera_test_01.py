import time #imports time libraries necessary for pauses

import picamera #imports camera libraries 

print("Running") #constantly displayed while camera running 

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768) #set resolution 
	camera.start_preview() #start preview screen 
	time.sleep(2) # pause
	camera.capture('camera_test2.jpg') # captures saves and names photo 
	print ("photo") #'photo' displays when photo has been taken 
