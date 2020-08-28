from blue_connect import BluetoothComm 
from ledstrip import Ledstrip
import subprocess
import constants
import pprint
import time
import datetime

# ps -ef | grep python
# sudo kill -9 [pid]
# pip freeze > requirements.txt
# pip install -r requirements.txt

pixels = Ledstrip()
blue_comm = None

def main():
    global blue_comm
    try:
        launch_bluetooth_server("")
    except Exception as e:         
        log_message(e)
        blue_comm.close()

def launch_bluetooth_server(args):
    global blue_comm
    blue_comm = BluetoothComm()
    blue_comm.accept_comm()
    blue_comm.read_comm_async(on_bluetooth_message_received)

def on_bluetooth_message_received(msg):
    global blue_comm
    print(msg)

    arr = msg.split(":")
    cmd = arr[0]
    args = {}
    if (len(arr) > 1 and arr[1]):
        arg_str = arr[1]    
        for val in arg_str.split(","):
            key_value = val.split("=")
            args[key_value[0]] = key_value[1]        

    print(cmd)
    pprint.pprint(args)

    if cmd in commandAction:
        commandAction[cmd](args)
    else:
        print("Unknown command")

def get_server_capabilities(args):
    global blue_comm
    for anim in constants.SERVER_CAPABILITIES: 
        print("Cap:" + anim + ":" + pprint.pformat(constants.SERVER_CAPABILITIES[anim]))        
        time.sleep(0.075)
        blue_comm.send_comm("Cap:" + anim + ":" + pprint.pformat(constants.SERVER_CAPABILITIES[anim]))
        
def log_message(msg):
    print(msg)
    f = open("/home/pi/Desktop/LightYourHearth-rpi/Logs/LightYourHeath_Logs.txt", "a")
    f.write("[%s] -> %s.\n" % (datetime.datetime.now(), msg))
    f.close()
   

commandAction = {
        constants.BLUETOOTH_DISCONNECT: launch_bluetooth_server,         
        constants.LED_OFF: pixels.pixel_off,
        constants.LED_RAINBOW_COLOR: pixels.pixel_rainbow_colors,
        constants.LED_RAINBOW_CYCLE: pixels.pixel_rainbow_cycle,
        constants.LED_RAINBOW_CYCLE_SUCCESSIVE: pixels.pixel_rainbow_cycle_successive,
        constants.LED_BRIGHTNESS_DECREASE: pixels.pixel_brightness_decrease,
        constants.LED_BLINK_COLOR: pixels.pixel_blink_color,
        constants.LED_APPEAR_FROM_BACK: pixels.pixel_appear_from_back,
        constants.LED_COLOR_WIPE: pixels.pixel_color_wipe,
        constants.LED_SET_BRIGHTNESS: pixels.set_brightness,
        constants.LED_SETTINGS: pixels.set_settings,
        constants.LED_ANIMATION_CAPABILITIES: get_server_capabilities
    }


if __name__ == "__main__":
    pprint.pprint(constants.SERVER_CAPABILITIES)
    main()

