安裝：
1. 系統
```
Distributor ID: Ubuntu
Description:    Ubuntu 16.04.1 LTS
Release:        16.04
Codename:       xenial
```
2. sudo easy_install gfirefly
**error:**
```
******************************************
Configure: Autodetecting ZMQ settings...
    Custom ZMQ dir:       None
detect/vers.c:3:17: fatal error: zmq.h: 没有那个文件或目录
compilation terminated.
Failed with default libzmq, trying again with /usr/local
******************************************
Configure: Autodetecting ZMQ settings...
    Custom ZMQ dir:       /usr/local
detect/vers.c:3:17: fatal error: zmq.h: 没有那个文件或目录
compilation terminated.
error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
Fatal: 
    Failed to compile ZMQ test program.  Please check to make sure:

    * You have a C compiler installed
    * A development version of Python is installed (including header files)
    * A development version of ZMQ >= 2.1.4 is installed (including header files)
    * If ZMQ is not in a default location, supply the argument --zmq=<path>
    * If you did recently install ZMQ to a default location, 
      try rebuilding the ld cache with `sudo ldconfig`
      or specify zmq's location with `--zmq=/usr/local`
    
******************************************
******************************************
error: Setup script exited with 1
```
解決方案：
sudo apt-get install libzmq-dev
3. 出現鏈接上去馬上被服務器斷開：
2016-09-05 16:40:19+0800 [-] Client 0 login in.[127.0.0.1,51242]
2016-09-05 16:40:19+0800 [-] Client 0 login out.
之前一直以為是代碼寫錯，以致棄游，后經同事提醒，其實是沒安裝好，gevent版本過高（1.1.1）
果斷卸載之，裝上1.0.2，
卸載：
sudo pip uninstall gevent
安裝：
sudo easy_install gevent==1.0.2

剛是第二次在另一台機器安裝gfirefly，又發現其實早就應該知道安裝有誤，不用等到客戶端測試的，在啟服務器時就出問題了
2016-09-05 16:39:38+0800 [-] Log opened.
2016-09-05 16:39:38+0800 [-] Log opened.
2016-09-05 16:39:38+0800 [-] [gate] started...
2016-09-05 16:39:38+0800 [-] [gate] pid: 32402
**2016-09-05 16:39:38+0800 [-] node [0] lose**
2016-09-05 16:39:38+0800 [-] Log opened.
2016-09-05 16:39:38+0800 [-] [net] started...
2016-09-05 16:39:38+0800 [-] [net] pid: 32405
**2016-09-05 16:39:38+0800 [-] node [1] lose**
2016-09-05 16:40:19+0800 [-] Client 0 login in.[127.0.0.1,51242]
2016-09-05 16:40:19+0800 [-] Client 0 login out.

node剛起就lose了。


