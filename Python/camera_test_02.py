import time
import picamera

print("running")

with picamera.PiCamera() as camera: 
	camera.resolution = (1024, 768)
	camera.image_effect = 'pastel' 
	camera.start_preview()
	time.sleep(2)
	camera.capture('pastel_pic1.jpg')
	print("picture 1: pastel")

with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.image_effect = 'cartoon'
        camera.start_preview()
        time.sleep(2)
        camera.capture('cartoon_pic2.jpg')
        print("picture 2: cartoon")

with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.image_effect = 'negative'
        camera.start_preview()
        time.sleep(2)
        camera.capture('negative_pic3.jpg')
        print("picture 3: negative")

with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.image_effect = 'oilpaint'
        camera.start_preview()
        time.sleep(2)
        camera.capture('oilpaint_pic4.jpg')
        print("picture 4: oilpaint")

with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.image_effect = 'sketch'
        camera.start_preview()
        time.sleep(2)
        camera.capture('sketch_pic5.jpg')
        print("picture 5: sketch")

