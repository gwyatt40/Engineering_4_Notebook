import time
# import time libraries 
import Adafruit_GPIO.SPI as SPI #import GPIO 
import Adafruit_SSD1306 #import LCD library 

import Adafruit_LSM303 #import accelerometer library
# image libraries for LCD: 
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

font = ImageFont.load_default()
# reset pin: 
RST = 24

DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# display address set up and start: 
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST,i2c_address=0x3d)
disp.begin()

while True:
    # reads acceleration 
    accel, mag = lsm303.read()
    # sets acceleration values as variables
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    # writes acceleration values to LCD screen
    draw.text('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={$
          accel_x, accel_y, accel_z, mag_x, mag_y, mag_z), font=font, fill= 255)
    # pause before reading accelerometer values again 
    time.sleep(0.5) 

