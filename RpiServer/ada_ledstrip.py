import led_animation_util as LedUtil
import time
import RPi.GPIO as GPIO
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

class AdaLedstrip:
    def __init__(self, pixel_count, spi_port, spi_device):
        self.pixels = Adafruit_WS2801.WS2801Pixels(pixel_count, spi=SPI.SpiDev(spi_port, spi_device), gpio=GPIO)      
        print("Controlling ledstrip on spi port ", spi_port, "and on spi device ", spi_device)        
        
    def pixel_on(self):
        self.pixels.clear()
        self.pixels.show()

        LedUtil.rainbow_cycle(self.pixels, wait=0.0005)

    def pixel_off(self):
        self.pixels.clear()
        self.pixels.show()
        