---
YAML是“YAML不是一种标记语言”的外语缩写
---

[TOC]

## 标题

# 一级标题

## 二级标题

### 三级标题

#### 四级标题

##### 五级标题

###### 六级标题



## 段落

中华人民共和国，在北半球。

**海南省`接近`赤道。**

## 强调

*斜体两边一个星号*

**粗体两边两个星号**

***粗体加斜体则是三个***

`文字强调两边一个反单引号`

## 列表

- name: Aaron
- age: 40
- info:
  - 1 
  - 2
  - 3
    - 1)
    - 2)

1. name: Aaron
2. age:40
3. info:
   1. qq
   2. phone

### 代码(三个反单引号，在英文输入模式下；三个波浪线则是中文）

~~~python
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

res = Dog()
print(res)
~~~



### 内嵌式链接

[百度]

[内部链接文件名称](概述.md)

[标题](excise.md#标题)

[引用式链接别名]



### 引用式链接

### 图片

网络图片引用

![百度logo][网络图片]

本仓库图片引用

![本地图片][本仓库图片]

> 中华人民共和国，在北半球。
>
> ​						——纳兰《浣溪沙》

多重引用

> >中华人民共和国，在北半球。`

### 水平分隔线

------

就是三个减号

### HTML代码

```HTML
<p align='center'>
    Hello World!
</p>
```

```Html
<p align='center'><img src='https://www.baidu.com/img/bd_logo1.png'/></p>
```

### 表格

|   这   |    是    |   表头   |
| :----: | :------: | :------: |
| Typora | 居然这么 | 智能制表 |
|   在   |  左上角  | 调配表格 |

### [GFM][Github Flavored Markdown介绍]

GitHub Flvored MarkDown

- [ ] item1
- [ ] item2
- [ ] tiem3




- [ ] yes
- [ ] no



### 表情符号

:smile:

:hourglass_flowing_sand:

:snake:





[豆瓣][原来引用式链接在这里]

[原来引用式链接在这里]: www.douban.com	"练习参考连接"
[百度]:http://www.baidu.com
[引用式链接别名]: http://www.baidu.com	"链接别名：百度网"
[网络图片]: https://www.baidu.com/img/bd_logo1.png	"引用式链接图片"
[本仓库图片]: git3.PNG	"引用本仓库链接图片"
[Github Flavored Markdown介绍]: https://www.jianshu.com/p/cfPxyr "Github Flavored Markdown介绍"
