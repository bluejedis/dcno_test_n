<div style="float: left; width: 64%; padding: 1%;">

### <span style="color: orange;">停止</span>- <span style="color: GreenYellow;">等待</span><span style="color: green;">流量</span><span style="color: Gold;">控制</span>   

<ul>

- 停止-等待流量控制是一种最简单的流量控制方法
- 基本过程：
  - 发送方每次只充许发送一个帧
  - 接收方每接收一个顿都要反馈一个应答信号，表示可以接收下一帧
  - 发送方收到应答信号后才能发送下一顿
  - 若发送方没有收到接收方反馈的应答信号，则需要一直等待
- 发送方每发送完一个帧，就进入等待接收方确认信息的过程中，因而传输效率很低

</ul>


</div>
<div style="float: right; width: 26%; padding: 1%;">

</div>
<div style="clear: both;"></div>
