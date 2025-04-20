<div style="float: left; width: 64%; padding: 1%;">

## PPP协议 <span style="color: gray; font-size: 14px;">Point-to-Point Protocol</span>

<ul>

### 概述

<ul>

- 是现在最流行的点对点链路控制协议
- 主要应用
  - 用户计算机与ISP通信时所用的数据链路层协议
  - 广域网路由器之间的专用线路

</ul>

### 组成

<ul>

- 链路控制协议（LCP）
  - 用来建立、配置、测试数据链路连接
  - 协商一些选项
- 网络控制协议（NCP）
  - 为不同网络层协议配置
  - 建立和配置逻辑连接
- IP数据报封装方法
  - IP数据报在PPP帧中作为信息部分
  - 长度受MTU限制

</ul>

### 帧格式

<ul>

- 帧结构如图3.33所示

![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/1e8d91d9da44885d266b032830b73b1f319582eddaad40c563b504eeddffc9ef.jpg)  
图3.33PPP帧的格式  

#### 首部字段

<ul>

- 标志字段(F)：0x7E
- 地址字段(A)：0xFF
- 控制字段(C)：0x03
- 协议字段：2字节
  - 0x0021表示IP数据报
  - 0xC021表示LCP数据

</ul>

#### 信息字段

<ul>

- 长度可变(0~1500字节)

>attention:  
因为PPP是点对点的，并不是总线形，所以无须使用CSMA/CD协议，自然就不会有最短帧长的限制，所以信息段占 $0\sim1500$ 字节，而不是46\~1500学节。  

</ul>

#### 尾部字段

<ul>

- 帧检验序列(FCS)：2字节，使用CRC检验

</ul>

</ul>

### PPP协议状态图及工作过程

<ul>

- 状态图如图3.34所示

![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/d94ee3aeefa6ea19b8d920eb532cdff20689de0539f58617c2802450a1044797.jpg)  
图3.34PPP协议的状态图  

#### 工作状态流程

<ul>

- 链路静止状态
- 链路建立状态
- 鉴别状态
- 网络层协议状态
- 链路打开状态
- 链路终止状态

</ul>

</ul>

###  <span style="color: Gold;">特点</span>

<ul>

- 不使用序号和确认机制，只保证无差错接收
  - 只支持全双工的点对点链路
  - 两端可运行不同网络层协议
- 面向 <span style="color: GreenYellow;">字节</span>
  - 帧长为整数个字节

</ul>

</ul>

</ul>

</div>
<div style="float: right; width: 26%; padding: 1%;">

</div>
<div style="clear: both;"></div>
