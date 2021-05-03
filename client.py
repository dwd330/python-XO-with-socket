import socket
import threading

class Client:
    def __init__(self, clientid1,clientid2):
        self.clientid1 = clientid1
        self.clientid2 = clientid2
        #socket create
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(('localhost', 58585))
        self.s.send(bytes(self.clientid1, encoding='utf-8'))
        threading._start_new_thread( self.RecivHandler,())
        self.recived=''
    #handle recive
    def RecivHandler(self):
        while True:
            self.recived=self.s.recv(256).decode()

    def get_data(self) :
        return self.recived


    #send message
    def send(self,posX,posY):
        self.posX=posX
        self.posY=posY
        pos_data=self.clientid2 +':'+str(posX)+','+str(posY)
        self.s.send(bytes(pos_data, encoding='utf-8'))









   
