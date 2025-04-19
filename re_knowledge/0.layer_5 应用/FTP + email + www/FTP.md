<div style="float: left; width: 64%; padding: 1%;">
# 文件传输协议(**FTP**)  

<ul>

## 工作原理

<ul>

### 基本功能与特点

<ul>

- 文件传输协议（FileTransferProtocol，FTP）是因特网上使用得最广泛的文件传输协议
- FTP提供交互式的访问，允许**客户** **指明**文件的<span style="color: orange;">类型</span>与<span style="color: lightblue;">格式</span>，并允许文件具有<b><span style="color: green;">存取</span></b>权限
- 它屏蔽了各计算机系统的细节，因而适合于在异构网络中的任意计算机之间传送文件
- FTP提供以下功能：
  -  提供不同种类主机系统（硬、软件体系等都可以不同）之间的文件传输能力
  -  以用户权限管理的方式提供用户对远程FTP服务器上的文件管理能力
  -  以匿名FTP的方式提供公用文件共享的能力

</ul>

>pro：FTP在传输层所使用的协议（2009、2018）  
<details>
<summary>TCP</summary>
FTP在传输层所使用的协议是TCP（传输控制协议）。
FTP依赖于TCP来提供可靠的、面向连接的服务。TCP确保了FTP数据传输的**可靠性**和顺序性，而FTP则利用TCP的这一特性来实现文件的上传和下载功能。
</details>

### 工作方式

<ul>

- FTP采用<b><span style="color: blue;">C</span></b>/<b><span style="color: green;">S</span></b>的工作方式，使用**TCP可靠**的传输服务
- 一个FTP服务器进程可同时为多个客户进程提供服务
- FTP的服务器进程由两大部分组成：
  - 一个主进程，负责接收新的请求
  - 另外有若干从属进程，负责处理单个请求

</ul>

#### 工作步骤

<ul>

- 打开熟知端口21（**控制**端口），使客户进程能够连接上
- 等待客户进程发连接请求
- 启动从属进程处理客户进程发来的请求
  - 从属进程对客户进程的请求处理完毕后即终止
- 回到等待状态，继续接收其他客户进程的请求
  - 主进程与从属进程是并发执行的

</ul>

#### 状态信息

<ul>

- FTP服务器必须在**整个会话期间**保留用户的状态信息
- 特别是服务器必须：
  - 把指定的用户账户与控制连接联系起来
  - 服务器必须追踪用户在远程目录树上的当前位置

</ul>
</ul>

### 控制连接与数据连接

<ul>

>pro：控制连接和数据连接的特点（2017、2023）  

#### port

<ul>

- FTP在工作时使用两个并行的TCP连接：
  - <span style="color: orange;">控制</span>连接（服务器端口号21）
  - <span style="color: darkblue;">数据</span>连接（服务器端口号20）
- 使用两个不同的端口号可以使协议更容易实现

- ![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/c1f0808dc3aeb3e8fa2e341b8a51d60ebf4df40ec50c263cab6b38816315d50f.jpg)  
图6.7控制连接和数据连接  

</ul>

#### 控制连接

<ul>

>pro：控制连接的作用（2009）  

- 服务器监听**21**号端口，等待客户连接
- 建立在这个端口上的连接称为控制连接，用来**传输** <b><span style="color: blue;">控制info</span></b>
- 控制连接特点：
  - FTP <b><span style="color: blue;">C</span></b>发出的传送请求through~ → <b><span style="color: green;">S</span></b>端的控制进程
  - 控制连接并**不**用来**传送文件**
  - 在**传输文件时**还可以使用~
  - ~在整个会话期间一直保持打开状态

</ul>

#### 数据连接

<ul>

##### 基本工作流程

<ul>

-  <b><span style="color: green;">S</span></b>端的控制进程 在接收到FTP客户发送来的文件传输请求后：
   - 创建"数据传送 <b><span style="color: orange;">进程</span></b>"和"数据 <b><span style="color: green;">连接</span></b>"
     - 数据 <b><span style="color: green;">连接</span></b> ：连接 <b><span style="color: blue;">C</span></b>和<b><span style="color: green;">S</span></b>端的数据传送 <b><span style="color: orange;">进程</span></b>
     - 数据传送 <b><span style="color: orange;">进程</span></b>  **实际**完成 文件的传送
   - 在传送完毕后关闭"数据传送连接"并结束运行

</ul>

##### 传输模式

<ul>

- 数据连接有两种传输模式：
  - <b><span style="color: orange;">主动</span></b>模式 P**ORT**
  - <b><span style="color: blue;">被动</span></b>模式 P _ASV_

###### PORT模式工作原理

<ul>

- 客户端连接到服务器的21端口
- 登录成功后要读取数据时：
  - <b><span style="color: blue;">C</span></b>端随机开放一个端口，并发送命令告知服务器
  - 服务器收到PORT命令和端口号后，通过20端口和客户端开放的端口连接，发送数据

</ul>

###### PASV模式工作原理

<ul>

- 客户端要读取数据时：
  - 发送PASV命令→<b><span style="color: green;">S</span></b>
    - <b><span style="color: green;">S</span></b>在本地随机开放一个端口，并告知客户端
  - 客户端再连接到服务器开放的端口进行数据传输

</ul>

> attention:  
很多教材并未介绍这两种模式，如无特别说明可**默认**为采用**主动**模式。  

</ul>
</ul>
</ul>

### 其他特点

<ul>

- 因为FTP使用了一个分离的控制连接，所以也称FTP的控制信息是带外（Out-ofband）传送的
- 使用FTP的局限性：
  - 要修改服务器上的文件，需要先将此文件传送到本地主机
  - 然后将修改后的文件副本传送到原服务器，来回传送耗费很多时间
- 网络文件系统（NFS）的优势：
  - 允许进程打开一个远程文件
  - 能在该文件的某个特定位置开始读写数据
  - 可使用户只复制一个大文件中的一个很小的片段，而不需要复制整个大文件

</ul>
</ul>
</ul>

</div>
<div style="float: right; width: 26%; padding: 1%;">

</div>
<div style="clear: both;"></div>
