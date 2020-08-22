BLUETOOTH_DISCONNECT = "Disconnect"
LED_OFF = "Led_Off"
LED_RAINBOW_COLOR = "Led_Rainbow_Color"
LED_RAINBOW_CYCLE = "Led_Rainbow_Cycle"
LED_RAINBOW_CYCLE_SUCCESSIVE = "Led_Rainbow_Cycle_Successive"
LED_BRIGHTNESS_DECREASE = "Led_Brightness_Decrease"
LED_BLINK_COLOR = "Led_Blink_Color"
LED_APPEAR_FROM_BACK = "Led_Appear_From_Back"

LED_SETTINGS = "Led_Settings"
LED_ANIMATION_CAPABILITIES = "Led_Animation_Capabilities"

PIXEL_COUNT = 64

TYPE_WS2812B = "WS2812B"
SPI_PORT   = 0
SPI_DEVICE = 0


SERVER_CAPABILITIES = {
        LED_OFF: { },
        LED_RAINBOW_COLOR: {
            "wait": { 
                "type": "double", 
                "default_value": 0.05, 
                "min_value": 0, 
                "max_value": 1 
            } 
        },
        LED_RAINBOW_CYCLE: { 
            "wait": { 
                "type": "double", 
                "default_value": 0.005, 
                "min_value": 0, 
                "max_value": 1 
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
                "type": "double", 
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
                "type": "double", 
                "default_value": 5, 
                "min_value": 0, 
                "max_value": 100 
            },
            "color": { 
                "type": "color", 
                "default_value": "#FFFFFF"
            }
        },
        LED_APPEAR_FROM_BACK: { 
            "color": { 
                "type": "color", 
                "default_value": "#1E90FF"
            }
        }
    }