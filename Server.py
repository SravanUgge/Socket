import socket
s=socket.socket()
print("socket created")
s.bind(('localhost',5757))
s.listen(5)
print('waiting for connections')

while True:
    c,addr=s.accept()
    name= c.recv(1024).decode()
    msg=c.recv(1024).decode()
    print('connection established with',addr,name)
    print(msg)
    chat=input("write a msg")
    c.send(bytes(chat,'utf-8'))
    c.send(bytes('welcome to server','utf-8'))
    c.close()
