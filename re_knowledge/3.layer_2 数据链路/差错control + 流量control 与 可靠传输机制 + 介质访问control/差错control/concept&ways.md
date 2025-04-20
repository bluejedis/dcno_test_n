<div style="float: left; width: 64%; padding: 1%;">

## 基本概念

<ul>

- 实际通信链路都不是理想的
  - 比特在传输过程中可能产生差错
    - 1可能变成0
    - 0也可能变成1
  - 这就是比特差错
- 比特差错是传输差错中的一种，本节仅讨论比特差错

</ul>

## 差错控制方式

<ul>

- 通常利用编码技术进行差错控制，主要有两类：
  - 自动重传请求（AutomaticRepeatreQuest，ARQ）
    - 当接收方检测到差错时，就设法通知发送方重发
    - 直到收到正确的数据为止
  - 前向纠错（Forward Error Correction，FEC）
    - 接收方不但能发现差错
    - 而且能确定错误的位置并加以纠正
- 因此，差错控制又可分为：
  - 检错编码
  - 纠错编码

</ul>
</div>
<div style="float: right; width: 26%; padding: 1%;">

</div>
<div style="clear: both;"></div>
