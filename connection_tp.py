import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto(bytes(str(input('entrez votre phrase : ')),'UTF-8'),('info24-13',9999))


while True:
    data, addr = s.recvfrom(1024)
    print ("Message: ", data)