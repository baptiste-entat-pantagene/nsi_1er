import network
import threading
import time


def host():
    server = network.Server()
    server.call_listenLoop()
    time.sleep(10)
    server.close()

def user(msg):
    user1 = network.Client()
    user1.send(msg)
    time.sleep(5)
    print(user1.dataReceived)
    user1.close()


threadA = threading.Thread(target= host)
#threadB = threading.Thread(target= user)

threadA.start()
#threadB.start()

user("msg 1")
user("msg 2")

threadA.join()
#threadB.join()



print("---> end <---")
