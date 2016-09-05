#coding:utf8

import time

from socket import AF_INET,SOCK_STREAM,socket
from thread import start_new
import struct
HOST='localhost'
PORT=11009
BUFSIZE=1024
ADDR=(HOST, PORT)
client = socket(AF_INET,SOCK_STREAM)
client.connect(ADDR)

def sendData(sendstr,commandId):
    '''
    78,37,38,48,9,0
    @param sendstr:
    @param commandId:
    @return:
    HEAD_0 = 78#chr(0)
    HEAD_1 = 37#chr(0)
    HEAD_2 = 38#chr(0)
    HEAD_3 = 48#chr(0)
    ProtoVersion = 9#chr(0)
    '''
    HEAD_0 = chr(78)
    HEAD_1 = chr(37)
    HEAD_2 = chr(38)
    HEAD_3 = chr(48)
    ProtoVersion = chr(9)
    ServerVersion = 0
    sendstr = sendstr
    data = struct.pack('!sssss3I',HEAD_0,HEAD_1,HEAD_2,\
                       HEAD_3,ProtoVersion,ServerVersion,\
                       len(sendstr)+4,\
                       commandId)
    senddata = data+sendstr
    return senddata

def resolveRecvdata(data):
    head = struct.unpack('!sssss3I',data[:17])
    length = head[6]
    data = data[17:17+length]
    return data

s1 = time.time()

def start():
    while True:
        time.sleep(1)
        client.sendall(sendData("abdcef", 0))
start()
