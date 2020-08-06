import led_animation_util as LedUtil
import asyncio
import threading
import time
import RPi.GPIO as GPIO
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

class AdaLedstrip:
    def __init__(self, pixel_count, spi_port, spi_device):
        self.onGoingTask = None
        self.cancelTask = False
        self.pixels = Adafruit_WS2801.WS2801Pixels(pixel_count, spi=SPI.SpiDev(spi_port, spi_device), gpio=GPIO)      
        print("Controlling ledstrip on spi port ", spi_port, "and on spi device ", spi_device)

    def pixel_rainbow_colors(self):
        self.__execute_task(LedUtil.rainbow_colors, (self.pixels, lambda: self.cancelTask, 0.005))

    def pixel_rainbow_cycle(self):
        self.__execute_task(LedUtil.rainbow_cycle, (self.pixels, lambda: self.cancelTask, 0.005))

    def pixel_rainbow_cycle_successive(self):
        self.__execute_task(LedUtil.rainbow_cycle_successive, (self.pixels, lambda: self.cancelTask, 0.1))

    def pixel_brightness_decrease(self):
        self.__execute_task(LedUtil.brightness_decrease, (self.pixels, lambda: self.cancelTask, 0.1, 1))

    def pixel_blink_color(self):
        self.__execute_task(LedUtil.blink_color, (self.pixels, lambda: self.cancelTask, 5, 0.1, (255, 127, 64)))

    def pixel_appear_from_back(self):
        self.__execute_task(LedUtil.appear_from_back, (self.pixels, lambda: self.cancelTask, (255, 127, 64)))

    def pixel_off(self):
        self.__cancel_task()
        self.pixels.clear()
        self.pixels.show()

    def __execute_task(self, task, args):
        self.pixel_off()
        self.onGoingTask = threading.Thread(target=task, args=args)
        self.onGoingTask.start()

    def __cancel_task(self):
        if (self.onGoingTask != None):
            self.cancelTask = True
            self.onGoingTask.join()
            self.cancelTask = False
            

        