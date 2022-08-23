import smtplib 

archivo = open('correos.txt', 'r').readlines()
lista = list(map(str.strip, archivo))

server = smtplib.SMTP('localhost', 1025)
server.ehlo()
for i in lista:
    mensaje = input("Ingrese el mensaje a enviar: ")
    server.sendmail('eduardo.lopez@gmail.com',i,mensaje)
server.close()
