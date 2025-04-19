<div style="float: left; width: 64%; padding: 1%;">


## 域名<span style="color: green;">解析</span>过程  

<ul>

>pro：**DNS**(域名系统) 协议的作用（2021)  

### 基本概念

<ul>

- 域名解析是指把域名转化为IP地址的过程
- 当客户端需要域名解析时，通过本机的DNS客户端构造一个DNS请求报文，以UDP数据报方式发往本地域名服务器

</ul>

### 查询方式

<ul>

域名解析有两种方式：递归查询和选代查询。

#### <span style="color: green;">递归</span>查询

<ul>

##### 主机 → 本地域名服务器

<ul>

- 若主机 所询问的本地域名服务器 → 不知道被查询域名的IP地址
  - 本地~ 以DNS客户的身份
    - 向**根**域名服务器继续发出查询请求报文（即替该主机继续查询）
  - 而不是 让该主机自己进行下一步的查询
- 两种查询方式的这一步是相同的

</ul>

>pro：递归查询DNS的工作原理（2010）  

##### 本地域名服务器 → 其他~ 的 <span style="color: green;">递归</span>查询

<ul>

- 本地域名服务器只需向根域名服务器查询一次
- 后面的几次查询都是递归地在其他几个域名服务器之间进行的［步骤 $\scriptstyle(\mathbf{\mathcal{B}}\sim\left(\mathbf{\mathcal{C}}\right)$ ]
- 在步骤 $\circleddash$ 中，本地域名服务器从根域名服务器得到了所需的ⅡP地址
- 最后在步骤 $^\mathrm{\textregistered}$ 中，本地域名服务器把查询结果告诉发起查询的主机
- 因为该方法给根域名服务器造成的负载过大，所以**实际**中**几乎不**使用

</ul>
</ul>

#### pic

<ul>

- ![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/2663a99a9e96d72925ec8df3f3c96270b6c7942f0010e486c7694ed8830a3713.jpg)  
图6.6两种域名解析方式工作原理  
- unsertand:
  - 递归→顺次；迭代→有1个顺次，后面一步到位

</ul>

#### <span style="color: orange;">迭代</span>查询

<ul>

>pro：迭代查询DNS的工作原理（2016、2020）  

##### 本地域名服务器→其他~的 <span style="color: orange;">迭代</span>查询

<ul>

- 本地域名服务器 → 根域名~  <span style="color: gray;">的查询  通常是采用送代查询</span>
- 当根域名服务器收到本地域名服务器发出的选代查询请求报文时：
  - 要么给出所要查询的IⅡP地址
  - 要么告诉本地域名服务器："你下一步应当向哪个顶级域名服务器进行查询"
- 然后让本地域名服务器进行后续的查询（而不替本地域名服务器进行后续的查询）
- 顶级域名服务器收到查询报文后：
  - 要么给出所要查询的IP地址
  - 要么告诉本地域名服务器下一步应当向哪个权限域名服务器查询
- 最后，知道了所要解析的域名的IP地址后，把这个结果返回给发起查询的主机

</ul>
</ul>
</ul>

### 域名解析<span style="color: lightblue;">eg

<ul>

- 假定某客户机想获知域名为y.abc.com主机的IP地址，域名解析的过程
- （最多需要使用8个UDP报文：4个查询报文和4个回答报文）：  

  - 客户机向其本地域名服务器发出DNS请求报文（递归查询）
  - 本地域名服务器收到请求后
    - 查询本地缓存，若没有该记录
      - 则以DNS客户的身份向根域名服务器发出解析请求报文（迭代查询）
  - 根域名服务器收到请求后
    - 判断该域名属于.com域
      - 将对应的顶级域名服务器dns.com的IP地址返回给本地域名服务器
  - 本地域名服务器向顶级域名服务器dns.com发出解析请求报文（迭代查询）
  - 顶级域名服务器dns.com收到请求后
    - 判断该域名属于abc.com域
      - 因此将对应的权限域名服务器dns.abc.com的IP地址返回给本地域名服务器
  - 本地域名服务器向权限域名服务器dns.abc.com发起解析请求报文（迭代查询）
  - 权限域名服务器dns.abc.com收到请求后
    - 将查询结果返回给本地域名服务器
  - 本地域名服务器将查询结果保存到本地缓存
    - 同时返回给客户机

- ![image](https://bluejedis.github.io/picx-images-hosting/image.b8xncbpc0.webp)
  

  ```mermaid
  sequenceDiagram
      participant C as 客户机
      participant L as 本地域名服务器
      participant R as 根域名服务器
      participant T as 顶级域名服务器dns.com
      participant A as 权限域名服务器dns.abc.com

      C->>+L: 1.DNS请求报文(递归查询)
      L->>+R: 2.解析请求报文(迭代查询)
      R-->>-L: 3.返回顶级域名服务器dns.com的IP
      L->>+T: 4.解析请求报文(迭代查询)
      T-->>-L: 5.返回权限域名服务器dns.abc.com的IP
      L->>+A: 6.解析请求报文(迭代查询)
      A-->>-L: 7.返回查询结果
      L-->>-C: 8.返回查询结果

  ```

</ul>

### 高速缓存

<ul>

- store域名的相关映射信息<span style="color: gray;">(最近查询过的)
  - another**相同**的**域名查询**arrive
  - **直接**提供 **IP地址**

- details
  - 为了提高DINS的查询效率，并减少因特网上的DNS查询报文数量，在域名服务器中广泛地使用了高速缓存
  - 用来缓存最近查询过的域名的相关映射信息
  - 当另一个**相同**的**域名查询**到达该DNS服务器时，该服务器就能**直接**提供所要求的IP地址
  - 因为主机名和IP地址之间的映射不是永久的，所以DNS服务器将在**一段时间**后丢弃高速缓存中的信息
  - 在主机中同样也很需要高速缓存：
    - 许多主机在启动时从本地域名服务器下载域名和地址的全部数据库
    - 维护存放自己最近使用的域名的高速缓存
    - 只在从**缓存中找不到**域名时才使用域名服务器

</ul>
</ul>
</ul>

</div>
<div style="float: right; width: 26%; padding: 1%;">

</div>
<div style="clear: both;"></div>
