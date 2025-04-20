<div style="float: left; width: 64%; padding: 1%;">

###  <span style="color: GreenYellow;">单</span>帧<span style="color: GreenYellow;">滑动</span><span style="color: LightSkyBlue;">窗口</span> 与  <span style="color: Gold;">停止</span>-<span style="color: green;">等待</span>协议（ <span style="color: Gold;">S</span>-<span style="color: green;">W</span>）

<ul>

#### 基本原理

<ul>

- 发送方每次只能发送一个帧
- 需等待接收方确认后才可发送下一帧
- 发送窗口和接收窗口大小均为1

</ul>

#### 差错处理

<ul>

- 数据帧破坏情况：
  - 接收方检测到破坏后丢弃
  - 发送方超时重传直到正确接收
- 确认帧破坏情况：
  - 发送方重传数据帧
  - 接收方丢弃重复帧并重发确认

</ul>

#### 实现细节

<ul>

- 帧编号：
  - 使用1比特编号(0和1交替)
  - 确认帧使用ACK0和ACK1
- 缓冲区设置：
  - 发送方和接收方都需设置帧缓冲区
  - 发送方需保留副本用于重传

</ul>


</div>
<div style="float: right; width: 26%; padding: 1%;">

</div>
<div style="clear: both;"></div>