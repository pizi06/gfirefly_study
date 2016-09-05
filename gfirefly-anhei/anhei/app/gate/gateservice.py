#coding:utf8
'''
Created on 2013-8-14

@author: lan (www.9miao.com)
'''
from gfirefly.utils.services import CommandService
from gtwisted.utils import log
from twisted.internet import defer


class LocalService(CommandService):
    
    def callTarget(self,targetKey,*args,**kw):
        '''call Target by Single
        @param conn: client connection
        @param targetKey: target ID
        @param data: client data
        '''
        target = self.getTarget(targetKey)
        if not target:
            log.err('the command '+str(targetKey)+' not Found on service')
            return None
        if targetKey not in self.unDisplay:
            log.msg("call method %s on service[single]"%target.__name__)
        response = target(targetKey,*args,**kw)
        return response

localservice = LocalService('localservice')

def localserviceHandle(target):
    '''服务处理
    @param target: func Object
    '''
    localservice.mapTarget(target)
