import led_animation_util as LedUtil
import threading
import time
from rpi_ws281x import Color, PixelStrip, ws
import pprint
import constants
from PIL import ImageColor

class Ledstrip:
    def __init__(self):
        self.onGoingTask = None
        self.cancelTask = False
        self.brightness = constants.LED_BRIGHTNESS
        self.pixels = PixelStrip(constants.LED_COUNT, constants.LED_PIN, constants.LED_FREQ_HZ, constants.LED_DMA, constants.LED_INVERT, constants.LED_BRIGHTNESS, constants.LED_CHANNEL, constants.LED_STRIP)
        self.pixels.begin()
        LedUtil.clear(self.pixels)
        self.pixels.setPixelColor(0, Color(255, 255, 255, 255))
        self.pixels.show()
        
        print("Controlling ledstrip on pin ", constants.LED_PIN)

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
        
    def pixel_color_wipe(self, args):
        self.__execute_task(LedUtil.color_wipe, (self.pixels, lambda: self.cancelTask, float(args["wait"]), ImageColor.getcolor(args["color"], "RGB")))        

    def set_settings(self, args):
        self.__cancel_task()
        self.led_type = args["led_type"]
        self.led_count = int(args["led_pixel_count"])
        if (args["led_type"] == constants.LED_STRIP_SK6812):
            self.pixels = PixelStrip(self.led_count, constants.LED_PIN, constants.LED_FREQ_HZ, constants.LED_DMA, constants.LED_INVERT, self.brightness, constants.LED_CHANNEL, constants.LED_STRIP)
            self.pixels.begin()

    def pixel_off(self, args):
        self.__cancel_task()
        LedUtil.clear(self.pixels)
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
            

        