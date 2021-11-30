# Python Program - LED BLINK
# Georgia Wyatt
# 11/30/21

from gpiozero import LED
from time import sleep

led1 = LED(21)
led2 = LED(13)

while True:
    led1.on()
    led2.off()
    print("RED ON, green off")
    sleep(1)
    led1.off()
    led2.on()
    print("red off, GREEN ON")
    sleep(1)
