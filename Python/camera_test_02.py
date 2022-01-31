import time # imports time libraries necessary for pauses 
import picamera # imports camera libraries 

print("Running") # displays constantly while camera is running 

with picamera.PiCamera() as camera: 
	camera.resolution = (1024, 768) # sets resolution 
	camera.image_effect = 'pastel' # sets effect (pastel)
	camera.start_preview() # starts preview screen 
	time.sleep(2) # pause 
	camera.capture('pastel_pic1.jpg') #takes saves and names picture
	print("picture 1: pastel") # prints that picture 1 has been taken

with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768) # sets resolution 
        camera.image_effect = 'cartoon' # sets effect (cartoon)
        camera.start_preview() # starts preview screen 
        time.sleep(2) # pause
        camera.capture('cartoon_pic2.jpg') # takes saves and names picture
        print("picture 2: cartoon") # prints that picture 2 has been taken

with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768) # sets resolution 
        camera.image_effect = 'negative' # sets effect (negative)
        camera.start_preview() # starts preview screen 
        time.sleep(2) # pause 
        camera.capture('negative_pic3.jpg') # takes saves and names picture
        print("picture 3: negative") # prints that picture 3 has been taken 

with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768) # sets resolution 
        camera.image_effect = 'oilpaint' # sets effect (oilpaint) 
        camera.start_preview() # starts preview screen 
        time.sleep(2) # pause 
        camera.capture('oilpaint_pic4.jpg') # takes saves and names picture 
        print("picture 4: oilpaint") # prints that picture 4 has been taken 

with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768) # sets resolution 
        camera.image_effect = 'sketch' # sets effect (sketch)
        camera.start_preview() # starts preview screen 
        time.sleep(2) # pause
        camera.capture('sketch_pic5.jpg') # takes saves and names picture
        print("picture 5: sketch") # prints that picture 5 has been taken

