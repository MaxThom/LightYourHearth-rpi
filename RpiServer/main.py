from blue_connect import BluetoothComm 
from ada_ledstrip import AdaLedstrip
import subprocess
import constants
import asyncio


pixels = AdaLedstrip(constants.PIXEL_COUNT, constants.SPI_PORT, constants.SPI_DEVICE)

def main():
    launch_bluetooth_server()


def launch_bluetooth_server():
    blue_comm = BluetoothComm()  
    blue_comm.accept_comm()
    blue_comm.read_comm_async(on_bluetooth_message_received)

def on_bluetooth_message_received(msg):
    print(msg)
    commandAction[msg]()
        

commandAction = {
        constants.BLUETOOTH_DISCONNECT: launch_bluetooth_server, 
        constants.LED_ON: pixels.pixel_on,
        constants.LED_OFF: pixels.pixel_off
    }

if __name__ == "__main__":
    main()

