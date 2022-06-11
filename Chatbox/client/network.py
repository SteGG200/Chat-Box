import socket 

class Network : 
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '192.168.1.12'
        self.port = 8888
        self.addr = (self.server,self.port)
        self.connect()
    def connect(self):
        self.client.connect(self.addr)
    def send(self, data):
        # print(data)
        self.client.send(str.encode(data))
    def receive(self):
        return self.client.recv(2048).decode()