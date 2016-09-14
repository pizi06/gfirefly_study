gfirefly版简易聊天系统：

依照一个firefly修改而来，其实就是导入firefly的地方换成gfirefly就好了。

之前也一直想写一个聊天系统，翻看了一些资料和源码，知道调用pushObject就可以向客户端发送消息，

但无赖没发现怎么获取用户列表。
得益于该文章[使用Firefly编写简易聊天室](http://www.9miao.com/thread-43974-3-1.html)了解到通过

`GlobalObject().netfactory.connmanager._connections.keys()`

获取所有客户端，然后：

`lis.remove(_conn.transport.sessionno)`

去除自己。

server：
python startmaster.py

client:
python tool/clienttest.py