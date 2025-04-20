<div style="float: left; width: 64%; padding: 1%;">

在数据链路层中，流量控制机制和可靠传输机制是交织在一起的。  


### <span style="color: green;">流量</span>  <span style="color: Gold;">控制</span>overview

<ul>

- 流量控制是指由接收方控制发送方的发送速率，使接收方有足够的缓冲空间来接收每个帧
- 常见的流量控制方法有两种：停止-等待协议和滑动窗口协议
- 数据链路层和传输层均有流量控制的功能，它们都用到了滑动窗口协议，但也有所区别，主要体现如下：  
  - 数据链路层控制的是相邻结点之间的流量，而传输层控制的是端到端的流量
  - 数据链路层的控制手段是接收方收不下就不返回确认。传输层的控制手段是接收方通过确认报文段中的窗口值来调整发送方的发送窗口

</div>
<div style="float: right; width: 26%; padding: 1%;">

</div>
<div style="clear: both;"></div>
