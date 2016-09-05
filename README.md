gfirefly學習，利用暗黑服務器端
查看代碼才發現DiabloWorld-V1.6是使用firefly版本的，故從新找了份代碼gfirefly-anhei
關鍵是這麼久沒更新學習日誌是源於我的gfirefly沒有真正的安裝好。
之前的安裝完後，使用其期待的測試腳本測試時每次聯通上去就會立刻把客戶端踢掉。
```
Client 1 login in.
Client 1 login out.
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