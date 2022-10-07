# coding: utf-8 

import socket
import threading

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self): 
   
        print("Connexion de %s %s" % (self.ip, self.port, ))

        data = self.clientsocket.recv(2048)
        print("Ouverture du fichier: ", data.decode(), "...")
        fp = open(data, 'rb')
        self.clientsocket.send(fp.read())

        print("Client %s %s" % (self.ip, self.port, ) + " déconnecté...")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("",1111))

while True:
    sock.listen(10)
    print( "En écoute...")
    (clientsocket, (ip, port)) = sock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()
