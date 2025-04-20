<div style="float: left; width: 64%; padding: 1%;">

### 边界网关Boundary gateway协议（BGP）

<ul>

> **pro：BGP的作用（2013）**

#### BGP的基本概念

<ul>

- 边界网关协议（Border Gateway Protocol，BGP）AS信息的协议，是一种外部网关协议
- 边界网关协议BGP常用于互联网的网关之间

</ul>

#### BGP的环境特点

<ul>

- 内部网关协议主要是设法使数据报在一个AS中尽可能有效地从源站传送到目的站
- 在一个AS内部也不需要考虑其他方面的策略
- 然而BGP使用的环境却不同，主要原因如下：
  - 互联网的规模太大，使得AS之间路由选择非常困难，每个主干网路由器表中的项目数都非常庞大
  - AS之间的路由选择必须考虑政治、安全或经济等有关因素

</ul>

#### BGP的工作原理

<ul>

##### BGP的基本特征

<ul>

- BGP只能是力求寻找一条能够到达目的网络且比较好的路由（不能兜圈子），而并非要寻找一条最佳路由
- BGP采用的是路径向量路由选择协议，它与距离向量协议（如RIP）和链路状态协议（如OSPF）都有很大的区别
- BGP是应用层协议，它是基于TCP的

</ul>

##### BGP的运行过程

<ul>

1. 配置BGP时，每个AS的管理员要选择至少一个路由器，作为该AS的"BGP发言人"BGP发言人往往就是BGP边界路由器

> **pro：封装BGP报文所采用的协议（2013、2017）**

2. 一个BGP发言人与其他AS中的BGP发言人要交换路由信息：
   - 先建立TCP连接
   - 然后在此连接上交换BGP报文以建立BGP会话
   - 再利用BGP会话交换路由信息
   - 使用TCP连接交换路由信息的两个BGP发言人，彼此成为对方的邻站或对等站
   - 每个BGP发言人除了必须运行BGP外，还必须运行该AS所用的内部网关协议，如OSPF或RIP

![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/4ab8772ba2216b0083326b701c09c66e732cf291ac3af19cc38f7fdaebe5ed2b.jpg)
图4.18BGP发言人和自治系统AS的关系示意图

3. BGP所交换的网络可达性信息：
   - 就是要到达某个网络所要经过的一系列自治系统
   - 当BGPP发言人互相交换网络可达性的信息后，各BGP发言人就根据所用的策略，从收到的路由信息中找出到达各自治系统的较好路由

![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/8f8fe0ecd96d6202cbd624e068791f7ff2d406d6b61dd7bf65606f87db5e3929.jpg)
图4.19主干网与自治系统间路径向量的交换

</ul>

</ul>

#### BGP的特点

<ul>

- BGP交换路由信息的结点数量级是AS个数的数量级，这要比这些AS中的网络数少很多
- 寻找一条较好的路径，取决于找准正确的BGP发言人，而每个AS中BGP发言人（或边界路由器）的数目是很少的。这样就使得AS之间的路由选择不致过分复杂
- BGP支持CIDR，thusBGP的路由表也就应当包括目的网络前缀、下一跳路由器，以及
- 当BGP刚运行时，BGP的邻站交换整个BGP路由表。但以后只需要在发生变化时更新有变化的部分。这样做对节省网络带宽和减少路由器的处理开销方面都有好处

</ul>

#### BGP的报文类型

<ul>

- BGP-4共使用4种报文：
  - 打开（Open）报文：用来与相邻的另一个BGP发言人建立关系，使通信初始化
  - 更新（Update）报文：用来通知某一路由的信息，以及列出要撤销的多条路由
  - 保活（Keepalive）报文：用来周期性地证实邻站的连通性
  - 通知（Notification）报文：用来发送检测到的差错

</ul>

#### BGP的通信过程

<ul>

- 建立邻站关系：
  - BGP发言人向对方发送Open报文
  - 对方接受则用Keepalive报文响应
- 维持邻站关系：
  - 两个BGP发言人彼此要周期性地交换Keepalive报文（一般每隔30秒）
  - Keepalive报文只有19B，thus不会造成网络上太大的开销
- 路由更新：
  - Update报文是BGP的核心内容
  - BGP发言人可以用Update报文撤销它曾经通知过的路由，也可以宣布增加新的路由

表4.6三种路由协议的比较 ![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/15cd3d3b0e07729275343dbe5d0888070cbc40ba2780a33c5736517ae359032a.jpg)

</ul>

</ul>

</ul>

</div>
<div style="float: right; width: 26%; padding: 1%;">

</div>
<div style="clear: both;"></div>
