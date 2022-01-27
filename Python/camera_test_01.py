import time

import picamera

print("Running")

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768)
	camera.start_preview()
	time.sleep(2)
	camera.capture('camera_test2.jpg')
	print ("photo")
