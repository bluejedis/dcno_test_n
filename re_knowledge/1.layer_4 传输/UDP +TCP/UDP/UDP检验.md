<div style="float: left; width: 64%; padding: 1%;">

## ⚠️UDP<span style="color: orange;">检验</span>

<ul>

### UDP<span style="color: orange;">检验</span><span style="color: green;">和</span>计算概述

<ul>

- 在计算检验和时，要在UDP数据报之前增加12B的伪首部
  - 伪首部并不是UDP的真正首部
  - 只是在计算检验和时，临时添加在UDP数据报的前面，得到一个临时的UDP数据报
  - 检验和就是按照这个临时的UDP数据报来计算的
  - 伪首部既不向下传送又不向上递交，而只是为了计算检验和

- ![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/05fa857d9ae050353446295e04e96bef0c74167c8553e5cf4439dd5c06e12f8d.jpg)  
图5.4UDP数据报的首部和伪首部  

</ul>

### UDP检验和特点

<ul>

- UDP计算检验和的方法和计算IP数据报首部检验和的方法相似
- 不同点：
  - IP数据报的检验和只检验IP数据报的首部
  - UDP的检验和要将首部和数据部分一起检验

</ul>

### UDP检验和<span style="color: green;">计算</span>方法

<ul>

- 发送方计算步骤：
  - 首先把全0放入检验和字段并添加伪首部
  - 把UDP数据报视为许多16位的字串接起来
  - 若UDP数据报的数据部分不是偶数个字节，则要在末尾填入一个全0字节（但此字节不发送）
  - 按二进制反码计算出这些16位字的和
  - 将此和的二进制反码写入检验和字段，并发送
- 接收方计算步骤：
  - 把收到的UDP数据报加上伪首部（若不为偶数个字节，则还需要补上全0字节）
  - 按二进制反码求这些16位字的和
  - 当无差错时其结果应为全1，否则就表明有差错出现
  - 有差错时接收方就应该丢弃这个UDP数据报
- ![image](https://bluejedis.github.io/picx-images-hosting/image.4g4j0ss5qe.webp)
- ![](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/9a474cc8b394cdcf814dda506d8775a8ef67f54081079a382c666e8607f4cb96.jpg)  
图5.5计算UDP检验和的例子  
-
  ```mermaid
  flowchart TD
    subgraph 发送方
        A[开始] --> B[校验和字段填充0]
        B --> C[添加伪首部]
        C --> D[将UDP数据报视为16位字串]
        D --> E[若为奇数字节则末尾补0]
        E --> F[计算二进制反码和]
        F --> G[将反码写入校验和字段]
        G --> H[发送数据报]
    end

    subgraph 接收方
        I[接收数据报] --> J[添加伪首部]
        J --> K[若需要则补充字节]
        K --> L[计算二进制反码和]
        L --> M{结果是否全1?}
        M -->|是| N[接受数据报]
        M -->|否| O[丢弃数据报]
    end
  ```
- 
  ```mermaid
    flowchart TD
      subgraph Receiver
          I[Receive datagram] --> J[Add pseudo header]
          J --> K[Add padding if needed]
          K --> L[Calculate ones' complement sum]
          L --> M{Sum = all 1s?}
          M -->|Yes| N[Accept datagram]
          M -->|No| O[Discard datagram]
      end
      subgraph Sender
          A[Start] --> B[Fill checksum field<br> with zeros]
          B --> C[Add pseudo header]
          C --> D[Treat UDP datagram as <br>16-bit strings]
          D --> E[Add padding zero byte <br>if odd length]
          E --> F[Calculate ones' complement sum]
          F --> G[Write ones' complement to <br>checksum field]
          G --> H[Send datagram]
      end
  ```

</ul>

> attention:

### 注意事项

<ul>

- 检验时，若UDP数据报部分的长度**不是偶数个字节**，则需填入一个全0字节，如图5.5所示
  - 但是此字节和伪首部一样，是不发送的
- 若UDP检验和检验出UDP数据报是**错误**的：
  - **丢弃**
  - **or交付**给上层，但是需要附上错误报告，即告诉上层这是错误的数据报
- 通过伪首部的作用：
  - 可以检查源端口号、目的端口号和UDP用户数据报的数据部分
  - 还可以检查IP数据报的源IP地址和目的地址

</ul>

### 检验方法评价

<ul>

- 这种简单的差错检验方法的校错能力并不强
- 好处是**简单**、 посмотрел速度**快**

</ul>

</ul>


</div>
<div style="float: right; width: 26%; padding: 1%;">

</div>
<div style="clear: both;"></div>
