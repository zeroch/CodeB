import socket
import sys

HOST, PORT = "codebb.cloudapp.net", 17429

USERNAME, PASSWORD = "HackCat", "xnvgMbgo0329"

class BloombergConnection:
    def connect(self):
        data = USERNAME + ' ' + PASSWORD + '\n'
        self.socket.sendall(bytes(data, "utf-8"))
        

    def disconnect(self):
        self.socket.sendall(bytes("\nCLOSE_CONNECTION\n", "utf-8"))
        self.socket.close()

    def run(self, command):
        self.socket.sendall(bytes(command + "\n", "utf-8"))
        return self.socket_file.readline().split()[1:]
    
    def save_securities(self):
        sec_dict = {}

        data = self.run("SECURITIES")
        print(len(data))
        for i in range(int(len(data) / 4)):
            sec_dict[data[i * 4]] = data[i * 4 + 1: i * 4 + 4]
        return sec_dict

    def __enter__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((HOST, PORT))
        self.socket_file = self.socket.makefile()
        self.connect()
        return self

    def __exit__(self, type, value, traceback):
        self.disconnect()
