# Simple demo of of the WS2801/SPI-like addressable RGB LED lights.
import time
import asyncio
# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI 
 
# Define the wheel function to interpolate between different hues.
def wheel(pos):
    if pos < 85:
        return Adafruit_WS2801.RGB_to_color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Adafruit_WS2801.RGB_to_color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Adafruit_WS2801.RGB_to_color(0, pos * 3, 255 - pos * 3)
 
# Define rainbow cycle function to do a cycle of all hues.
def rainbow_cycle_successive(pixels, isCancelled, wait=0.1):
    pixels.clear()
    pixels.show()
    for i in range(pixels.count()):
        # tricky math! we use each pixel as a fraction of the full 96-color wheel
        # (thats the i / strip.numPixels() part)
        # Then add in j which makes the colors go around per pixel
        # the % 96 is to make the wheel cycle around
        pixels.set_pixel(i, wheel(((i * 256 // pixels.count())) % 256) )
        if (isCancelled()):
            break
        pixels.show()
        if wait > 0:
            time.sleep(wait)
        if (isCancelled()):
            break
 
def rainbow_cycle(pixels, isCancelled, wait=0.005):
    pixels.clear()
    pixels.show()
    for j in range(256): # one cycle of all 256 colors in the wheel
        for i in range(pixels.count()):
            pixels.set_pixel(i, wheel(((i * 256 // pixels.count()) + j) % 256) )
        if (isCancelled()):
            break
        pixels.show()
        if wait > 0:
            time.sleep(wait)
        if (isCancelled()):
            break
 
def rainbow_colors(pixels, isCancelled, wait=0.05):
    pixels.clear()
    pixels.show()
    for j in range(256): # one cycle of all 256 colors in the wheel
        for i in range(pixels.count()):
            pixels.set_pixel(i, wheel(((256 // pixels.count() + j)) % 256) )
        if (isCancelled()):
            break
        pixels.show()
        if wait > 0:
            time.sleep(wait)
        if (isCancelled()):
                break
 
def brightness_decrease(pixels, isCancelled, wait=0.01, step=1):
    for j in range(int(256 // step)):
        for i in range(pixels.count()):
            r, g, b = pixels.get_pixel_rgb(i)
            r = int(max(0, r - step))
            g = int(max(0, g - step))
            b = int(max(0, b - step))
            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( r, g, b ))
        if (isCancelled()):
            break
        pixels.show()
        if wait > 0:
            time.sleep(wait)
        if (isCancelled()):
            break
 
def blink_color(pixels, isCancelled, blink_time=5, wait=0.5, color=(255,0,0)):
    pixels.clear()
    pixels.show()
    for i in range(blink_time):
        # blink two times, then wit
        pixels.clear()
        for j in range(2):
            for k in range(pixels.count()):
                # LedStrip is bgr and not rgb  
                pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[2], color[1], color[0] ))
            if (isCancelled()):
                break
            pixels.show()
            time.sleep(0.08)
            pixels.clear()
            pixels.show()
            if (isCancelled()):
                break
            time.sleep(0.08)
            if (isCancelled()):
                break
        time.sleep(wait)
        if (isCancelled()):
            break
 
def appear_from_back(pixels, isCancelled, color=(255, 0, 0)):
    pixels.clear()
    pixels.show()
    pos = 0
    for i in range(pixels.count()):
        for j in reversed(range(i, pixels.count())):
            pixels.clear()
            # first set all pixels at the begin
            for k in range(i):
                pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[2], color[1], color[0] ))
            # set then the pixel at position j
            pixels.set_pixel(j, Adafruit_WS2801.RGB_to_color( color[2], color[1], color[0] ))            
            if (isCancelled()):
                break
            pixels.show()
            time.sleep(0.02)
            if (isCancelled()):
                break
