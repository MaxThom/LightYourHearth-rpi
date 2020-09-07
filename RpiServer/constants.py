from rpi_ws281x import ws

BLUETOOTH_DISCONNECT = "Disconnect"
LED_OFF = "Led_Off"
LED_RAINBOW_COLOR = "Led_Rainbow_Color"
LED_RAINBOW_CYCLE = "Led_Rainbow_Cycle"
LED_RAINBOW_CYCLE_SUCCESSIVE = "Led_Rainbow_Cycle_Successive"
LED_BRIGHTNESS_DECREASE = "Led_Brightness_Decrease"
LED_BLINK_COLOR = "Led_Blink_Color"
LED_APPEAR_FROM_BACK = "Led_Appear_From_Back"
LED_COLOR_WIPE = "Led_Color_Wipe"
LED_COLOR_WIPE_CYCLE = "Led_Color_Wipe_Cycle"
LED_COLOR_WIPE_RAINBOW = "Led_Color_Wipe_Rainbow"
LED_SET_BRIGHTNESS = "Led_Set_Brightness"

LED_SETTINGS = "Led_Settings"
LED_ANIMATION_CAPABILITIES = "Led_Animation_Capabilities"

LED_STRIP_WS2811 = "WS2811"
LED_STRIP_WS2812B = "WS2812B"
LED_STRIP_SK6812= "SK6812"


# LED strip configuration:
LED_COUNT = 1000          # Number of LED pixels.
LED_PIN = 18           # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000   # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10           # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 127   # Set to 0 for darkest and 255 for brightest
LED_INVERT = False     # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0
LED_STRIP = ws.SK6812W_STRIP


SERVER_CAPABILITIES = {
        LED_OFF: { },
        LED_COLOR_WIPE: { 
            "wait": { 
                "type": "double", 
                "default_value": 0.0, 
                "min_value": 0, 
                "max_value": 1 
            },
            "color": { 
                "type": "color", 
                "default_value": "#00000000"
            },
            "should_clear": {
                "type": "boolean", 
                "default_value": "False",
            }
        },
        LED_COLOR_WIPE_CYCLE: { 
            "wait": { 
                "type": "double", 
                "default_value": 0.01, 
                "min_value": 0, 
                "max_value": 0.25 
            },
            "color": { 
                "type": "color", 
                "default_value": "#FF0000FF"
            },
            "fade_step": {
                "type": "int", 
                "default_value": 50, 
                "min_value": 1, 
                "max_value": 100 
            },
            "loop_forever": {
                "type": "boolean", 
                "default_value": "True",
            }
        },
        LED_COLOR_WIPE_RAINBOW: { 
            "wait": { 
                "type": "double", 
                "default_value": 0.01, 
                "min_value": 0, 
                "max_value": 0.25 
            },
            "fade_step": {
                "type": "int", 
                "default_value": 50, 
                "min_value": 1, 
                "max_value": 100 
            },
            "color_step": {
                "type": "int", 
                "default_value": 30, 
                "min_value": 1, 
                "max_value": 80 
            }
        },
        LED_RAINBOW_COLOR: {
            "wait": { 
                "type": "double", 
                "default_value": 0.05, 
                "min_value": 0, 
                "max_value": 1 
            },
            "loop_forever": {
                "type": "boolean", 
                "default_value": "True"
            }
        },
        LED_RAINBOW_CYCLE: { 
            "wait": { 
                "type": "double", 
                "default_value": 0.005, 
                "min_value": 0, 
                "max_value": 0.1 
            },
            "loop": { 
                "type": "int", 
                "default_value": 0, 
                "min_value": 0, 
                "max_value": 100 
            },
            "loop_forever": {
                "type": "boolean", 
                "default_value": "True"
            } 
        },
        LED_RAINBOW_CYCLE_SUCCESSIVE: {
            "wait": { 
                "type": "double", 
                "default_value": 0.1, 
                "min_value": 0, 
                "max_value": 1 
            } 
        },
        LED_BRIGHTNESS_DECREASE: { 
            "wait": { 
                "type": "double", 
                "default_value": 0.01, 
                "min_value": 0, 
                "max_value": 1 
            },
            "step": { 
                "type": "int", 
                "default_value": 1, 
                "min_value": 1, 
                "max_value": 100 
            } 
        },
        LED_BLINK_COLOR: { 
            "wait": { 
                "type": "double", 
                "default_value": 0.5, 
                "min_value": 0, 
                "max_value": 1 
            },
            "blink_time": { 
                "type": "int", 
                "default_value": 5, 
                "min_value": 0, 
                "max_value": 100 
            },
            "color": { 
                "type": "color", 
                "default_value": "#00000000"
            }
        },
        LED_APPEAR_FROM_BACK: { 
            "color": { 
                "type": "color", 
                "default_value": "#00000000"
            }
        }
    }
