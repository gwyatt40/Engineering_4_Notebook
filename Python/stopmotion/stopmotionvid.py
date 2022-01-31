from picamera import PiCamera # imports camera libraries
from time import sleep # imports time libaries 
from gpiozero import Button # imports button libraries

button = Button(17) # sets button pin 17
camera = PiCamera() # sets camera 

camera.start_preview() # starts preview display 
frame = 1 # sets intial frame #
while True:
    try:
        button.wait_for_press()
        camera.capture('frame%03d.jpg' % frame) # takes photo and names image with frame number
        frame += 1 # increases frame number by one 
    except KeyboardInterrupt: # KeyboardInterrupt stops camera
        camera.stop_preview() # stops preview display 
        break
