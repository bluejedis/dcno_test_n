<div style="float: left; width: 64%; padding: 1%;">
## 电子邮件格式与<b><span style="color: purple;">M</span></b>IME  

<ul>

### 电子邮件格式  

<ul>

#### 基本结构

<ul>

- 一个电子邮件分为信封和内容两大部分
- 邮件内容又分为首部和主体两部分
- RFC822规定了邮件的首部格式，而邮件的主体部分则让用户自由撰写
- 用户写好首部后，邮件系统自动地将信封所需的信息提取出来并写在信封上，用户不需要亲自填写信封上的信息

</ul>

#### 邮件首部格式

<ul>

- 邮件内容的首部包含一些首部行
  - 每个首部行由一个关键字后跟冒号再后跟值组成
  - 有些关键字是必需的，有些则是可选的
  - 最重要的关键字是To和Subject

##### To关键字

<ul>

- 是必填的关键字
- 后面填入一个或多个收件人的电子邮件地址
- 电子邮件地址的格式：
  - 收件人邮箱名 $@$ 邮箱所在主机的域名
  - 如abc@cskaoyan.com
  - abc cska oy an.com这个邮件服务器上必须是唯一的
  - 这也就保证了该邮件地址在整个因特网上是唯一的

</ul>

##### Subject关键字

<ul>

- 是可选关键字
- 是邮件的主题
- 反映了邮件的主要内容

</ul>

##### From关键字

<ul>

- 是必填的关键字
- 通常由邮件系统自动填入
- 首部与主体之间用一个空行进行分割

</ul>

##### 典型邮件内容示例

<ul>

- ![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/ad6c7d88b4818d5ccfd48b3f5f46a9fdfe4b14571fa005e2fce9eb9bd53a5b58.jpg)  

</ul>
</ul>
</ul>

### 多用途**M**ultipurpose因特网邮件扩展**I**nternet **M**ail **E**xtensions（MIME）  

<ul>

>pro：SMTP直接传输的内容（2018）  

#### MIME产生背景

<ul>

- SMTP只能传送7位ASCII码文本邮件
- 许多其他非英语国家的文字无法传送
  - 如中文、俄文
  - 甚至带重音符号的法文或德文
- 无法传送可执行文件及其他二进制对象

</ul>

#### MIME与SMTP关系

<ul>

- MIME**并未改动**SMTP或取代它
- 发送过程：
  - 当发送端发送的邮件中包含有非ASCII码数据时，不能直接使用SMTP进行传送
  - 要通过MIME进行转换，将非ASCII码数据转换为ASCII码数据
  - 之后，就可以使用SMTP进行传送
- 接收过程：
  - 接收端要使用MIME对接收到的ASCII码数据进行逆转换
  - 以便可以得到包含有非ASCII码数据的邮件

</ul>

![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/b50f6aad5d70911c62bdd8542a01a0e00833e19a2ac698dac6e472b48a6ca867.jpg)  
图6.10SMTP与MIME的关系  

#### MIME主要内容

<ul>

- 5个新的邮件首部字段
  - MIME版本
  - 内容描述
  - 内容标识
  - 传送编码
  - 内容类型
- 定义了许多邮件内容的格式，对多媒体电子邮件的表示方法进行了标准化
- 定义了传送编码，可对任何内容格式进行转换，而不会被邮件系统改变

</ul>
</ul>
</ul>

</div>
<div style="float: right; width: 26%; padding: 1%;">

</div>
<div style="clear: both;"></div>
