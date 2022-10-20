from socket import *
from threading import *

connexion = socket(AF_INET, SOCK_STREAM)
connexion.connect(("info24-15", 9999))

def thread_en_envoie():
    while True:
        message = input()
        if message:
            message = gethostname()+" : "+message
            connexion.send(message.encode())

def thread_en_reception():
    while True:
        message = connexion.recv(1024).decode()
        print(message)

Thread(target=thread_en_envoie).start()
Thread(target=thread_en_reception).start()