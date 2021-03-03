import network
import threading
import time


def host():
    server = network.Server()
    server.listenLoop()
    time.sleep(10)
    server.close()

def user():
    user1 = network.Client()
    user1.send("salut bg !")
    time.sleep(5)
    print(user1.dataReceived)
    user1.close()


threadA = threading.Thread(target= host)
threadB = threading.Thread(target= user)

threadA.start()
threadB.start()
threadA.join()
threadB.join()

print("---> end <---")
