import socket
adresseIP = "127.0.0.1"	# Ici, le poste local
port = 50000	# Se connecter sur le port 50000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((adresseIP, port))
except:
    print("!-> serveur close <-!\npease restart")
    exit(0)

print("Connecté au serveur")
client.send("Bonjour, je suis le client".encode("utf-8"))
reponse = client.recv(255)
print(reponse.decode("utf-8"))
print("Connexion fermée")
client.close()