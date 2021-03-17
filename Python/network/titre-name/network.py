import socket
import threading


class Server:
    def __init__(self) -> None:
        self.HOST = "" #void
        self.PORT = 50505

        #client
        self.remoteUser = {}
        self.receiveData = {}

        #socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.HOST, self.PORT))
        self.sock.setblocking(True)
        self.sock.listen(5)
    
    def listen(self):
        acceptTh = threading.Thread(target=self._accept)
        for addr, connect in self.remoteUser.items():
            print("receive start for ->", addr, connect)
            reveiveTh = threading.Thread(target=self._receive, args=(addr, connect))
            reveiveTh.start()
        acceptTh.start()
        

    def _accept(self):
        while True:
            connect, addr = self.sock.accept()
            print("connect with", addr)
            self.remoteUser[addr] = connect

            #dataByt = connect.recv(1024)
            #data = dataByt.decode("utf-8")
            #print(data)

    def _receive(self, addr, connect):
        dataByt = connect.recv(1024)
        data = dataByt.decode("utf-8")
        print(addr, "send", data)



class Client:
    def __init__(self) -> None:
        self.HOST = socket.gethostname()
        self.PORT = 50505
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.sock.connect((self.HOST, self.PORT))
            return True
        except:
            return False
    
    def send(self, msg:str):
        self.sock.send(msg.encode("utf-8"))