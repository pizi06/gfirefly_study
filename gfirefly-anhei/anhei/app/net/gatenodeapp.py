#coding:utf8
'''
Created on 2013-8-14

@author: lan (www.9miao.com)
'''
from gfirefly.server.globalobject import GlobalObject,remoteserviceHandle


@remoteserviceHandle('gate')
def pushObject(topicID,msg,sendList):
    print "pushObject......."
    GlobalObject().netfactory.pushObject(topicID, msg, sendList)