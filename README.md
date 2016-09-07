gfirefly學習，利用暗黑服務器端
查看代碼才發現DiabloWorld-V1.6是使用firefly版本的，故從新找了份代碼gfirefly-anhei
關鍵是這麼久沒更新學習日誌是源於我的gfirefly沒有真正的安裝好。
之前的安裝完後，使用其期待的測試腳本測試時每次聯通上去就會立刻把客戶端踢掉。
```
2016-09-05 16:40:19+0800 [-] Client 0 login in.[127.0.0.1,51242]
2016-09-05 16:40:19+0800 [-] Client 0 login out.
```
后經請教朋友才發現我的gevent版本過高（1.1.1），卸載后安裝1.0.2版gevent。一切ok
```
2016-09-05 11:37:52+0800 [-] Client 0 login in.[127.0.0.1,8162]
2016-09-05 11:38:02+0800 [-] call method echo_1 on service[single]
2016-09-05 11:38:02+0800 [-] 1
2016-09-05 11:38:12+0800 [-] call method echo_1 on service[single]
2016-09-05 11:38:12+0800 [-] 2
2016-09-05 11:38:22+0800 [-] call method echo_1 on service[single]
2016-09-05 11:38:22+0800 [-] 3
```

master 模塊剛被同事問住了，作何用途？和gate的區別？
用途：
剛好看到一篇文章分析各個模塊的盜用之：
http://www.tuicool.com/articles/AVJBni
![gfirefly包含的组件](http://od0yttd3b.bkt.clouddn.com/zaYb2er.png)
1. master管理节点  这是用来管理所有节点的节点，如可通过http来关闭所有节点(可回调节点注册的关闭方法)，其实master节点也可以理解为是分布式root节点，其它节点都是remote节点
2. net前端节点   net节点是client端连接节点，负责数据包的结束，解包，封包，发送。net节点也是gate节点的分布式节点，由于游戏中流量较大，所以一般net节点只负责解包，封包，然后将解包后的数据转发给gate分布式根节点，处理完毕后再有net节点将处理结果发给client
3. gate分布式根节点  net节点将解包的数据发给gate节点后，gate节点可以自己处理数据返回结果，也可以调用remote子节点处理数据。
4. remote子节点  一般remote子节点都是真正干活的节点
5. dbfront节点   这个节点一般是负责管理memcache和数据库交互的节点


備忘：
ConnectionManager.pushObject
http://www.cnblogs.com/123ing/p/3905074.html
http://www.tuicool.com/articles/yuIjeyr
http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652563721&idx=1&sn=bad7d44dfe7d68ca84f2eb2d7b912f86&scene=0#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652563721&idx=2&sn=e9ef6ff4d101e2daa03cc6a02d5fbc53&scene=0&ptlang=2052&ADUIN=270593769&ADSESSION=1473059730&ADTAG=CLIENT.QQ.5461_.0&ADPUBNO=26553#wechat_redirect