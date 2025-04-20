<div style="float: left; width: 64%; padding: 1%;">

###  <span style="color: purple;">多</span>帧<span style="color: GreenYellow;">滑动</span><span style="color: LightSkyBlue;">窗口</span> 与 <span style="color: LightSkyBlue;">选择</span><span style="color: green;">重传</span>协议（<span style="color: LightSkyBlue;">S</span><span style="color: green;">R</span>）

<ul>

Selective Repeat

#### 工作原理

<ul>

>pro：选择重传协议的工作原理（2011）  

- 只重传出错和超时的帧
- 接收方可接收失序但正确的帧
- 需要较大接收窗口缓存失序帧

</ul>

#### 实现<span style="color: green;">机制</span>

<ul>

- 确认机制：
  - 逐<span style="color: LightSkyBlue;">帧</span>确认，不使用累积确认
  - 可使用NAK请求立即重传
-  <span style="color: Gold;">缓冲</span>要求：
     -  <span style="color: GreenYellow;">接收方</span> 设置 足够<span style="color: LightSkyBlue;">帧</span>缓冲区
     - every <span style="color: LightSkyBlue;">发送</span> <span style="color: Gold;">缓冲</span>区对应 → 一个计时器

</ul>

#### <span style="color: LightSkyBlue;">窗口</span>设置

<ul>

- 基本要求：
  - WR和WT都大于1
  - 使用n比特编号时需满足：
    - WR+WT≤2^n
    - WR≤WT
    - WR≤2^n-1
  - 通常WR和WT大小相同

![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/de59299ec42c47f7749328137b7d85d10deaadf593f80970a3170cc75da885a2.jpg)  
图3.12SR协议的工作原理：对超时和出错数据帧的处理

</ul>


</div>
<div style="float: right; width: 26%; padding: 1%;">

</div>
<div style="clear: both;"></div>
