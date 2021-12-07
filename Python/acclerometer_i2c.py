import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

font = ImageFont.load_default()

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0


# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST,i2c_address=0x3d)
disp.begin()

while True:
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    draw.text('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={$
          accel_x, accel_y, accel_z, mag_x, mag_y, mag_z), font=font, fill= 255)
    
    time.sleep(0.5) 

