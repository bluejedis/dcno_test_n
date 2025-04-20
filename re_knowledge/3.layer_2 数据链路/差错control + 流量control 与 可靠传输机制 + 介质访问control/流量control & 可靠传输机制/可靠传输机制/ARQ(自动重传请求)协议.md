<div style="float: left; width: 64%; padding: 1%;">

### 基本概念与机制

<ul>

- 可靠传输含义：发送方发送的数据都能被接收方正确地接收
- 实现机制：
  - 确认机制：接收方每收到发送方发来的数据顺，都要向发送方发回一个确认顺
  - 超时重传机制：发送方在发送数据后启动计时器，规定时间内未收到确认则重发

</ul>

### <span style="color: LightSkyBlue;">A</span><span style="color: green;">R</span><span style="color: Gold;">Q</span>协议 <span style="color: gray; font-size: 14px;">Automatic Repeat-reQuest</span>

<ul>

- ARQ(自动重传请求)协议特点：
  - 重传自动进行，无需接收方请求
  - 数据帧和确认帧需编号
- 分类：
  - 停止-等待协议
  - 后退N帧协议 
  - 选择重传协议
- 应用范围：
  - 不仅限于数据链路层
  - 可应用到上层协议
- 使用场景：
  - 有线网络：链路误码率低，不要求数据链路层提供可靠传输
  - 无线网络：链路易受干扰，要求数据链路层提供可靠传输

</ul>


</div>
<div style="float: right; width: 26%; padding: 1%;">

</div>
<div style="clear: both;"></div>
