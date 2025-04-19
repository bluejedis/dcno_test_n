<div style="float: left; width: 64%; padding: 1%;">


## TCP<span style="color: green;">流量</span>控制  

<ul>

### 基本概念

<ul>

- 流量控制的功能就是让发送方的发送速率不要太快，以便让接收方来得及接收，因此可以说流量控制是一个速度匹配服务（匹配发送方的发送速率与接收方的读取速率）

</ul>

### 实现机制

<ul>

#### TCP<span style="color: green;">滑动</span>窗口

<ul>

- TCP使用滑动窗口sw 机制进行流量控制：
  - 这个机制在第3章中已经介绍过其基本原理。

- 流量控制的目的：
  - 确保发送方不会发送超过接收方处理能力的报文量。

- 实现方式：
  - 接收方维护一个**接收窗口**（rwnd），它表示接收方当前可接收的数据量。
    - 接收窗口的**大小** ← 接收方的接收缓存大小决定，并动态调整。
    - 接收方通过TCP报文段首部的"窗口"字段通知发送方其接收窗口的大小。
  - 发送方的发送窗口大小不能超过接收方提供的接收窗口值，这样可以避免发送方发送过快，导致接收方处理不过来。

- 结果：
  - 这种方式<span style="color: green;">限制</span>了**发送方**发送数据的**速率**，从而实现流量控制。

</ul>

> pro：利用接收窗口实现流量控制的过程（2016、2021）

#### 流量控制process

<ul>

- 图5.10说明了如何利用滑动窗口机制进行流量控制
  - 接收方B
    - 可通过设置确认报文段首部中的窗口字段来将rwnd通知给A
      - **rwnd**即**接收方** 允许**连续接收**的**能力**
        - 单位是字节
  - 发送方A
    - 总是**根据**最新收到的**rwnd**值来限制自己发送窗口的大小
      - 保证A不会使B的接收缓存溢出
- process
  - 连接建立时，B告诉A："我的接收窗口rwnd $=4000$"
  - 接收方B进行了**三次流量控制**
    - 第一次把窗口减到rwnd $=300$
    - 第二次又减到rwnd $=100$
    - 最后减到rwnd $=\!0$

- ![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/2ea4a8c799f964a7e96572594c00edii4f1536d705a7e0ede4d1ac19178b9e9412.jpg)  
图5.10利用可变窗口进行流量控制举例  

</ul>

#### <span style="color: green;">持续</span>计时器机制

<ul>

- TCP为每个连接设有一个持续计时器
  - 发送方 收到对方的**零窗口通知** ← **启动**持续计时器
  - 计时器**超时** → 发送零窗口**探测报文**段
    - 对方在**确认**探测报文段时 → 给出现在的窗口值
- 若窗口仍为零，发送方收到确认后重新设置持续计时器

</ul>

</ul>

### 与<span style="color: blue;">数据链路层</span>流量控制的区别

<ul>

- 实现**范围**不同
  - 数据链路层：两个中间的相邻**结点**之间
  - 传输层：**端**到**端**，两个进程之间
- **窗口特性**不同
  - 数据链路层：**窗口大小** **不能动态变化**
  - 传输层：~ **可以**~

</ul>

</ul>

## TCP<span style="color: orange;">拥塞</span>控制  

<ul>

### 基本概念

<ul>

- 拥塞控制是指防止过多的数据注入网络，保证网络中的路由器或链路不致过载
- 出现拥塞时，端点并不了解拥塞发生的细节
- 对通信的端点来说，拥塞往往表现为通信时延的增加

</ul>

### 与流量控制的区别

<ul>

#### 控制范围

<ul>

- 拥塞控制
  - 全局性过程
  - 涉及所有主机、路由器及相关因素
- 流量控制
  - 点对点通信量控制
  - 端到端问题

</ul>

#### 相似之处

<ul>

- 都通过控制发送方发送数据的速率来达到控制效果

</ul>

#### 应用场景示例

<ul>

- 高速链路场景
  - 链路速率：$10\mathrm{{Gb}}/s$
  - 大型机向PC传送：1Gb/s
  - 需要流量控制而非拥塞控制
- 多用户场景
  - 100万台PC同时传送：每台1Mb/s
  - 需要考虑网络负载承受能力

</ul>

</ul>

### 拥塞控制算法

<ul>

- TCP有四种拥塞控制算法
  - 慢开始
  - 拥塞避免
  - 快重传
  - 快恢复

</ul>

### 拥塞控制机制

<ul>

#### 窗口控制

<ul>

- 发送方需维持 **拥塞**窗口（cwnd）
- 拥塞窗口大小取决于网络拥塞程度
- 动态变化原则
  - 网络未拥塞：增大窗口
  - 网络出现拥塞：减小窗口

</ul>

#### 发送窗口确定

<ul>

- 发送窗口上限值计算：
  - 发送窗口的上限值 $=$ min[rwnd, cwnd]
- 影响因素说明
  - 接收窗口通过TCP报文首部窗口字段通知
  - 拥塞窗口由网络拥塞程度决定

</ul>

#### 说明

<ul>

- 假设条件
  - 数据为单方向传送，对方只传送确认报文
  - 接收方有足够大的缓存空间
  - 发送窗口大小由网络拥塞程度决定
- 度量单位
  - 采用 **最大报文段长度** MSS 作为拥塞窗口大小的单位

</ul>

</ul>

### 慢开始和拥塞避免  

<ul>

#### <span style="color: orange;">慢</span>开始  

<ul>

##### 基本思路与方法

<ul>

- 当发送方刚开始发送数据时，因为并不清楚网络的负荷情况，若立即把大量数据注入网络，则有可能引发网络拥塞
- 具体方法是：
  - 先发送**少量**数据**探测**一下，若没有发生拥塞
    - 则适当增大拥塞窗口
  - 即由小到大逐渐增大拥塞窗口（即发送窗口）

</ul>

> pro：慢开始算法的实现过程（2014、2015）

##### 实现过程

<ul>

- A向B发送数据，发送方先令cwnd $=1$ ，即一个MSS
- A发送第一个报文段，A收到B对第一个报文段的确认后，把cwnd从1增大到2
- A接着发送两个报文段，A收到B对这两个报文段的确认后，把cwnd从2增大到4，下次就可一次发送4个报文段
- 
  ```mermaid
    sequenceDiagram
      participant A
      participant B
      Note over A: cwnd = 1 MSS
      A->>B: Send 1 segment
      B->>A: ACK
      Note over A: cwnd = 2 MSS
      A->>B: Send 2 segments
      B->>A: ACK
      Note over A: cwnd = 4 MSS
      Note over A: Ready to send 4 segments
  ```

</ul>

##### 特点说明

<ul>

- 慢开始的"慢"并不是指拥塞窗口cwnd的增长速率慢，而是指在TCP开始发送报文段时先设置cwnd $=1$
  - 每经过一个传输轮次（即往返时延RTT），cwnd就会加倍，即cwnd的值随传输轮次指数增长
  - 为防止cwnd增长过大而引起网络拥塞，需要设置一个慢开始门限ssthresh（网值）
    - 当慢开始一直把cwnd增大到一个规定的ssthresh时 → 拥塞避免算法

</ul>

</ul>

#### 拥塞<span style="color: green;">避免</span>算法  

<ul>

> pro：慢开始和拥塞避免算法的实现过程/慢开始门限的作用（2017、2020、2023）

##### 基本思路

<ul>

- 让**拥塞窗口**cwnd**缓慢增大**
- 每经过一个往返时延RTT就把发送方的拥塞窗口cwnd加1，而不是加倍
- 使拥塞窗口cwnd按线性规律缓慢增长（即加法增大）

</ul>

##### 算法执行规则

<ul>

- 当cwnd$<$ssthresh时 → 慢开始算法
- 当cwnd $>$ ssthresh时，停止使用慢开始算法而改用拥塞避免算法
- 当cwnd $=$ ssthresh时，既可使用慢开始算法，又可使用拥塞避免算法（通常做法）

</ul>

</ul>

#### 网络拥塞的处理  

<ul>

##### 处理方法

<ul>

- 无论在慢开始阶段还是在拥塞避免阶段，只要发送方**判断** **网络**出现**拥塞**：
  - 首先把 慢开始**门限** **ssthresh**设置为
    - **出现拥塞时**的**发送方**的cwnd值的一半（但不能小于2）
  - 然后把**拥塞窗口**cwnd重新设置为1
  - 执行慢开始算法

*减小ssthresh，重新开始慢开始

</ul>

> pro：慢开始和拥塞避免阶段的平均传输速率分析（2016、2023）

##### 实现过程示例

<ul>

- 初始时：
  - 拥塞窗口置为1，即cwnd $=1$
  - 慢开始门限置为16，即ssthresh $=16$

![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/a1450fb7a0a2a7cbc01c8a1dcf0c026c45cb4c81db6c5a4ba5ff6ac97202f4bd.jpg)  
图5.11慢开始和拥塞避免算法的实现过程  

</ul>

> pro：慢开始/拥塞避免阶段拥塞窗口的变化分析（2016、2023）

##### 窗口变化过程

<ul>

- 慢开始阶段：
  - 发送方**每**收到一个对新报文段的确认**ACK**，就把拥塞窗口**cwnd+1**
    - 经过每个传输轮次（RTT），cwnd呈<span style="color: blue;">指数</span>规律增长
  - 当cwnd增长到慢开始门限ssthresh时（即当cwnd $=16$ 时），改用拥塞避免算法
    - cwnd按<span style="color: orange;">线性</span>规律增长

</ul>

> pro：当网络超时时，慢开始和拥塞避免算法的实现过程（2009、2022）

##### <span style="color: orange;">超时</span>处理

<ul>

- 当cwnd $=24$ 时，网络出现超时：
  - 调整ssthresh值为12（即为超时时cwnd值的一半）
  - cwnd置为1
  - 执行慢开始算法
  - 当cwnd $=12$ 时，改为执行拥塞避免算法

</ul>

> attention:

##### 注意事项

<ul>

- 在慢开始阶段：
  - 若2cwnd $>$ ssthresh，RT T cw nd s s thresh,而不等于2cwnd
  - 第16个轮次时cwnd $=8$ 、ssthresh $=12$ ，则第17个轮次时cwnd $=12$ ，而不等于16

</ul>

##### 算法特点

<ul>

- 使用了"乘法减小"和"加法增大"方法：
  - "**乘法减小**"：
    - 出现超时时，把ssthresh设置为当前拥塞窗口的一半
    - 网络频繁出现拥塞时，ssthresh值快速下降
  - "**加法增大**"：
    - 执行拥塞避免算法后，每个RTT后cwnd增加一个MSS大小
      - RTT（Round-Trip Time，往返时延）
    - 使拥塞窗口**缓慢增大**

</ul>

##### 拥塞避免的局限性

<ul>

- 拥塞避免并不能完全避免拥塞
- 拥塞避免是指在拥塞避免阶段把拥塞窗口控制为按线性规律增长

</ul>

</ul>

</ul>

### <span style="color: green;">快<span style="color: purple;">重传</span><span style="color: gray;">和</span>快恢复  

<ul>

#### 背景介绍

<ul>

- 个别报文段在网络中丢失时，网络可能并未发生拥塞
  - 发送方未收到确认会产生超时，误认为网络发生拥塞
    - 错误启动慢开始算法会降低传输效率
- 快重传算法可让发送方尽早知道个别报文段的丢失

</ul>

#### <span style="color: green;">快<span style="color: purple;">重传</span>  

<ul>

> pro：快重传算法的原理、重传的时机（2019）

##### 基本原理

<ul>

- 使<span style="color: blue;">sender</span>尽快进行重传，不等超时计时器超时
- <span style="color: green;">receiver</span>要求：
  - **不要等待**自已发送数据时才进行捐带确认
  - **立即发送**确认
    - 收到失序报文段也要立即发出对已收到报文段的重复确认
- 发送方收到**3个**冗余**ACK** → 立即重传相应报文段

</ul>

</ul>

#### <span style="color: green;">快恢复  

<ul>

##### 算法原理

<ul>

- 发送方连续收到3个允余ACK时：
  - 执行"乘法减小"MD方法
    - 把ssthresh调整为当前cwnd的一半
      - 把cwnd值调整为当前cwnd的一半
  - 开始执行拥塞避免算法

</ul>

##### 特点

<ul>

- **跳过了**拥塞窗口cwnd从1起始的**慢开始**过程
- **直接**进入**拥塞避免**阶段

![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/62dd33f004450128a3f441728d804d8b3a69264acb169f32cceb123861070b61.jpg)  
图5.12快恢复算法的实现过程  

</ul>

</ul>

#### 算法应用总结

<ul>

- TCP**连接建立**和网络出现**超时**时：
  - 采用<span style="color: orange;">慢</span>开始  和拥塞<span style="color: green;">避免</span>算法
  - ssthresh = cwnd/2，cwnd $=1$
- 发送方收到3个冗余ACK时：
  - 采用<span style="color: green;">快<span style="color: purple;">重传</span><span style="color: gray;">和</span>快恢复 
  - ssthresh $=$ cwnd/2，cwnd $=$ ssthresh

</ul>

#### 发送窗口swnd控制

<ul>

- 流量控制：
  - <span style="color: blue;">sender</span>发送数据的量 ←  <span style="color: green;">receiver</span>决定
- 拥塞控制：
  - <span style="color: blue;">sender</span>自己通过检测网络状况来决定
- swnd大小：
  - 由流量控制和拥塞控制共同决定
  - 取决于rwnd和cwnd中**较小的值**

</ul>

</ul>

</ul>


</div>
<div style="float: right; width: 26%; padding: 1%;">

</div>
<div style="clear: both;"></div>
