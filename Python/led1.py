# Python Program - LED BLINK
# Georgia Wyatt
# 11/30/21

# import LED and time libraries
from gpiozero import LED
from time import sleep

# assign pins
led1 = LED(21)
led2 = LED(13)

while True: # loops constantly until ctrl+C
    led1.on() # red on
    led2.off() # green off 
    print("RED ON, green off") # prints to screen
    sleep(1) # 1 second pause
    led1.off() # red off 
    led2.on() # green on 
    print("red off, GREEN ON") # prints to screen
    sleep(1) # 1 second pause
