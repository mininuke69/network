import socket

class network():
    class Server():

        def __init__(self):
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        def Create(self, port= 9898):
            self.hostname = socket.gethostname()
            self.ip = socket.gethostbyname(self.hostname)
            self.port = port
            self.addr = (self.ip, self.port)

            self.client.bind(self.addr)
            return self.ip, self.port, self.addr, self.hostname
        
        def Start(self):
            self.client.listen()
        
        def Stop(self):
            self.client.close()

        def AcceptConn(self):
            return self.client.accept()
        
        def Send(self, data: str, connection: socket.socket):
            return connection.send(data.encode())

        def Recv(self, buffer: int, connection: socket.socket):
            return connection.recv(buffer).decode()

    class Client():

        def __init__(self):
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        def Connect(self, addr: tuple):
            self.client.connect(addr)
            self.connected_to = addr
        
        def Send(self, data: str):
            return self.client.send(data.encode())
        
        def Recv(self, buffer: int):
            return self.client.recv(buffer).decode()