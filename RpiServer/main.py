from blue_connect import BluetoothComm 
from ada_ledstrip import AdaLedstrip
import subprocess
import constants
import asyncio
import pprint
import time

# ps -ef | grep python
# sudo kill -9 [pid]

pixels = AdaLedstrip(constants.PIXEL_COUNT, constants.SPI_PORT, constants.SPI_DEVICE)
blue_comm = None

def main():
    launch_bluetooth_server("")


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
        blue_comm.send_comm("Unknown command")

def get_server_capabilities(args):
    global blue_comm
    for anim in constants.SERVER_CAPABILITIES: 
        print("Cap:" + anim + ":" + pprint.pformat(constants.SERVER_CAPABILITIES[anim]))        
        time.sleep(0.075)
        blue_comm.send_comm("Cap:" + anim + ":" + pprint.pformat(constants.SERVER_CAPABILITIES[anim]))
        
    

commandAction = {
        constants.BLUETOOTH_DISCONNECT: launch_bluetooth_server,         
        constants.LED_OFF: pixels.pixel_off,
        constants.LED_RAINBOW_COLOR: pixels.pixel_rainbow_colors,
        constants.LED_RAINBOW_CYCLE: pixels.pixel_rainbow_cycle,
        constants.LED_RAINBOW_CYCLE_SUCCESSIVE: pixels.pixel_rainbow_cycle_successive,
        constants.LED_BRIGHTNESS_DECREASE: pixels.pixel_brightness_decrease,
        constants.LED_BLINK_COLOR: pixels.pixel_blink_color,
        constants.LED_APPEAR_FROM_BACK: pixels.pixel_appear_from_back,
        constants.LED_SETTINGS: pixels.set_settings,
        constants.LED_ANIMATION_CAPABILITIES: get_server_capabilities
    }


if __name__ == "__main__":
    pprint.pprint(constants.SERVER_CAPABILITIES)
    main()

