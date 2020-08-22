import led_animation_util as LedUtil
import asyncio
import threading
import time
import RPi.GPIO as GPIO
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI
import pprint
import constants
from PIL import ImageColor

class AdaLedstrip:
    def __init__(self, pixel_count, spi_port, spi_device):
        self.onGoingTask = None
        self.cancelTask = False
        self.pixels = Adafruit_WS2801.WS2801Pixels(pixel_count, spi=SPI.SpiDev(spi_port, spi_device), gpio=GPIO)
        print("Controlling ledstrip on spi port ", spi_port, "and on spi device ", spi_device)

    def pixel_rainbow_colors(self, args):
        self.__execute_task(LedUtil.rainbow_colors, (self.pixels, lambda: self.cancelTask, float(args["wait"])))

    def pixel_rainbow_cycle(self, args):
        self.__execute_task(LedUtil.rainbow_cycle, (self.pixels, lambda: self.cancelTask, float(args["wait"])))

    def pixel_rainbow_cycle_successive(self, args):
        self.__execute_task(LedUtil.rainbow_cycle_successive, (self.pixels, lambda: self.cancelTask, float(args["wait"])))

    def pixel_brightness_decrease(self, args):
        self.__execute_task(LedUtil.brightness_decrease, (self.pixels, lambda: self.cancelTask, float(args["wait"]), int(args["step"])))

    def pixel_blink_color(self, args):
        self.__execute_task(LedUtil.blink_color, (self.pixels, lambda: self.cancelTask, int(args["blink_time"]), float(args["wait"]), ImageColor.getcolor(args["color"], "RGB")))

    def pixel_appear_from_back(self, args):
        self.__execute_task(LedUtil.appear_from_back, (self.pixels, lambda: self.cancelTask, ImageColor.getcolor(args["color"], "RGB")))

    def set_settings(self, args):
        self.__cancel_task()
        self.led_type = args["led_type"]
        self.led_count = int(args["led_pixel_count"])
        if (args["led_type"] == constants.TYPE_WS2812B):
            self.pixels = Adafruit_WS2801.WS2801Pixels(int(args["led_pixel_count"]), spi=SPI.SpiDev(constants.SPI_PORT, constants.SPI_DEVICE), gpio=GPIO)

    def pixel_off(self, args):
        self.__cancel_task()
        self.pixels.clear()
        self.pixels.show()

    def __execute_task(self, task, args):
        self.__cancel_task()
        self.onGoingTask = threading.Thread(target=task, args=args)
        self.onGoingTask.start()

    def __cancel_task(self):
        if (self.onGoingTask != None):
            self.cancelTask = True
            self.onGoingTask.join()
            self.cancelTask = False
            

        