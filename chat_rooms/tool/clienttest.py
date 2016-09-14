#coding:utf8

import time
import socket
#from socket import AF_INET,SOCK_STREAM,socket
from thread import start_new
import struct
#HOST='localhost'
#PORT=1000
#BUFSIZE=1024
#ADDR=(HOST , PORT)
#client = socket(AF_INET,SOCK_STREAM)
#client.connect(ADDR)

def sendData(sendstr,commandId):
    HEAD_0 = chr(0)
    HEAD_1 = chr(0)
    HEAD_2 = chr(0)
    HEAD_3 = chr(0)
    ProtoVersion = chr(0)
    ServerVersion = 0
    sendstr = sendstr
    data = struct.pack('!sssss3I',HEAD_0,HEAD_1,HEAD_2,\
                       HEAD_3,ProtoVersion,ServerVersion,\
                       len(sendstr)+4,commandId)
    senddata = data+sendstr
    return senddata

def resolveRecvdata(data):
    head = struct.unpack('!sssss3I',data[:17])
    length = head[6]
    data = data[17:17+length]
    return data

def sendMessage(connection):
    while 1:
        data = raw_input()
        length = len(data)
        if length > 80:
            length = 80
        line = length * "_"
        data += "\r\n" + line
        connection.sendall(sendData(data, 10001))
        print line

def receiveMessage(connection):
    while 1:
        message = connection.recv(1024)
        message = resolveRecvdata(message)
        print message

class ChatServer:

    def __init__(self, port):
        self.port = port
        self.srvsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.srvsock.connect(("127.0.0.1", port))

    def run(self):
        start_new(sendMessage, (self.srvsock,))
        start_new(receiveMessage, (self.srvsock,))

if __name__ == "__main__":
    myServer = ChatServer(10000).run()
    while 1:
        pass