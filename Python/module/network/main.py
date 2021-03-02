import network
import threading


threadA = threading.Thread(None, network.serveur, None, {}) 
threadB = threading.Thread(None, network.client, None, {}) 


threadA.start() 
threadB.start()