# coding: utf-8 

import multiprocessing
from os import kill
import socket
from socket import *
import threading
import sys

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self): 
        i = 0
        while i == 0:
            print("Connexion de %s %s" % (self.ip, self.port, ))
            data = self.clientsocket.recv(2048)
            data = data.decode()
            print(data)
            if data == 'quit':
                self.clientsocket.send(bytes(data, 'UTF-8'))
                print("Connexion fermée de %s %s" % (self.ip, self.port, ))

sock = socket(AF_INET, SOCK_STREAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind(("",1111))



while True:
    sock.listen(10)
    print( "En écoute...")
    (clientsocket, (ip, port)) = sock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()
