import socket
import sys
""" Création d’une instance de socket. Le premier paramètre est AF_INET (pour
l’adresse IP) et le deuxième est SOCK_STREAM (pour le protocole TCP orienté
connexion)."""
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket créé")
except socket.error as err:
    print("Socket non créé %s" %(err))
# port pour le socket
port = 80
try:
    ip = socket.gethostbyname('www.univ-orleans.fr')
except socket.gaierror:
    print("Il y a certainement un souci avec le site recherché ! ")
sys.exit()

# connexion au serveur
s.connect((ip, port))
print("Le socket s'est bien connecté à l’Université d’Orléans sur le port == %s"
%(port), " à l'adresse %s" %(ip))