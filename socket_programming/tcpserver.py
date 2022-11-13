import socket,socketserver
from chatbot import gettingresponse

class chatserver(socket):
	host = 'localhost'
	port = 7000

	socobj = socket.socket()

	socobj.bind((host,port))

	socobj.listen()

	while True:
		con,add = socobj.accept()
		msg = con.recv(1024).decode("utf-8") 
		print(msg)
		res = gettingresponse(msg)
		con.sendall(str.encode(res))

server = socketserver(('localhost',7000),chatserver)
server.server_forever()