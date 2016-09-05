#coding:utf8
'''
Created on 2013-9-4

@author: hg (www.9miao.com)
'''
from flask import request
from memmode import register_admin
from gfirefly.server.globalobject import GlobalObject,webserviceHandle
from urls import getDayRecordList,getStatistics
import json

@webserviceHandle('/opera')
def operaPlayer():
    username = request.args['username']
    oprea_str = request.args['opera_str']
    usermodedata = register_admin.getObjData(username)#register_admin，注册表的mmode管理器，getObjData(username)，通过主键获取的对应的数据，dict型
    if not usermodedata:
        return "Account does not exist!!!"
    pid = usermodedata.get('characterId')#角色id
    if not pid:
        return "Role does not exist!!!"#角色不存在，创建了账号没有创建人物
    gate_node = GlobalObject().remote.get('gate')
    gate_node.callRemote("opera_player",pid,oprea_str)
    return "Success"
    
@webserviceHandle('/dayrecored')
def dayrecored():
    index = int(request.args['index'])#日前+dd
    data = getDayRecordList(index)
    response = json.dumps(data)
    return response
    

@webserviceHandle('/statistics')
def statistics():
    data = getStatistics() 
    response = json.dumps(data)
    return response
        

@webserviceHandle('/test')
def test():
    return """<!DOCTYPE html>
<html>
<head>
<title>123</title>
</head>
<body>
testtt
<script language="javascript" type="text/javascript">
document.write ('<a href="http://www.51.la/?16181997" target="_blank"><img alt="&#x35;&#x31;&#x2E;&#x6C;&#x61;&#x20;&#x4E13;&#x4E1A;&#x3001;&#x514D;&#x8D39;&#x3001;&#x5F3A;&#x5065;&#x7684;&#x8BBF;&#x95EE;&#x7EDF;&#x8BA1;" src="http://icon.ajiang.net/icon_9.gif" style="border:none" /></a>');
var a1997tf="51la";var a1997pu="";var a1997pf="51la";var a1997su=window.location;var a1997sf=document.referrer;var a1997of="";var a1997op="";var a1997ops=1;var a1997ot=1;var a1997d=new Date();var a1997color="";if (navigator.appName=="Netscape"){a1997color=screen.pixelDepth;} else {a1997color=screen.colorDepth;}
try{a1997tf=top.document.referrer;}catch(e){}
try{a1997pu =window.parent.location;}catch(e){}
try{a1997pf=window.parent.document.referrer;}catch(e){}
try{a1997ops=document.cookie.match(new RegExp("(^| )AJSTAT_ok_pages=([^;]*)(;|$)"));a1997ops=(a1997ops==null)?1: (parseInt(unescape((a1997ops)[2]))+1);var a1997oe =new Date();a1997oe.setTime(a1997oe.getTime()+60*60*1000);document.cookie="AJSTAT_ok_pages="+a1997ops+ ";path=/;expires="+a1997oe.toGMTString();a1997ot=document.cookie.match(new RegExp("(^| )AJSTAT_ok_times=([^;]*)(;|$)"));if(a1997ot==null){a1997ot=1;}else{a1997ot=parseInt(unescape((a1997ot)[2])); a1997ot=(a1997ops==1)?(a1997ot+1):(a1997ot);}a1997oe.setTime(a1997oe.getTime()+365*24*60*60*1000);document.cookie="AJSTAT_ok_times="+a1997ot+";path=/;expires="+a1997oe.toGMTString();}catch(e){}
try{if(document.cookie==""){a1997ops=-1;a1997ot=-1;}}catch(e){}
a1997of=a1997sf;
if(a1997pf!=="51la"){a1997of=a1997pf;}
if(a1997tf!=="51la"){a1997of=a1997tf;}
a1997op=a1997pu;
try{lainframe}catch(e){a1997op=a1997su;}
a1997src='http://web.51.la:82/go.asp?svid=8&id=16181997&tpages='+a1997ops+'&ttimes='+a1997ot+'&tzone='+(0-a1997d.getTimezoneOffset()/60)+'&tcolor='+a1997color+'&sSize='+screen.width+','+screen.height+'&referrer=www.baidu.com'+'&vpage='+escape(a1997op)+'&vvtime='+a1997d.getTime();
setTimeout('a1997img = new Image;a1997img.src=a1997src;',0);
</script>
<noscript><a href="http://www.51.la/?16181997" target="_blank"><img alt="&#x6211;&#x8981;&#x5566;&#x514D;&#x8D39;&#x7EDF;&#x8BA1;" src="http://img.users.51.la/16181997.asp" style="border:none" /></a></noscript>
</body>
</html>"""

        
        
        



