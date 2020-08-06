from blue_connect import BluetoothComm 
from ada_ledstrip import AdaLedstrip
import subprocess
import constants
import asyncio


pixels = AdaLedstrip(constants.PIXEL_COUNT, constants.SPI_PORT, constants.SPI_DEVICE)
blue_comm = None

async def main():
    launch_bluetooth_server()


def launch_bluetooth_server():
    global blue_comm
    blue_comm = BluetoothComm()
    blue_comm.accept_comm()
    blue_comm.read_comm_async(on_bluetooth_message_received)

def on_bluetooth_message_received(msg):
    global blue_comm
    print(msg)
    if msg in commandAction:
        commandAction[msg]()
    else:
        print("Unknown command")
        blue_comm.send_comm("Unknown command")

commandAction = {
        constants.BLUETOOTH_DISCONNECT: launch_bluetooth_server,         
        constants.LED_OFF: pixels.pixel_off,
        constants.LED_RAINBOW_COLOR: pixels.pixel_rainbow_colors,
        constants.LED_RAINBOW_CYCLE: pixels.pixel_rainbow_cycle,
        constants.LED_RAINBOW_CYCLE_SUCCESSIVE: pixels.pixel_rainbow_cycle_successive,
        constants.LED_BRIGHTNESS_DECREASE: pixels.pixel_brightness_decrease,
        constants.LED_BLINK_COLOR: pixels.pixel_blink_color,
        constants.LED_APPEAR_FROM_BACK: pixels.pixel_appear_from_back
    }

if __name__ == "__main__":
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(main())
    asyncio.run(main())
    #main()

