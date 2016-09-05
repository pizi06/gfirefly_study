#coding:utf8
'''
Created on 2013-8-14

@author: lan (www.9miao.com)
'''
from gfirefly.server.globalobject import GlobalObject
from gfirefly.netconnect.datapack import DataPackProtoc


def callWhenConnLost(conn):
    print "call when conn lost......"
    dynamicId = conn.transport.sessionno
    GlobalObject().remote['gate'].callRemoteNotForResult("netconnlost",dynamicId)

GlobalObject().netfactory.doConnectionLost = callWhenConnLost
dataprotocl = DataPackProtoc(78,37,38,48,9,0)
GlobalObject().netfactory.setDataProtocl(dataprotocl)



def loadModule():
    import netapp
    import gatenodeapp