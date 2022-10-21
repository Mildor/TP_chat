# coding: utf-8 

import socket as socke
from socket import *
import threading

#List d'utilisateurs connecté
users = []

#objet client qui correspond a un client qui se connecte au serveur, il hérite de la class threading afin de pouvoir activé plusieurs connexion en même temps
class ClientThread(threading.Thread):
    
    #initialisation de la class ClientThread
    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))
    
    #Fonction run qui s'active a la creation d'un clientThread 
    def run(self): 
        print("Connexion de %s %s" % (self.ip, self.port, ))
        
        #Boucle qui permet la réception de message
        i = 1
        while i==1:
            data = self.clientsocket.recv(2048)
            data = data.decode()
            client = socke.gethostbyaddr(self.ip)
            print(data)
            self.multicast(data)
            if data is None or data == "" or data=="quit":
                print("Connexion de %s %s coupé" % (self.ip, self.port, ))
                i = 2
    
    #Fonction qui envoie un message
    def multicast(self, message):
        for user in users:
            if user != self.clientsocket:
                user.send(message.encode())

#Boucle de création du serveur, puis de création de Thread client 
while True:
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(("",1111))
    sock.listen(10)
    print( "En écoute...")
    (clientsocket, (ip, port)) = sock.accept()
    users.append(clientsocket)
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()
