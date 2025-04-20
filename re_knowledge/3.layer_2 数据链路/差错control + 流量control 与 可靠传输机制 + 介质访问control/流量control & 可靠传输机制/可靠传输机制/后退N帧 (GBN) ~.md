<div style="float: left; width: 64%; padding: 1%;">

### <span style="color: purple;">多</span>帧<span style="color: GreenYellow;">滑动</span><span style="color: LightSkyBlue;">窗口</span> 与 <span style="color: green;">后退</span>N帧协议（<span style="color: green;">GB</span>N）

<ul>

#### 基本工作原理

<ul>

>pro：GBN协议的工作原理（2009）  

- 发送方可连续发送多个帧而无需等待确认
- 出错时需重传出错帧及其后续N个帧

</ul>

#### 确认机制

<ul>

>pro：GBN确认号的含义/捎带确认的应用（2017）  

- 累积确认：
  - 可对连续多个正确帧只确认最后一个
  - ACKn表示n号帧及之前所有帧均正确接收
- 接收方只按序接收数据帧

</ul>

#### 差错处理

<ul>

>pro：GBN超时重传的分析（2017）  

![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/f3d8ffa553e14eac7cd68cf2198b841bed3882b8f8397d4235957d13e95a1280.jpg)  
图3.11GBN协议的工作原理：对出错数据帧的处理  

</ul>

#### 窗口设置

<ul>

>pro：GBN发送窗口的意义/最大尺寸（2017）  

- 发送窗口要求：
  - 使用n比特编号时，1<WT≤2^n-1
  - 超出范围会导致新旧帧无法分辨
- 接收窗口：
  - WR=1，保证按序接收
- 效率分析：
  - 优点：连续发送提高信道利用率
  - 缺点：重传包含正确帧，在高误码率时效率可能低于停止-等待协议

</ul>


</div>
<div style="float: right; width: 26%; padding: 1%;">

</div>
<div style="clear: both;"></div>
