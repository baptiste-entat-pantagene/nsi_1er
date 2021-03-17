import threading
import network
import time

def startServer():
    server = network.Server()
    server.listen()


def startClient():
    client = network.Client()
    stat = client.connect()
    if stat == False:
        print("hoo no, server down")
        return None
    time.sleep(1)
    client.send("hallu server !")
    



serverThread = threading.Thread(target=startServer)
clientThread = threading.Thread(target=startClient)

serverThread.start()
time.sleep(1)
clientThread.start()

clientThread.join()
print("clientThread joint")

serverThread.join()
print("serverThread joint")
