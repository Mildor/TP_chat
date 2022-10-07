from datetime import date
import socket
from datetime import date



# try:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print("Socket créé")
# except socket.error as err:
#     print("Socket non créé %s" %(err))
#     # port pour le socket
# port = 80
# try:
#     ip = socket.gethostbyname('www.univ-orleans.fr')
# except socket.gaierror:
#     print("Il y a certainement un souci avec le site recherché ! ")
#     sys.exit()
# # connexion au serveur
# s.connect((ip, port))
# print("Le socket s'est bien connecté à l’Université d’Orléans sur le port == %s"
# %(port), " à l'adresse %s" %(ip))
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('',9999))# lien du socket
while True:
    message=s.recvfrom(1024)
    message_text = message[0].decode()
    client = socket.getnameinfo(message[1], 10)
    print(client[0], message_text)
    if message == 'quit':
        break