<div style="float: left; width: 64%; padding: 1%;">

## 客户/服务 <span style="color: blue;">C</span></b>/<b><span style="color: green;">S</span> 器模型  

<ul>

>pro：C/S模型和P2P模型的特点（2019）  

### 工作流程

<ul>

- 服务器处于接收请求的状态
- 客户机发出服务请求，并等待接收结果
- 服务器收到请求后，分析请求，进行必要的处理，得到结果并发送给客户机

</ul>

### 基本特征

<ul>

- 客户是服务请求方，服务器是服务提供方
  - 服务器上运行着专门用来提供某种服务的程序，可同时处理多个远程或本地客户的请求
  - 客户程序必须知道服务器程序的地址
  - 服务器启动后就一直不断地运行着，被动等待并接收来自各地客户的请求
  - 服务器程序不需要知道客户程序的地址
- 常见应用包括Web、文件传输协议（FTP）、远程登录和电子邮件等

</ul>

### 主要特点

<ul>

- 网络中各计算机的地位不平等，服务器可通过对用户权限的限制来达到管理客户机的目的
- 整个网络的管理工作由少数服务器担当，因此网络的管理非常集中和方便
- 客户机相互之间不直接通信
- 可扩展性不佳，受服务器硬件和网络带宽的限制，服务器支持的客户机数有限
- pic
  - ![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/0968413e5bed6d57bfeff2b949e4c6ede48faed1adb20a5457f23dced3514fd4.jpg)  
  图6.1C/S模型  

</ul>
</ul>

</div>
<div style="float: right; width: 26%; padding: 1%;">

</div>
<div style="clear: both;"></div>
