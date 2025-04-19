<div style="float: left; width: 64%; padding: 1%;">


## <b><span style="color: orange;">S</span></b>MTP和<span style="color: blue;">P</span>OP3  

<ul>

>pro：  SMTP和POP3在传输层所使用的服务（2015、2018）  
<details>
<summary> **TCP**</summary>
<p>
SMTP（简单邮件传输协议）和POP3（邮局协议版本3）都是在TCP/IP协议栈的应用层运行的协议，它们分别用于电子邮件的发送和接收。然而，当涉及到传输层时，这两个协议所使用的服务有所不同：

SMTP：
SMTP在传输层使用的是TCP（传输控制协议）服务。
TCP提供了一种可靠的、面向连接的传输服务，确保数据包的顺序传输和错误检测/恢复。
SMTP利用TCP的这些特性来确保电子邮件消息能够从发送方的邮件服务器可靠地传输到接收方的邮件服务器。
SMTP通常使用TCP端口25进行通信。
POP3：
POP3同样在传输层使用TCP服务。
与SMTP类似，POP3也依赖于TCP的可靠性和顺序传输特性。
POP3允许用户从邮件服务器上下载邮件到本地计算机。
POP3通常使用TCP端口110进行通信。
总结来说，SMTP和POP3在传输层都使用TCP服务来保证电子邮件的可靠传输。TCP的面向连接和可靠性特性对于确保邮件服务的正常运行至关重要。
</p></details>

### SMTP和POP3在传输层所使用的服务

<ul>

- SMTP和POP3都是基于TCP连接的
  - SMTP使用TCP的25号端口
  - POP3~110号端口

</ul>

### <b><span style="color: orange;">S</span></b>MTP  

<ul>

>pro：  SMTP的用途及特点（2013、2014）  

#### 基本概念

<ul>

- 简单邮件传输协议（Simple Mail Transfer Protocol，SMTP）
  - 控制 两个**相互通信**的<b><span style="color: orange;">S</span></b>MTP进程 交换信息
- 采用<span style="color: blue;">C</span></b>/<b><span style="color: green;">S</span></b>模式工作：
  - 发送邮件的<b><span style="color: orange;">S</span></b>MTP进程 → SMTP<span style="color: blue;">C</span></b>
  - 接收邮件~ → <b><span style="color: green;">S</span></b>

</ul>

#### SMTP通信阶段

<ul>

##### 连接建立

<ul>

- 发件人的邮件发送到发送方邮件服务器的邮件缓存中后：
  - SMTP客户就每隔一定时间对邮件缓存扫描一次
  - 发现有邮件就与接收方邮件服务器的SMTP服务器建立TCP连接
  - SMTP服务器使用的熟知端口号为25
- 连接建立后：
  - 接收方SMTP服务器发出220Serviceready（服务就绪）
  - SMTP客户向SMTP服务器发送HELO命令，附上发送方的主机名
- SMTP**连接特点**：
  - 不使用中间的邮件服务器
  - TCP连接总是在发送方和接收方这两个邮件服务器之间直接建立
  - 当接收方邮件服务器故障时，发送方只能等待一段时间后再次尝试连接

</ul>

##### 邮件传送

<ul>

- 连接建立后开始传送邮件：
  - 从MAIL命令开始，包含发件人地址
  - SMTP服务器准备好接收邮件后回答250OK
- RCPT命令：
  - 格式为RCPTTO：<收件人地址>
  - 每发送一个RCPT命令都有相应信息返回
  - 作用是确认接收方系统准备状态
- DATA命令：
  - 表示开始传送邮件内容
  - SMTP返回354 Start mail input
  - 可开始传送邮件内容
  - 用<CRLF>.<CRLF>表示结束

</ul>

##### 连接释放

<ul>

- 邮件发送完毕后：
  - SMTP客户发送QUIT命令
  - SMTP服务器返回221（服务关闭）
  - TCP连接释放，邮件传送结束

</ul>

##### pic

<ul>

- ![SMTP](https://bluejedis.github.io/picx-images-hosting/SMTP.2doqcgsxfj.png)
- 
  ```mermaid
  sequenceDiagram
      participant Client as SMTP Client
      participant Server as SMTP Server

      Note over Client,Server: Connection Establishment
      Server->>Client: 220 Service ready
      Client->>Server: HELO (hostname)

      Note over Client,Server: Mail Transfer
      Client->>Server: MAIL FROM: <sender address>
      Server->>Client: 250 OK
      Client->>Server: RCPT TO: <recipient address>
      Server->>Client: 250 OK
      Client->>Server: DATA
      Server->>Client: 354 Start mail input
      Client->>Server: Mail content
      Client->>Server: <CRLF>.<CRLF>

      Note over Client,Server: Connection Release
      Client->>Server: QUIT
      Server->>Client: 221 Service closing

  ```

</ul>
</ul>
</ul>

### <span style="color: blue;">P</span>OP3<span style="font-size: 14px;"> Post Office Protocol 3</span>和IM<span style="color: darkred;">A</span>P<span style="font-size: 14px;"> Internet Message Access Protocol </span> 

<ul>

即 邮局协议的第3个版本
- 规定**个人**计算机如何连接到互联网上的邮件服务器进行收发邮件

互联网消息访问协议
- 邮件获取协议
- 允许用户
  - 从邮件服务器上获取邮件的信息，下载邮件等
- 与POP3协议相比
  - 用户可以在不同的设备上访问和操作服务器上的邮件
  - 无需先将邮件下载到本地设备

#### POP3

<ul>

- 邮局协议特点：
  - 是简单但功能有限的邮件读取协议
  - 现在使用的版本是POP3
  - 采用客户/服务器模式
  - 在传输层使用TCP，端口号为110
- 工作方式：
  - "下载并保留"：邮件保存在服务器上**可再次读取**
  - "下载并删除"：邮件**读取后**从服务器**删除**

</ul>

#### IMAP

<ul>

- 因特网报文存取协议特点：
  - 比POP复杂
  - 提供创建文件夹、移动邮件等联机命令
  - IMAP服务器维护会话用户状态信息
  - 允许用户代理只获取报文部分内容

</ul>

#### 基于万维网的电子邮件

<ul>

- 特点：
  - 如Hotmail、Gmail等
  - 用户浏览器与邮件服务器间使用HTTP
  - 不同邮件服务器间传送才使用SMTP

</ul>
</ul>
</ul>
</ul>

</div>
<div style="float: right; width: 26%; padding: 1%;">

</div>
<div style="clear: both;"></div>
