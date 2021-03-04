import socket
import time
import threading



class Server:
    def __init__(self) -> None:
        self.threadStat = True

        # create an INET, STREAMing socket
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((socket.gethostname(), 50000))
        self.server.listen(5)
        print("serveur start, port ->", self.server.getsockname())

    def call_listenLoop(self):
        self.threadListen = threading.Thread(target=self.__listenLoop)
        self.threadListen.start()

    def __listenLoop(self):
        while True:
            print("run")
            if self.threadStat == False:
                break
            client, infosClient = self.server.accept()
            print("Client connecté. Adresse " + infosClient[0])
            requete = client.recv(255)  # Reçoit 255 octets. Vous pouvez changer pour recevoir plus de données
            print(requete.decode("utf-8")) #msg reçu duclient

            time.sleep(2)
            reponse = "Bonjour, je suis le serveur"
            client.send(reponse.encode("utf-8"))
            print("Connexion fermée")
            client.close()

    def close(self):
        self.threadStat = False
        self.threadListen.join()
        self.server.close()

"""
def client():
    adresseIP = "192.168.56.1"  # Ici, le poste local
    port = 50000  # Se connecter sur le port 50000
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((adresseIP, port))
    print("Connecté au serveur")
    client.send("Bonjour, je suis le client".encode("utf-8"))
    reponse = client.recv(255)
    print(reponse.decode("utf-8"))
    print("Connexion fermée")
    client.close()
"""

class Client:
    def __init__(self) -> None:
        self.serverIp = "192.168.56.1" #adresse du serveur
        self.port = 50000 ## Se connecter sur le port XX
        self.__connect()

        self.threadReceived = threading.Thread(target= self.__receivedLoop)
        self.threadStat = True
        self.threadReceived.start()
        

        self.dataReceived = []
    
    def __connect(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                self.socket.connect((self.serverIp, self.port))
                break
            except:
                print("connection denied or impossible")
                print("retry in 5 sec")
            
            time.sleep(5)
    
    def __receivedLoop(self):
        while self.threadStat == True:
            try:
                reply = self.socket.recv(255) # Reçoit 255 octets. Vous pouvez changer pour recevoir plus de données
            except:
                pass
            else:
                if reply.decode("utf-8") != "":
                    self.dataReceived.append(reply.decode("utf-8"))
        
    def send(self, msg:str):
        self.socket.send(msg.encode("utf-8"))
    
    def close(self):
        self.threadStat = False
        self.threadReceived.join()
        self.socket.close()