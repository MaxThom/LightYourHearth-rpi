import RPi.GPIO as GPIO
import datetime

class ButtonManager:
    def __init__(self, callback):
        self.callback = callback
        self.last_button_click = datetime.datetime.now()
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(10, GPIO.RISING, callback=self.button_callback)

    def button_callback(self, channel):
        now = datetime.datetime.now()
        diff = (now - self.last_button_click)        
        if (diff.total_seconds() >= 0.5):
            self.last_button_click = now
            self.callback(channel)        

    def __del__(self):
        GPIO.cleanup()

    def close(self):
        GPIO.cleanup()  
        
    

