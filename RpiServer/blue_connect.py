import bluetooth
import constants

class BluetoothComm:
    def __init__(self):
        self.server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)        
        port = 1
        self.server_socket.bind(("", port))
        self.server_socket.listen(1)
        print("Listening bluetooth on port ", port)        
        
    def accept_comm(self):
        print("Accepting connection ...")
        self.client_socket, address = self.server_socket.accept()
        print("Accepted connection from ", address)

    def read_comm_async(self, callback):
        res = ""
        while res != constants.BLUETOOTH_DISCONNECT:
            try:
                res = self.client_socket.recv(1024)                
                res = res.decode('utf_8').rstrip("\r\n").rstrip("\n").rstrip("\r")
            except:
                res = constants.BLUETOOTH_DISCONNECT
                self.server_socket.close()
            
            if len(res):
                callback(res)
            else:
                callback(None)

    def read_comm(self, callback):
        res = ""
        while res != constants.BLUETOOTH_DISCONNECT:
            try:
                res = self.client_socket.recv(1024)
            except:
                res = constants.BLUETOOTH_DISCONNECT
                self.server_socket.close()
            if len(res):
                return res
            else:
                return None
 
    def send_comm(self, text):
        self.client_socket.send(text)

    def close(self):
        self.client_socket.close()
        self.server_socket.close()
        
        
