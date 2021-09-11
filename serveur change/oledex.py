from machine import Pin, SoftI2C
import ssd1306


i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.fill(0)
oled.text('taux de change', 0, 0)
oled.show()




