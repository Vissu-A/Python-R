import socket

host = 'localhost'  
print(host) 
port = 9000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(b'Hello, world')
data = s.recv(1024)
s.close()
print('Received', repr(data))