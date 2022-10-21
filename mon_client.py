from socket import *
from threading import *

#Connexion au PC Serveur
#target correspondant au nom/ip du serveur serveur
#port corresspondant au port du serveur
target = "info24-15"
port = "9999"
connexion = socket(AF_INET, SOCK_STREAM)
connexion.connect(("info24-15", 9999))

#Fonction d'envoie de message
def envoie():
    while True:
        message = input()
        if message:
            message = gethostname()+" : "+message
            connexion.send(message.encode())

#Fonction réception message
def thread_en_reception():
    while True:
        message = connexion.recv(1024).decode()
        print(message)

#création de thread pour la récéption et l'envoie de message
Thread(target=thread_en_envoie).start()
Thread(target=thread_en_reception).start()
