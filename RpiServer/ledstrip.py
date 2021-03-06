import led_animation_util as LedUtil
import utilities as Util
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
        wait, isFloat = Util.floatTryParse(args["wait"])
        loop_forever, isBool = Util.boolTryParse(args["loop_forever"])
        if (isFloat and isBool):
            self.__execute_task(LedUtil.rainbow_colors, (self.pixels, lambda: self.cancelTask, wait, loop_forever))

    def pixel_rainbow_cycle(self, args):
        loop_forever, isBool = Util.boolTryParse(args["loop_forever"])
        wait, isFloat = Util.floatTryParse(args["wait"])
        loop, isInt = Util.intTryParse(args["loop"])
        if (isBool and isFloat and isInt):
            self.__execute_task(LedUtil.rainbow_cycle, (self.pixels, lambda: self.cancelTask, wait, loop, loop_forever))

    def pixel_rainbow_cycle_successive(self, args):
        wait, isFloat = Util.floatTryParse(args["wait"])
        if (isFloat):
            self.__execute_task(LedUtil.rainbow_cycle_successive, (self.pixels, lambda: self.cancelTask, wait))

    def pixel_brightness_decrease(self, args):
        wait, isFloat = Util.floatTryParse(args["wait"])
        step, isInt = Util.intTryParse(args["step"])
        if (isFloat and isInt):
            self.__execute_task(LedUtil.brightness_decrease, (self.pixels, lambda: self.cancelTask, wait, step))

    def pixel_blink_color(self, args):
        color, isColor = Util.colorTryParse(args["color"])
        wait, isFloat = Util.floatTryParse(args["wait"])
        blink_time, isInt = Util.intTryParse(args["blink_time"])
        if (isColor and isFloat and isInt):
            self.__execute_task(LedUtil.blink_color, (self.pixels, lambda: self.cancelTask, blink_time, wait, color))

    def pixel_appear_from_back(self, args):
        color, isColor = Util.colorTryParse(args["color"])
        wait, isFloat = Util.floatTryParse(args["wait"])
        size, isInt = Util.intTryParse(args["size"])
        if (isColor and isFloat and isInt):
            self.__execute_task(LedUtil.appear_from_back, (self.pixels, lambda: self.cancelTask, color, wait, size))
        
    def pixel_color_wipe(self, args):
        color, isColor = Util.colorTryParse(args["color"])
        wait, isFloat = Util.floatTryParse(args["wait"])
        should_clear, isBool = Util.boolTryParse(args["should_clear"])
        if (isColor and isFloat and isBool):
            self.__execute_task(LedUtil.color_wipe, (self.pixels, lambda: self.cancelTask, wait, color, should_clear))  

    def pixel_color_wipe_cycle(self, args):
        color, isColor = Util.colorTryParse(args["color"])
        wait, isFloat = Util.floatTryParse(args["wait"])
        fade_step, isInt = Util.intTryParse(args["fade_step"])
        loop_forever, isBool = Util.boolTryParse(args["loop_forever"])
        if (isColor and isFloat and isInt and isBool):
            self.__execute_task(LedUtil.color_wipe_cycle, (self.pixels, lambda: self.cancelTask, wait, color, fade_step, loop_forever)) 

    def pixel_theater_chase(self, args):
        color, isColor = Util.colorTryParse(args["color"])
        wait, isFloat = Util.floatTryParse(args["wait"])
        is_rainbow, isBool = Util.boolTryParse(args["is_rainbow"])
        if (isColor and isFloat and isBool):
            self.__execute_task(LedUtil.theaterChase, (self.pixels, lambda: self.cancelTask, color, wait, is_rainbow))     

    def pixel_color_wipe_rainbow(self, args):
        wait, isFloat = Util.floatTryParse(args["wait"])
        fade_step, isInt = Util.intTryParse(args["fade_step"])
        color_step, isInt2 = Util.intTryParse(args["color_step"])
        if (isFloat and isInt and isInt2):
            self.__execute_task(LedUtil.color_wipe_rainbow, (self.pixels, lambda: self.cancelTask, wait, fade_step, color_step))            

    def pixel_breathing(self, args):
        color, isColor = Util.colorTryParse(args["color"])
        move_factor, isFloat = Util.floatTryParse(args["move_factor"])
        if (isFloat and isColor):
            self.__execute_task(LedUtil.breathing, (self.pixels, lambda: self.cancelTask, color, move_factor))

    def pixel_breathing_lerp(self, args):
        color_to, isColor1 = Util.colorTryParse(args["color_to"])
        color_from, isColor2 = Util.colorTryParse(args["color_from"])
        move_factor, isFloat = Util.floatTryParse(args["move_factor"])
        if (isColor1 and isColor2 and isFloat):
            self.__execute_task(LedUtil.breathing_lerp, (self.pixels, lambda: self.cancelTask, color_from, color_to, move_factor))  

    def pixel_breathing_rainbow(self, args):
            move_factor, isFloat = Util.floatTryParse(args["move_factor"])
            color_step, isInt = Util.intTryParse(args["color_step"])
            if (isInt and isFloat):
                self.__execute_task(LedUtil.breathing_rainbow, (self.pixels, lambda: self.cancelTask, color_step, move_factor))  

    def pixel_fireworks(self, args):
        size, isInt = Util.intTryParse(args["size"])
        color, isColor = Util.colorTryParse(args["color"])
        is_rainbow, isBool = Util.boolTryParse(args["is_rainbow"])
        number_of_fireworks, isInt1 = Util.intTryParse(args["number_of_fireworks"])
        chance_of_explosion, isInt2 = Util.intTryParse(args["chance_of_explosion"])
        fade_step, isInt3 = Util.intTryParse(args["fade_step"])
        firework_fade, isInt4 = Util.intTryParse(args["firework_fade"])
        if (isColor and isBool and isInt and isInt1 and isInt2 and isInt3 and isInt4):
            self.__execute_task(LedUtil.fireworks, (self.pixels, lambda: self.cancelTask, size, color, is_rainbow, number_of_fireworks, chance_of_explosion, fade_step, firework_fade))     

    def pixel_labyrinth(self, args):
        wait, isFloat = Util.floatTryParse(args["wait"])
        color, isColor = Util.colorTryParse(args["color"])
        contact_color, isColor2 = Util.colorTryParse(args["contact_color"])        
        count, isInt = Util.intTryParse(args["count"])
        turn_chance, isInt2 = Util.intTryParse(args["turn_chance"])
        if (isColor and isColor2 and isFloat and isInt and isInt2):
            self.__execute_task(LedUtil.labyrinth, (self.pixels, lambda: self.cancelTask, wait, count, turn_chance, color, contact_color))

    def pixel_color_pair(self, args):
        wait, isFloat = Util.floatTryParse(args["wait"])
        color1, isColor1 = Util.colorTryParse(args["color1"])
        color2, isColor2 = Util.colorTryParse(args["color2"])
        size1, isInt1 = Util.intTryParse(args["size1"])
        size2, isInt2 = Util.intTryParse(args["size2"])        
        with_animation, isBool = Util.boolTryParse(args["with_animation"]) 
        fade_step, isInt = Util.intTryParse(args["fade_step"])
        if (isColor1 and isColor2 and isFloat and isInt1 and isInt2 and isInt and isBool):
            self.__execute_task(LedUtil.color_pair, (self.pixels, lambda: self.cancelTask, wait, color1, color2, size1, size2, with_animation, fade_step))
            

    def set_brightness(self, args):
        brightness, isInt = Util.intTryParse(args["brightness"])
        if (isInt):
            self.brightness = brightness
            self.pixels.setBrightness(brightness)
            self.pixels.show()

    def set_settings(self, args):
        self.__cancel_task()        
        
        led_pixel_count, isInt = Util.intTryParse(args["led_pixel_count"])
        if (isInt):
            self.led_count = led_pixel_count
            self.led_type = args["led_type"]
            ledType = constants.LED_STRIP
            if (self.led_type == constants.LED_STRIP_SK6812):
                ledType = ws.SK6812W_STRIP
            elif (self.led_type == constants.LED_STRIP_WS2811):
                ledType = ws.WS2811_STRIP_RGB
            elif (self.led_type == constants.LED_STRIP_WS2812B):
                ledType = ws.WS2811_STRIP_RGB

            self.pixels = PixelStrip(self.led_count, constants.LED_PIN, constants.LED_FREQ_HZ, constants.LED_DMA, constants.LED_INVERT, self.brightness, constants.LED_CHANNEL, ledType)
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
            

        