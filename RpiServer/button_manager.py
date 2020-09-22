import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

class ButtonManager:
    def __init__(self, callback):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(10, GPIO.RISING, callback=callback)

    def __del__(self):
        GPIO.cleanup()

    def close(self):
        GPIO.cleanup()  
        
    

