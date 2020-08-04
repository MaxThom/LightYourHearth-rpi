from blue_connect import BluetoothComm 
import subprocess
import constants

def main():    
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

