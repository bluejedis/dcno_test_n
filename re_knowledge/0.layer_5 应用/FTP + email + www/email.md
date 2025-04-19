<div style="float: left; width: 64%; padding: 1%;">

# 电子邮件**E-mail** 

<ul>

## 电子邮件系统的组成结构  

<ul>

### 概述

<ul>

- 电子邮件是一种**异步**通信方式，通信时不**需要双方**  **同时在场**
- 电子邮件把邮件发送到收件人使用的邮件服务器，并放在其中的收件人邮箱中
- 收件人可以随时上网到自已使用的邮件服务器进行读取

</ul>

### 主要组成构件

<ul>

一个电子邮件系统应具有三个最主要的组成构件：
- 用户**代理**（User Agent）
- 邮件<b><span style="color: green;">S</span></b> (Mail Server)
- 电子邮件使用的<span style="color: orange;">协议</span>，如SMTP、POP3（或IMAP）等

#### pic

<ul>

  - ![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/dfcc3f07d050e1a4bd109677dfc892e5090689da8a858b59b160fa23ab313e71.jpg)  
图6.8电子邮件系统最主要的组成构件  

</ul>

#### 用户**代理**（UA）

<ul>

- 用户与电子邮件系统的接口
- 功能：
  - 向用户提供友好的接口来发送和接收邮件
  - 至少应当具有撰写、显示和邮件处理的功能
- 形式：
  - 通常是运行在PC上的程序（电子邮件客户端软件）
  - 常见的有Outlook和Foxmail等

</ul>

#### 邮件<b><span style="color: green;">S</span></b> (Mail Server)

<ul>

- 主要功能：
  - 发送和接收邮件
  - 向发件人报告邮件传送的情况（已交付、被拒绝、丢失等）
- 工作模式：
  - 以客户/服务器模式工作
  - 必须能够同时充当客户和服务器
  - 例如：
    - 当邮件服务器A向B发送邮件时，A是SMTP客户，B是SMTP服务器
    - 当B向A发送邮件时，B是SMTP客户，A是SMTP服务器

</ul>

>pro：邮件发送协议和读取协议的应用（2012）  

#### 邮件发送、读取<span style="color: orange;">协议</span>

<ul>

- 发送：
  - 用于用户代理向邮件服务器发送邮件或在邮件服务器之间发送邮件
  - 如SMTP
  - 使用"推"（Push）的通信方式
- 读取：
  - 用于用户代理从邮件服务器读取邮件
  - 如POP3
  - 使用"拉"（Pull）的通信方式

</ul>
</ul>

### email的收发过程

<ul>

#### pic

<ul>

- ![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/6ca073f4d9e5db6d02912d03369337bbc2dd68d517d1196365f94c02d9453f0b.jpg)  
图6.9电子邮件的发送、接收过程  

</ul>

#### 发送

<ul>

- 发件人调用用户代理来撰写和编辑要发送的邮件
- 点击"发送邮件"按钮后：
  - 用户代理用SMTP把邮件传送给发送端邮件服务器
  - 发送端邮件服务器将邮件放入邮件缓存队列中
  - 发送端邮件服务器与接收端建立TCP连接
  - 依次发送邮件缓存队列中的邮件

</ul>

#### 接收

<ul>

- SMTP服务器进程收到邮件后：
  - 将邮件放入收件人的用户邮箱
  - 等待收件人读取
- 收件人收信时：
  - 调用用户代理
  - 使用POP3（或IMAP）协议从邮件服务器取回邮件

</ul>
</ul>
</ul>

## 电子邮件格式与<b><span style="color: purple;">M</span></b>IME  

<ul>

### 电子邮件格式  

<ul>

#### 基本结构

<ul>

- 一个电子邮件分为信封和内容两大部分
- 邮件内容又分为首部和主体两部分
- RFC822规定了邮件的首部格式，而邮件的主体部分则让用户自由撰写
- 用户写好首部后，邮件系统自动地将信封所需的信息提取出来并写在信封上，用户不需要亲自填写信封上的信息

</ul>

#### 邮件首部格式

<ul>

- 邮件内容的首部包含一些首部行
  - 每个首部行由一个关键字后跟冒号再后跟值组成
  - 有些关键字是必需的，有些则是可选的
  - 最重要的关键字是To和Subject

##### To关键字

<ul>

- 是必填的关键字
- 后面填入一个或多个收件人的电子邮件地址
- 电子邮件地址的格式：
  - 收件人邮箱名 $@$ 邮箱所在主机的域名
  - 如abc@cskaoyan.com
  - abc cska oy an.com这个邮件服务器上必须是唯一的
  - 这也就保证了该邮件地址在整个因特网上是唯一的

</ul>

##### Subject关键字

<ul>

- 是可选关键字
- 是邮件的主题
- 反映了邮件的主要内容

</ul>

##### From关键字

<ul>

- 是必填的关键字
- 通常由邮件系统自动填入
- 首部与主体之间用一个空行进行分割

</ul>

##### 典型邮件内容示例

<ul>

- ![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/ad6c7d88b4818d5ccfd48b3f5f46a9fdfe4b14571fa005e2fce9eb9bd53a5b58.jpg)  

</ul>
</ul>
</ul>

### 多用途**M**ultipurpose因特网邮件扩展**I**nternet **M**ail **E**xtensions（MIME）  

<ul>

>pro：SMTP直接传输的内容（2018）  

#### MIME产生背景

<ul>

- SMTP只能传送7位ASCII码文本邮件
- 许多其他非英语国家的文字无法传送
  - 如中文、俄文
  - 甚至带重音符号的法文或德文
- 无法传送可执行文件及其他二进制对象

</ul>

#### MIME与SMTP关系

<ul>

- MIME**并未改动**SMTP或取代它
- 发送过程：
  - 当发送端发送的邮件中包含有非ASCII码数据时，不能直接使用SMTP进行传送
  - 要通过MIME进行转换，将非ASCII码数据转换为ASCII码数据
  - 之后，就可以使用SMTP进行传送
- 接收过程：
  - 接收端要使用MIME对接收到的ASCII码数据进行逆转换
  - 以便可以得到包含有非ASCII码数据的邮件

</ul>

![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/b50f6aad5d70911c62bdd8542a01a0e00833e19a2ac698dac6e472b48a6ca867.jpg)  
图6.10SMTP与MIME的关系  

#### MIME主要内容

<ul>

- 5个新的邮件首部字段
  - MIME版本
  - 内容描述
  - 内容标识
  - 传送编码
  - 内容类型
- 定义了许多邮件内容的格式，对多媒体电子邮件的表示方法进行了标准化
- 定义了传送编码，可对任何内容格式进行转换，而不会被邮件系统改变

</ul>
</ul>
</ul>

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
