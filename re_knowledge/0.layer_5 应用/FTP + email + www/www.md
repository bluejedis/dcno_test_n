<div style="float: left; width: 64%; padding: 1%;">

# 万维网 (**www**)  

<ul>

## WWW的概念与组成结构

<ul>

### WWW基本概念

<ul>

- 万维网（WorldWideWeb，WWW）是分布式、联机式的信息存储空间
  - 有用的事物称为"资源"
  - 资源由统一资源定位符（URL）标识
  - 通过HTTP协议传送给使用者
  - 使用者通过单击链接获取资源

</ul>

### WWW特点与功能

<ul>

- 使用链接方法便于站点间访问
- 支持按需获取信息
- 通过超文本标记语言设计页面
- 支持页面间超链接

</ul>

>pro：HTTP在传输层所使用的协议（2018）

### WWW核心组成

<ul>

#### 统一资源定位符（URL）

<ul>

- 标识万维网文档
- 确保文档唯一性

</ul>

#### 超文本传输协议（HTTP）

<ul>

- 应用层协议
- 使用TCP连接
- 规范客户端与服务器交互

</ul>

#### 超文本标记语言（HTML）

<ul>

- 文档结构标记语言
- 描述页面信息（文字、声音、图像、视频等）
- 定义页面格式

</ul>
</ul>

### URL结构与格式

<ul>

- 一般形式：<协议>://<主机>:<端口>/<路径>
  - 协议：http、ftp等
  - 主机：域名或IP地址
  - 端口和路径可选
  - 不区分大小写

</ul>

### WWW工作模式

<ul>

#### 客户端/服务器架构

<ul>

- 浏览器作为客户端程序
- Web服务器运行服务器程序

</ul>

#### 工作流程

<ul>

1. 建立连接与请求
   - Web用户通过浏览器指定URL
   - 与Web服务器建立连接
   - 发送浏览请求

2. 服务器处理
   - URL转换为文件路径
   - 返回信息给浏览器

3. 连接终止
   - 通信完成后关闭连接

</ul>
</ul>

### WWW在因特网中的地位

<ul>

- 构成因特网**最主要**部分
- 与其他服务共存
  - 电子邮件
  - Usenet
  - 新闻组

</ul>
</ul>

## 超文本传输协议（HTTP）  

<ul>

### 概述

<ul>

- HTTP是一个面向事务的应用层协议，具有以下特点：
  - 定义了浏览器与服务器之间的交互规则
    - 规定了浏览器如何向服务器请求文档
    - 规定了服务器如何向浏览器传送文档
  - 作为可靠文件交换的基础
    - 支持多种类型文件的交换
      - 文本文件
      - 声音文件  
      - 图像文件
      - 其他多媒体文件

</ul>

### 操作过程

<ul>

#### 基本工作过程

<ul>

- 浏览器访问WWW服务器时:
  - 首先完成对WWW服务器的域名解析
  - 获得服务器IP地址后，通过TCP发送连接建立请求

- ![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/363a6b1080e3e78e9e80684b408b2662a0e895391584428207a067d33fa28931.jpg)  
图6.11万维网的工作过程  

- 具体过程:
  - 服务器进程监听TCP端口80
  - 与浏览器建立TCP连接
  - 浏览器发送HTTP请求
  - 服务器返回HTTP响应
  - 浏览器解释显示Web页
  - TCP连接释放

</ul>

>pro：访问Web时可能用到的协议（2014、2021）  

#### 访问网站的具体事件流程

<ul>

- 以访问清华大学网站为例:
  - URL输入
  - DNS解析
  - 建立TCP连接
  - HTTP请求发送
  - 服务器响应
  - TCP连接释放
  - 浏览器解释显示

- 涉及协议:
  - 应用层: DHCP、DNS、HTTP
    - DHCP（动态主机配置协议）
      - 用于自动分配IP地址和其他网络配置参数给网络中的设备
      - 作用: 简化网络管理，减少IP地址冲突，并提高IP地址的使用效率
  - 传输层: UDP、TCP
  - 网际层: IP、ARP
  - 数据链路层: CSMA/CD或PPP

</ul>
</ul>

### 特点

<ul>

#### 基本特性

<ul>

- 使用TCP作为传输层协议
- HTTP本身无连接
- HTTP无状态

</ul>

#### Cookie机制

<ul>

- 工作原理:
  - 初次访问:
    - 服务器生成Cookie识别码
    - 创建数据库项目
    - 响应报文添加Set-cookie
  - 再次访问:
    - 请求报文包含Cookie
    - 服务器查询数据库
    - 执行个性化工作

</ul>

#### 连接方式

<ul>

##### 非持续连接

<ul>

- 特点:
  - 每个对象需单独TCP连接
  - 时间开销: 文档传输时间 + 2RTT
  - 服务器负担重

</ul>

![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/08b82f7f1d88b1f3b0c9eb1da958e256c83631e22d81d9985f204e369daec97d.jpg)  
图6.12请求一个万维网文档所需的时间  

##### 持续连接

<ul>

- 特点:
  - 服务器保持连接
  - 可继续传送后续请求和响应

</ul>

![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/d8a1e5c5841bd5690047250af1122856a1bed175683d0f7181aa958511f8ee4e.jpg)  
图6.13使用持续连接（非流水线）  

>pro：HTTP/1.1页面请求时间的分析（2011、2022）  

###### 持续连接的两种方式

<ul>

- 非流水线方式:
  - 串行请求和响应
  - TCP连接空闲浪费
- 流水线方式:
  - 连续发送请求
  - 共计1个RTT延迟
  - 受TCP发送窗口限制

</ul>
</ul>
</ul>

### **报文结构**  

<ul>

>pro：  HTTP请求报文中各种方法的意义（2015）  

#### 报文基本概念

<ul>

- HTTP是面向文本的（Text-Oriented）
  - 报文中每个字段都是ASCII码串
  - 每个字段长度不确定
- 两类HTTP报文：
  - **请求**报文：从客户向服务器发送的请求报文
  - **响应**报文：从服务器到客户的回答

</ul>

![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/dc22417e8a5262e7d4371c0540322afc2b85b46a41a3f4dc747d385dd38e9c24.jpg)  
图6.14HTTP的报文结构  

#### 报文组成部分

<ul>

- 开始行
  - 请求报文：称为请求行
  - 响应报文：称为状态行
  - 三个字段间以空格分隔
  - 以CR和LF结束
- 首部行
  - 说明浏览器、服务器或报文主体信息
  - 可有多行或不使用
  - 每行包含首部字段名和值
  - 以空行与实体主体分隔
- 实体主体
  - 请求报文一般不用
  - 响应报文可能没有

</ul>

#### 请求报文详解

<ul>

##### 请求行组成

<ul>

- 三个内容：
  - 方法
  - 请求资源的URL
  - HTTP版本

</ul>

##### 常用方法

<ul>

表6.1HTTP请求报文中常用的几个方法
![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/92d53ee3242092e4b08f0650c3127b1480828e42ece80aeb9314973ae11db4ab.jpg)  

</ul>

##### 典型请求报文示例

<ul>

- GET/bbs/index.htmHTTP/1.1
- Host:www.cskaoyan.com
- Connection: Keep-Alive
- User-Agent:Mozilla/5.0
- Accept-Language: cn

</ul>
</ul>

#### 响应报文详解

<ul>

##### 状态行组成

<ul>

- 三个内容：
  - HTTP版本
  - 状态码
  - 解释状态码的短语
- 常见状态行示例：
  - HTTP/1.1 202 Accepted
  - HTTP/1.1 400 Bad Request
  - HTTP/1.1 404 Not Found

</ul>
</ul>
</ul>

### 请求报文举例  

<ul>

#### Wireshark捕获分析

<ul>

![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/515e751b14db49afc2fe22d36d3a943c3fb0480756f37eda47cc30973bd9d976.jpg)  
图6.15用Wireshark捕获的一个HTTP请求报文  

##### 数据帧结构分析

<ul>

- 以太网数据帧：
  - 目的MAC地址：00-0f-e2-3f-27-3f（第1~6字节）
  - 本机MAC地址：00-27-13-67-73-8d（第7~12字节）
  - 类型字段：08-00（第13~14字节）
- IP数据报首部：
  - 源IP地址：219.223.210.112
  - 目的IP地址：113.105.78.10
- TCP报文段首部：第35~54字节
- TCP数据部分：从第55字节开始

</ul>
</ul>

#### 常见应用层协议

<ul>

-![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/6a17e3acc5e24d05afd103b899739bb177a17668a96e0a1d020cb0a76d5289c1.jpg)  
表6.2常见应用层协议小结

</ul>
</ul>
</ul>
</ul>

</div>
<div style="float: right; width: 26%; padding: 1%;">

</div>
<div style="clear: both;"></div>
