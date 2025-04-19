<div style="float: left; width: 64%; padding: 1%;">


## ⚠️连接管理(3次握手、4次挥手)

<ul>

### TCP连接的基本概念

<ul>

- TCP是面向连接的协议
- 每个TCP连接都有三个阶段
  - 连接建立
  - 数据传送
  - 连接释放

</ul>

### TCP连接建立要解决的问题

<ul>

- 要使每一方能够确知对方的存在
- 要允许双方协商一些参数

</ul>

### TCP连接的特点

<ul>

- TCP连接的**端点**是**套接字**
- 每条TCP连接 唯一地被 **两个端点** **确定**
- 同一个IP地址可以有多个不同的TCP连接
- 同一个端口号可以出现在多个不同的TCP连接中
- TCP连接的建立采用客户/服务器模式
  - 主动发起连接建立的应用进程称为客户
  - 被动等待连接建立的应用进程称为服务器

</ul>

### TCP连接的建立  

<ul>

### TCP连接的**建立**-“三次握手”

<ul>

- ![image](https://bluejedis.github.io/picx-images-hosting/basic/image.41y3dmdsq7.webp)

- 过程：
  - **服务器**在连接建立前处于**LISTEN**（收听）状态，等待客户连接请求。

- 步骤：
   - 客户机发送连接请求：
     - 首部中的同步位 $\mathrm{{SYN}} = 1$。
     - 选择一个初始序号 ${\mathrm{seq}} = x$。
     - 进入SYN-SENT（同步已发送）状态。
  - 服务器收到连接请求并同意建立连接：
     - 发回确认报文段，$\mathrm{{SYN}} = 1$ 和 $\mathrm{{ACK}} = 1$。
     - 确认号 $\operatorname{ack} = x + 1$。
     - 选择自己的初始序号 ${\mathrm{seq}} = y$。
     - 进入SYN-RCVD（同步收到）状态。
  - 客户机收到确认后：
     - 发送确认报文段，$\mathrm{{ACK}} = 1$。
     - 确认号 $\mathsf{ack} = y + 1$。
     - 序号 ${\mathrm{seq}} = x + 1$。
     - 可以携带数据，若不携带数据则不消耗序号。
     - 进入ESTABLISHED（已建立连接）状态。

- 服务器收到客户机的确认后：
  - 也进入ESTABLISHED状态。

- 连接建立后：
  - 双方进入全双工通信状态，可以随时发送数据。
- pic
- ![image](https://bluejedis.github.io/picx-images-hosting/image.3yehbwb6vd.webp)
  ```mermaid
  sequenceDiagram
      participant Client
      participant Server
      Note over Server: LISTEN state
      
      Client->>Server: SYN=1, seq=x
      Note over Client: SYN-SENT state
      
      Server->>Client: SYN=1, ACK=1, seq=y, ack=x+1
      Note over Server: SYN-RCVD state
      
      Client->>Server: ACK=1, seq=x+1, ack=y+1
      Note over Client,Server: Both ESTABLISHED state
      
      Note over Client,Server: Full-duplex Communication
  ```

</ul>

</ul>

### TCP连接的**释放**-四次挥手

<ul>

#### steps

<ul>

##### pic

<ul>

- ![image](https://bluejedis.github.io/picx-images-hosting/basic/image.7pbuse7qv.webp)
图5.8用"四次挥手"释放TCP连接  
- 

```PlantUML
  @startuml
  ' 设置注释背景颜色
  skinparam note {
    BackgroundColor #ffffff
  }

  ' 定义参与者
  participant Client
  participant Server

  ' 添加注释并指定背景颜色
  note over Client, Server
    Active Connection
  end note

  Client -> Server : FIN=1, seq=u
  note over Client
    FIN-WAIT-1 state
  end note

  Server -> Client : ACK=1, seq=v, ack=u+1
  note over Server
    CLOSE-WAIT state
  end note
  note over Client
    FIN-WAIT-2 state
  end note

  note over Client, Server #f96
    Half-closed state
  end note

  Server -> Client : FIN=1, seq=w, ack=u+1
  note over Server
    LAST-ACK state
  end note

  Client -> Server : ACK=1, seq=u+1, ack=w+1
  note over Client
    TIME-WAIT state (2MSL)
  end note
  note over Server
    CLOSED state
  end note

  note over Client
    CLOSED state after 2MSL
  end note
  @enduml
```

</ul>

##### 第一步

<ul>

- 客户机打算关闭连接时：
  - 向其TCP发送连接释放报文段，并停止发送数据
  - 主动关闭TCP连接
  - 该报文段的终止位FIN置1
  - **序号** $seq=\!u$，等于前面已传送过的数据的最后一个字节的序号加1
  - FIN报文段即使不携带数据，也要消耗掉一个序号
  - 客户机进入FIN-WAIT-1（终止等待1）状态
- TCP是**全双工**的：
  - 可以想象为一条TCP连接上有两条数据通路
  - 发送FIN的一端不能再发送数据，即关闭了其中一条数据通路
  - 但对方还可以发送数据

</ul>

##### 第二步

<ul>

- 服务器收到连接释放报文段后：
  - 发出确认，**确认号** $ack=\!u+1$
  - 序号 ${\mathfrak{s e q}}\!=\!v$，等于它前面已传送过的数据的最后一个字节的序号加1
  - 服务器进入CLOSE-WAIT（关闭等待）状态
- 此时：
  - C → S 方向的连接 **释放**了
  - TCP连接处于<b><span style="color: green;">半</span><span style="color: orange;">关闭</span></b>状态
  - 服务器若发送数据，客户机仍要接收
- 客户机：
  - 收到来自服务器的确认后，进入FIN-WAIT-2（终正等待2）状态
  - 等待服务器发出的连接释放报文段

</ul>

> pro：TCP连接释放过程中状态的变化（2021）

##### 第三步

<ul>

- 若<span style="color: green;">sever</span>已经没有要向客户机发送的数据：
  - 通知TCP释放连接
  - 发出 $\mathrm{FIN}\!=\!1$ 的连接释放报文段
  - 报文段序号为 $w$（处于半关闭状态的服务器可能又发送了一些数据）
  - 重复发送上次已发送的确认号 $\operatorname{ack}\!=\!u\!+1$
  - 服务器进入LAST-ACK（最后确认）状态

</ul>

> pro：TCP连接释放的过程及状态变化的时间分析（2016、2022）

##### 第四步

<ul>

- 客户机收到连接释放报文段后：
  - 必须发出确认
  - 进入TIME-WAIT（时间等待）状态
  - 该报文段的确认位ACK置1
  - 确认号 $\operatorname{ack}\!=\!w+1$
  - 序号 $\scriptstyle{\mathrm{seq}}\,=\,u\,+\,1$
- <span style="color: green;">sever</span>：
  - 收到该确认报文段后就进入CLOSED（连接关闭）状态
- <span style="color: blue;">client</span>：
  - 进入TIME-WAIT状态后，还要经过时间等待计 2 MSL后，才进入CLOSED状态 ← just 规定
    - 2MSL：**2倍**Maximum segments lifetime（）
  - 若服务器收到连接释放请求后不再发送数据：
    - 从客户机发出FIN报文段时刻算起，客户机释放连接的最短时间为 $1\,\mathrm{RTT}+2\,\mathrm{MSL}$
    - 服务器释放连接的==最短==时间为1.5RTT

</ul>

</ul>

#### 保活计时器

<ul>

- TCP**设有**保活计时器：
  - 解决TCP双方建立连接后，客户主机突然故障的情况
  - **防止**服务器**一直等待**客户发来的数据

</ul>

#### ⚠️TCP连接建立和释放**总结**

<ul>

##### 建立连接（3步）

<ul>

- SYN=1,seq=**x**
  - SYN=1,ACK=1,seq=y,ack=**x+1**
- ACK=1,seq=**x+1**,ack=y+1

</ul>

##### 释放连接（4步）

<ul>

- **FIN**=1,seq=**u**
  - ACK=1,seq=v,ack=**u+1** (被)
  - **FIN**=1,ACK=1,seq=*w*,ack=**u+1**(被)
- ACK=1,seq=**u+1**,ack=*w+1*

选择题喜欢考查（关于连接建立和释放的题目，<span style="color: green;">ACK</span>、<span style="color: orange;">SYN</span>、**FIN**=**1**），请牢记。

</ul>

</ul>

</ul>

</ul>

## TCP可靠传输  

<ul>

- TCP提供可靠数据传输服务：
  - 在不可靠的**IP层**之上建立
  - 确保接收方读出的字节流与发送方发出的**字节流完全一致**

- TCP使用以下机制实现可靠性：
  - 检验：
    - 与UDP的检验机制相同
  - 序号：
    - 给每个字节分配序号，确保数据按序到达
  - 确认：
    - 接收方发送确认信息，告知发送方已成功接收哪些数据
  - 重传：
    - 发送方未在规定时间内收到确认，则重传数据

> pro: TCP的**确认机制**，**序号**和**确认号**的含义（2011、2012、2013）

### 序号  

<ul>

- TCP首部中的序号字段：
  - 作用是确保数据能按顺序提交给应用层。
  - TCP将数据视为一个无结构但有序的字节流。
  - 序号是针对传送的字节流而不是报文段。

- 数据流中的每个字节都有序号：
  - 序号字段值表示本报文段发送的数据的第一个字节的序号。
  - 举例说明：
    - 假设A和B建立了一条TCP连接。
    - A的发送缓存区有10个字节，序号从0开始。
    - 第一个报文段包含第0到第2个字节，则该TCP报文段的序号是0。
    - 第二个报文段的序号是3。

![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/c26ac704f59eca3c51a2c5c371f1336b60b64260c34e4d2227d63e9f9712d1c8.jpg)  
图5.9A的发送缓存区中的数据划分成TCP段  

</ul>

### 确认  

<ul>

- TCP首部的确认号字段：
  - 表示接收方期望收到的下一个报文段的数据的第一个字节的序号。
  - 举例说明：
    - 如果接收方B已经收到了第一个报文段的数据，那么B希望下一个报文段从第3个字节开始，则B发送给A的报文段中的确认号字段应为3。

- 发送方缓存区：
  - 会继续存储已发送但未收到确认的报文段，以便在必要时重传。

- TCP默认使用累积确认：
  - 只确认数据流中至第一个丢失字节为止的字节。
  - 举例说明：
    - 如果接收方B收到了包含字节0到2和字节6到7的报文段，但未收到字节3到5，那么B仍在等待字节3及其后面的字节。
    - 在这种情况下，B发送给A的下一个报文段将确认号字段置为3，表示确认至字节2，并期待字节3。

</ul>

### <span style="color: purple;">重传</span>  

<ul>

- 有两种事件会导致TCP对报文段进行重传：超时和余ACK。

#### <span style="color: orange;">超时</span>重传  

<ul>

- TCP协议工作原理：
  - 每发送一个报文段时，TCP会设置一个超时计时器。
  - 如果在计时器到期之前没有收到报文段的确认，TCP会重传该报文段。

- 互联网环境下的挑战：
  - 由于互联网中IP数据报的路由选择变化很大，导致传输层的往返时延（RTT）也有很大的方差。

- 超时计时器的自适应算法：
  - TCP记录报文段的发送时间和收到确认的时间，这两个时间差即为往返时间（RTT）。
  - TCP维护着一个加权平均的RTT值，称为RTTS，它会根据新的RTT样本值进行调整。
  - 超时计时器设置的重传时间（RTO）应略大于RTTS，但不宜过大，以确保在报文段丢失时TCP能够迅速重传，避免过大的数据传输时延。

</ul>

#### <span style="color: Violet;">冗余</span> ACK重传  

<ul>

##### 超时重传的缺陷

<ul>

- 超时触发重传存在的问题是超时周期通常很长

</ul>

#####  <span style="color: Violet;">冗余</span> ACK机制

<ul>

- 优势
  - 发送方通常可以在超时事件发生之前，通过检测冗余ACK来较好地识别丢包情况
- 定义
  - 冗余ACK是指对某个报文段进行**重复确认**的**ACK**，而发送方之前已经收到过该报文段的确认

</ul>

##### 工作过程示例

<ul>

- 场景设置
  - 发送方A发送了序号为1、2、3、4、5的TCP报文段，其中**2**号报文段在传输过程中**丢失**
- r方 行为
  - 由于2号报文段丢失，3、4、5号报文段对于接收方B来说是失序的
  - TCP规定，当接收方收到比期望序号大的失序报文段时
    - 会发送一个冗余ACK，指明下一个期望接收的字节序号
      - **3、4、5**号报文段到达B时，B发现它们不是期望接收的下一个报文段
      - 发送**3**个对1号报文段的**冗余ACK**
        - 表示期望接收2号报文段
- s方 响应
  - 当发送方A收到对同一个报文段的3个冗余ACK时
    - 可以判断2号报文段已经丢失，并立即对2号报文段进行重传
  - 这种技术称为 <span style="color: green;">快速</span><span style="color: purple;">重传</span>

</ul>

##### 应用范围

<ul>

- 冗余ACK不仅在丢包检测中使用，还在拥塞控制中发挥作用，这将在后续内容中讨论

</ul>

</ul>

</ul>

</ul>

</ul>


</div>
<div style="float: right; width: 26%; padding: 1%;">

</div>
<div style="clear: both;"></div>
