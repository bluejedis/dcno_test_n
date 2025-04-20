<div style="float: left; width: 64%; padding: 1%;">

## VLAN <span style="color:gray; font-size: 14px;">(virtual lan) 

<ul>

### 概念

<ul>

- 一个以太网是一个 <span style="color: GreenYellow;">广播</span>域，当一个以太网中包含的计算机太多时，往往会导致：
  - 以太网中出现大量的广播帧，特别是经常使用的ARP和DHCP协议（第4章）
  - 一个单位的不同部门共享一个局域网，对信息保密和安全不利
- 通过虚拟局域网（VirtualLAN，VLAN)，可将一个较大的局域网分割成一些较小的与地理位置无关的逻辑上的VLAN，而每个VLAN是一个较小的广播域

</ul>

### 划分方式

<ul>

- 基于接口
  - 将交换机的若干接口划为一个逻辑组
  - 这种方法最简单、最有效
  - 若主机离开了原来的接口，则可能进入一个新的子网
- 基于MAC地址
  - 按MAC地址将一些主机划分为一个逻辑子网
  - 当主机的物理位置从一个交换机移动到另一个交换机时，它仍属于原来的子网
- 基于IP地址
  - 根据网络层地址或协议划分VLAN
  - 这样的VLAN可以跨越路由器进行扩展，将多个局域网的主机连接在一起

</ul>

### 帧格式

<ul>

- 802.3ac标准定义了支持VLAN的以太网帧格式的扩展
  - 在以太网帧中插入一个4字节的标识符（插在源地址字段和类型字段之间）
  - 称为VLAN标签，用来指明发送该顿的计算机属于哪个虚拟局域网
  - 插入VLAN标签的帧称为802.1Q顿
  - 以太网的最大帧长从原来的1518字节变为1522字节

![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/1fa3727e65c66ef56fbed43250bdacfe8219a92ec3a163fb8a0fb3a860dc6465.jpg)  
图3.30插入VLAN标签后变成了802.1Q帧  

#### 标签结构

<ul>

- 前两个字节总是置为 $0x8100$，表示这是一个802.1Q帧
- 后两个字节
  - 前4位实际上并没什么作用
  - 后12位是该VLAN的标识符VID，唯一标识该802.1Q顺属于哪个VLAN
  - 12位的VID可识别4096个不同的VLAN
- 插入VLAN标签后，802.1Q帧最后的FCS必须重新计算

</ul>

</ul>

### 工作原理

<ul>

- 交换机配置
  - 交换机1连接7台计算机，划分为VLAN-10和VLAN-20
  - VID值由交换机管理员设定
  - 各主机不知道自己的VID值，但交换机必须知道
  - 主机与交换机之间交互的都是标准以太网帧

![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/dd404bb6f4326a5aaef9831d2ab0187e38a5a00c9a33d5c1bef9ca4561b86ddf.jpg)  
图3.31利用以太网交换机构成虚拟局域网  

#### 通信场景

<ul>

- 同一交换机内VLAN通信
  - A站向B站发送帧：交换机1直接转发帧
- 跨交换机同VLAN通信
  - A站向E站发送帧：
    - 交换机1插入VLAN标签后转发
    - 交换机2移除VLAN标签后转发给E站
- 不同VLAN间通信
  - A站向C站发送帧：
    - 需要通过上层路由器
    - 或使用交换机中嵌入专用芯片进行转发

</ul>

</ul>

### 本质

<ul>

- 虚拟局域网只是局域网为用户提供的一种<span style="color: green;">服务</span>，并不是一种新型局域网

</ul>

</ul>
</ul>
</ul>
</ul>


</div>
<div style="float: right; width: 26%; padding: 1%;">

</div>
<div style="clear: both;"></div>
