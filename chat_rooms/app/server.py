# -*- coding:utf8 -*-

from gfirefly.server.globalobject import netserviceHandle
from gfirefly.server.globalobject import GlobalObject
from datetime import *

def doConnectionMade(conn):
    """当前连接建立时调用的方法"""
    str1 = "welcome\r\n"
    GlobalObject().netfactory.pushObject(10001, str1,
                                         [conn.transport.sessionno])
    stt2 = "%d is login\r\n" % conn.transport.sessionno
    lis = GlobalObject().netfactory.connmanager._connections.keys()
    lis.remove(conn.transport.sessionno)
    GlobalObject().netfactory.pushObject(10001, stt2, lis)

def doConnectionLost(conn):
    """当连接断开时调用的方法"""
    str2 = "%d is logout\r\n" % conn.transport.sessionno
    lis = GlobalObject().netfactory.connmanager._connections.keys()
    lis.remove(conn.transport.sessionno)
    GlobalObject().netfactory.pushObject(10001, str2, lis)

GlobalObject().netfactory.doConnectionMade = doConnectionMade
GlobalObject().netfactory.doConnectionLost = doConnectionLost

@netserviceHandle
def speak_10001(_conn, data):
    """用户发言的方法"""
    date = datetime.now()
    str1 = date.strftime("%Y-%m-%d %H:%M:%S") + "(" + str(
        _conn.transport.sessionno) + "):\r\n" + data
    lis = GlobalObject().netfactory.connmanager._connections.keys()
    lis.remove(_conn.transport.sessionno)
    GlobalObject().netfactory.pushObject(10001, str1, lis)