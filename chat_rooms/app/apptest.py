#coding:utf8

from gfirefly.server.globalobject import netserviceHandle

@netserviceHandle
def echo_1(_conn,data):
    return data

    


