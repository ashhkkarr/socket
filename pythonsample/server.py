import socket
s= socket.socket()
print('socket created')
s.bind(('127.0.0.1',9999))

s.listen(5)
print('waiting for connections')

while True:
    c,addr= s.accept()
    print("connected with",addr)
    
    c.send(bytes("welcome to ashkar db",'utf-8'))
    c.close