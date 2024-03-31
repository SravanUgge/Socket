import socket
c=socket.socket()
c.connect(('localhost',5757))
name=input('enter your name')
c.send(bytes(name,'utf-8'))
chat=input("write a msg")
c.send(bytes(chat,'utf-8'))
chat=print(c.recv(1024).decode())
print(c.recv(1024).decode())
