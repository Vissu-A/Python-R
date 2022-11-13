from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from chatbot import gettingresponse


class ChatServer(WebSocket):

    def handleMessage(self):
        # echo message back to client
        message = self.data
        response = gettingresponse(message)
        self.sendMessage(response)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')



server = SimpleWebSocketServer('localhost', 7000, ChatServer)
server.serveforever()