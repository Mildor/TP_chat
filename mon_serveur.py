# coding: utf-8 

import multiprocessing
from os import kill
import socket as socke
from socket import *
import threading


users = []

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self): 
        print("Connexion de %s %s" % (self.ip, self.port, ))
        while True:
            data = self.clientsocket.recv(2048)
            data = data.decode()
            client = socke.gethostbyaddr(self.ip)
            print(data)
            self.multicast(data)
            if data is None or data == "" or data=="quit":
                print("Connexion de %s %s coupé" % (self.ip, self.port, ))
                break

    def multicast(self, message):
        for user in users:
            if user != self.clientsocket:
                user.send(message.encode())


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
