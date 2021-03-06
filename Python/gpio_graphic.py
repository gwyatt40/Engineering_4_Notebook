
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


lsm303 = Adafruit_LSM303.LSM303()


RST = 24

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)


disp.begin()


disp.clear()
disp.display()



width = disp.width
height = disp.height
image = Image.new('1', (width, height))


draw = ImageDraw.Draw(image)


draw.rectangle((0,0,width,height), outline=0, fill=0)


padding = 2
top = padding
bottom = height-padding
x = 1


font = ImageFont.load_default()

while True:

    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag



    draw.rectangle((0,0,width,height), outline=0, fill=0)

    draw.text((x, top),'Accel X={0}, Y={1}, Z={2}'.format(accel_x, accel_y, accel_z), font=font, fill=255)

    draw.text((x, top+10),'Mag X={0}, Y={1}, Z={2}'.format(mag_x, mag_y, mag_z), font=font, fill=255)

    disp.image(image)

    disp.display()
    time.sleep(0.5)
    disp.clear()
