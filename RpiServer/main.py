from blue_connect import BluetoothComm 
from ada_ledstrip import AdaLedstrip
import subprocess
import constants


def main():
    pixels = AdaLedstrip(constants.PIXEL_COUNT, constants.SPI_PORT, constants.SPI_DEVICE)
    pixels.pixel_on()
    accept_bluetooth_client()
    
 

def accept_bluetooth_client():
    blue_comm = BluetoothComm()  
    blue_comm.accept_comm()
    blue_comm.read_comm_async(on_bluetooth_message_received)

def on_bluetooth_message_received(msg):
    print(msg)
    if (msg == constants.BLUETOOTH_DISCONNECT):
        accept_bluetooth_client()
        


if __name__ == "__main__":
    main()

