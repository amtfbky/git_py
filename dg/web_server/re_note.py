In [3]: import re

In [4]: pattern = "itcast"

In [5]: s = "itheima"

In [6]: re.match(pattern, s)	# pattern不匹配s？

In [7]: s = "itcast"

In [8]: re.match(pattern, s)
Out[8]: <_sre.SRE_Match object; span=(0, 6), match='itcast'>

In [9]: result = re.match(pattern, s)

In [10]: dir(result)

In [11]: result.group()
Out[11]: 'itcast'

In [13]: res = re.match("itcast", "itcastitheima")

In [14]: res.group()
Out[14]: 'itcast'

In [15]: "itcastitheima".startswith("itcast")
Out[15]: True

In [16]: re.match(".", "i")
Out[16]: <_sre.SRE_Match object; span=(0, 1), match='i'>

In [17]: re.match(".", "\n")	# 占位符匹配任何字符，除了\n

In [18]: re.match("...", "ab")	#两位不中

In [19]: re.match("...", "abc")
Out[19]: <_sre.SRE_Match object; span=(0, 3), match='abc'>

In [20]: re.match("...", "abcd")
Out[20]: <_sre.SRE_Match object; span=(0, 3), match='abc'>

In [21]: re.match("\d", "1")
Out[21]: <_sre.SRE_Match object; span=(0, 1), match='1'>

In [22]: re.match("\d", "a")	# a非数字

In [23]: re.match("\d", "100")
Out[23]: <_sre.SRE_Match object; span=(0, 1), match='1'>

In [24]: re.match("\D", "a")	# a中，因为D匹配非数字
Out[24]: <_sre.SRE_Match object; span=(0, 1), match='a'>

In [25]: re.match("\s", " ")
Out[25]: <_sre.SRE_Match object; span=(0, 1), match=' '>

In [26]: re.match("\s", "\r")
Out[26]: <_sre.SRE_Match object; span=(0, 1), match='\r'>

In [27]: re.match("\s", "\n")
Out[27]: <_sre.SRE_Match object; span=(0, 1), match='\n'>

In [28]: re.match("\s", "\t")
Out[28]: <_sre.SRE_Match object; span=(0, 1), match='\t'>

In [29]: re.match("\S", "\t")	# \t是空白的制表符

In [30]: re.match("\w", "-a")	# -即减号非字母数字和下划线

In [31]: re.match("\w", "_a")
Out[31]: <_sre.SRE_Match object; span=(0, 1), match='_'>

In [32]: re.match("\w", "an")
Out[32]: <_sre.SRE_Match object; span=(0, 1), match='a'>	# a-z,A-Z,0-9,_

In [33]: re.match("\W", "an")

In [34]: re.match("\w\W", "2a")

In [35]: re.match("1\d\d\d\d\d\d\d\d\d\d", "178907")		# 匹配手机号位数不中

In [36]: re.match("1\d\d\d\d\d\d\d\d\d\d", "17222222222")
Out[36]: <_sre.SRE_Match object; span=(0, 11), match='17222222222'>

In [37]: re.match("1\d\d\d\d\d\d\d\d\d\d", "17222222222dfsaffd")# 后面加字母却中
Out[37]: <_sre.SRE_Match object; span=(0, 11), match='17222222222'>


\d == [0-9]
\D == [^0-9]
\w == [a-zA-Z0-9_]
\W == [^a-zA-Z0-9_]

In [38]: re.match("1[34578]", "18")
Out[38]: <_sre.SRE_Match object; span=(0, 2), match='18'>

In [39]: re.match("1[34578]", "19")	# 9不在方括号内

In [40]: re.match("1[^34578]", "19")
Out[40]: <_sre.SRE_Match object; span=(0, 2), match='19'>

In [41]: re.match("1[a-z5-9]", "19")
Out[41]: <_sre.SRE_Match object; span=(0, 2), match='19'>

In [42]: re.match("1[a-z5-9]", "11")	# 第二个1不在方括号内

In [43]: re.match("1\[34578]\[0-9]\[0-9]\[0-9]\[0-9]\[0-9]\[0-9]\[0-9]\[0-9]\[0-9]", "17222222222")

In [44]: re.match("1[34578][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", "17222222222")# 够笨的方法,还不对！
Out[44]: <_sre.SRE_Match object; span=(0, 11), match='17222222222'>

In [45]: re.match("1[34578]\d.........", "17222222222")	# 自己瞎想的，还没学到匹配多个字符的格式
In [59]: re.match("1[34578][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", "17222222222fdsafadsfa")# 后加字母也中
Out[59]: <_sre.SRE_Match object; span=(0, 11), match='17222222222'>

In [60]: re.match("1[34578]\d\d\d\d\d\d\d\d\d", "17222222222fdsafafadfasdf")# 后加字母也中
Out[60]: <_sre.SRE_Match object; span=(0, 11), match='17222222222'>

In [46]: re.match("1[34578]\d\d\d\d\d\d\d\d\d", "17222222222")# 够笨的方法
Out[46]: <_sre.SRE_Match object; span=(0, 11), match='17222222222'>

In [47]: re.match("\d*", "")	# *匹配前一个字符出现0次或无数次
Out[47]: <_sre.SRE_Match object; span=(0, 0), match=''>

In [48]: re.match("\d*", "abc")
Out[48]: <_sre.SRE_Match object; span=(0, 0), match=''>

In [49]: re.match("\d*", "43214abc")
Out[49]: <_sre.SRE_Match object; span=(0, 5), match='43214'>

In [50]: re.match("\d+", "abc")	# +匹配前一个字符出现1次或无数次，即至少出现1次

In [51]: re.match("\d+", "432abc")
Out[51]: <_sre.SRE_Match object; span=(0, 3), match='432'>

In [52]: re.match("\d?", "")	# ?匹配前一个字符出现1次或0次，即要么1次，要么没有
Out[52]: <_sre.SRE_Match object; span=(0, 0), match=''>

In [53]: re.match("\d?", "abc")
Out[53]: <_sre.SRE_Match object; span=(0, 0), match=''>

In [54]: re.match("\d?", "134124abc")
Out[54]: <_sre.SRE_Match object; span=(0, 1), match='1'>

In [55]: re.match("\d?", "3abc")
Out[55]: <_sre.SRE_Match object; span=(0, 1), match='3'>

In [56]: re.match("\d?[a-z]", "3abc")
Out[56]: <_sre.SRE_Match object; span=(0, 2), match='3a'>

In [57]: re.match("\d?\[a-z]", "3abc")

In [58]: re.match("\d?\[a-z]", "3431abc")

In [63]: re.match("1[34578]\d{9}", "17222222222")
Out[63]: <_sre.SRE_Match object; span=(0, 11), match='17222222222'>

In [64]: re.match("1[34578]\d{9}", "17222222222fdsafaf")
Out[64]: <_sre.SRE_Match object; span=(0, 11), match='17222222222'>

In [67]: re.match("1[34578]\d{8,}", "17222222222fdsafaf")# 8次以上的数字
Out[67]: <_sre.SRE_Match object; span=(0, 11), match='17222222222'>

In [68]: re.match("1[34578]\d{10,}", "17222222222fdsafaf")# 10次以上的数字就不中了

==============================================================================
以后的正则表达式都要加r这个原始字符串标记

In [69]: s = "\nabc"

In [70]: s
Out[70]: '\nabc'

In [71]: print(s)

abc

In [72]: s = "\\nabc"

In [73]: print(s)
\nabc

In [74]: re.match("\\nabc", s)

In [75]: re.match("\\\\nabc", s)
Out[75]: <_sre.SRE_Match object; span=(0, 5), match='\\nabc'>

In [76]: re.match("\\\\n\w", s)
Out[76]: <_sre.SRE_Match object; span=(0, 3), match='\\na'>

In [77]: s = r"\nabc"	# r的魔法

In [78]: print(s)
\nabc

In [79]: re.match("\\\\n\w", s)
Out[79]: <_sre.SRE_Match object; span=(0, 3), match='\\na'>

In [80]: re.match(r"\\n\w", s)
Out[80]: <_sre.SRE_Match object; span=(0, 3), match='\\na'>

In [81]: r"\\nabc"
Out[81]: '\\\\nabc'

**********************
案例1：手机号填入限定字符
**********************
In [82]: re.match("1[35678]\d{9}$", "17222222222")	# $匹配字符串结尾,终于把手机号给匹配好了
Out[82]: <_sre.SRE_Match object; span=(0, 11), match='17222222222'>

In [83]: re.match("1[35678]\d{9}$", "17222222222afdsafadsf")

In [84]: re.match("1[35678]\d{9}$", "1722222222289787")

In [85]: re.match("^1[35678]\d{9}$", "17222222222")	# $匹配字符串开头，但在match里不明显
Out[85]: <_sre.SRE_Match object; span=(0, 11), match='17222222222'>

-------------
上面都忘了加r了
-------------
In [86]: re.match(r"^\w+ve", "hover")
Out[86]: <_sre.SRE_Match object; span=(0, 4), match='hove'>

In [87]: re.match(r"^\w+ve\b", "hover")		# 非边界

In [88]: re.match(r"^\w+\bve\b", "hover")	# 非边界

In [89]: re.match(r"^\w+\bve\b", "ho ve r")	# 虽然有边界，但前面的\b的前面是匹配字母，不中，应该是\s

In [90]: re.match(r"^\w+\s\bve\b", "ho ve r")
Out[90]: <_sre.SRE_Match object; span=(0, 5), match='ho ve'>

In [91]: re.match(r"^.+\bve\b", "ho ve r")	# .+占位符和至少一位前字符，这里匹配"ho ve"，说明
# ve前面\b的前面有字符，即使是空格
Out[91]: <_sre.SRE_Match object; span=(0, 5), match='ho ve'>

In [92]: re.match(r"^.+ve\B", "ho ve r")	# \B非边界

In [93]: re.match(r"^.+ve\B", "ho ver")
Out[93]: <_sre.SRE_Match object; span=(0, 5), match='ho ve'>

In [94]: re.match(r"^.+\Bve\B", "ho ver")

In [95]: re.match(r"^.+\Bve\B", "hover")
Out[95]: <_sre.SRE_Match object; span=(0, 4), match='hove'>

**********************
案例2：匹配0~100之间的数字
**********************

In [113]: re.match(r"[1-9]\d?$|0$|100$", "09")	# |匹配左右任意一个表达式

In [114]: re.match(r"[1-9]?\d?$|100$", "0")	# [1-9]?表示1-9的数字可有可无，后面的\d就可以是0了，再后面的100怎么优化掉呢？
Out[114]: <_sre.SRE_Match object; span=(0, 1), match='0'>

==================================================================================================================

开始网页内容匹配了(分组)
-----------------------------------------------------------------------------------------------------------
1.抓取标签中间的内容，可分组提取
-----------------------------------------------------------------------------------------------------------
In [115]: res = re.match(r"<h1>(.*)</h1>", "<h1>匹配分组</h1>")

In [116]: res.group()
Out[116]: '<h1>匹配分组</h1>'

In [117]: res.group(1)	# 抓取的是第一个小括号(分组)里的内容
Out[117]: '匹配分组'

In [118]: res = re.match(r"(<h1>).*(</h1>)", "<h1>匹配分组</h1>")

In [119]: res.group(1)
Out[119]: '<h1>'

In [121]: res.group(2)	# 抓取的是第二个小括号(分组)里的内容
Out[121]: '</h1>'

In [122]: res.group(0)
Out[122]: '<h1>匹配分组</h1>'

In [123]: res.group()	# 默认参数0
Out[123]: '<h1>匹配分组</h1>'

In [124]: res.groups()
Out[124]: ('<h1>', '</h1>')

In [125]: res.groups()[0]	# 等价于res.group(1)
Out[125]: '<h1>'
-----------------------------------------------------------------------------------------------------------
2.抓取一对闭合标签内的内容，用到\num，引用分组num匹配到的字符串
-----------------------------------------------------------------------------------------------------------
In [126]: s = "<html><h1>itcast</h1></html>"

In [127]: re.match(r"<.+><.+>.+</.+></.+>", s)	# 这种方法不灵活，万一哪个标签名改动就匹配不出来了
Out[127]: <_sre.SRE_Match object; span=(0, 28), match='<html><h1>itcast</h1></html>'>

In [128]: s = "<html><h1>itcast</h1></h>"

In [129]: re.match(r"<(.+)><(.+)>.+</\2></\1>", s)

In [130]: s = "<html><h1>itcast</h1></html>"

In [131]: re.match(r"<(.+)><(.+)>.+</\2></\1>", s)	# 这种方法灵活，\1代表这个标签对应的第一分组标签\2依次类推
Out[131]: <_sre.SRE_Match object; span=(0, 28), match='<html><h1>itcast</h1></html>'>

**********************
案例3：邮箱地址填入字符
**********************

In [132]: p = r"(\w+)@(163|126|sina|qq|hotmail)\.(com|cn|net)"

In [133]: r = re.match(p, "xjbrhnhh@163.com")

In [134]: r
Out[134]: <_sre.SRE_Match object; span=(0, 16), match='xjbrhnhh@163.com'>

In [135]: r.group()
Out[135]: 'xjbrhnhh@163.com'

In [136]: r.group(1)	# 邮箱名内容作为一个分组
Out[136]: 'xjbrhnhh'

-----------------------------------------------------------------------------------------------------------
3.引用别名为name分组匹配到的字符串,解决分组多了记不住的问题
-----------------------------------------------------------------------------------------------------------
In [6]: re.match(r"<(?P<key1>.+)><(?P<key2>.+)>.+</(?P=key2)></(?P=key1)>", s)	# P大写的，千万注意
Out[6]: <_sre.SRE_Match object; span=(0, 28), match='<html><h1>itcast</h1></html>'>

-----------------------------------------------------------------------------------------------------------
4.search默认抓取第一个匹配对象后不再往后匹配，所以要抓取全部匹配对象就要用 5.findall
-----------------------------------------------------------------------------------------------------------
In [7]: re.search(r"itcast", s)
Out[7]: <_sre.SRE_Match object; span=(10, 16), match='itcast'>

In [8]: re.search(r"^itcast", s)

In [9]: re.search(r"^itcast$", s)

In [10]: s = "itcast</h1></html>"

In [11]: re.search(r"^itcast", s)
Out[11]: <_sre.SRE_Match object; span=(0, 6), match='itcast'>

In [12]: s = "itcast</h1></html>itheima</h1>"

In [13]: re.search(r"\w+</h1>", s)
Out[13]: <_sre.SRE_Match object; span=(0, 11), match='itcast</h1>'>

In [14]: res = re.search(r"\w+</h1>", s)

In [15]: res.group()	# \w+匹配itcast</h1>和itheima</h1>,但search只抓取第一个匹配对象
Out[15]: 'itcast</h1>'

In [22]: res = re.findall(r"\w+</h1>", s)# 这就要用到findall了

In [23]: res
Out[23]: ['itcast</h1>', 'itheima</h1>']
×××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××


In [16]: num = re.search(r"\d+", "python = 999, c = 700, c++ = 600")

In [17]: num.group()	# search只抓取第一个匹配对象
Out[17]: '999'

In [18]: num = re.findall(r"\d+", "python = 999, c = 700, c++ = 600")# 这就要用到findall了

In [19]: print(num)
['999', '700', '600']

In [21]: num
Out[21]: ['999', '700', '600']

-----------------------------------------------------------------------------------------------------------
6.sub替换匹配到的数据 split 贪婪模式
-----------------------------------------------------------------------------------------------------------

“”“
<span class="advantage">职位诱惑：</span>
        <p>提供住宿,一日三餐,晋升空间,五险一金</p>
    </dd>
    <dd class="job_bt">
        <h3 class="description">职位描述：</h3>
        <div>
        <p>职位描述:</p>
<p>高效地完成产品研发需求</p>
<p>编写易于维护的高质量代码</p>
<p><br></p>
<p>职位要求:</p>
<p>&nbsp;本科以上学历，计算机相关专业</p>
<p>&nbsp;熟练掌握 Python 语言</p>
<p>深入了解 Flask 或其他主流 Python Web 框架</p>
<p>熟悉 PostgreSQL/MySQL/redis</p>
<p>掌握基本的数据库设计能力</p>
<p>热爱编程，具备较强的编程能力和良好的编码风格</p>
<p>有较强的逻辑分析能力和学习能力</p>
<p><br></p>
<p>优先条件:</p>
<p>有自己的开源项目或为流行开源项目提交过代码<br></p>
”“”

In [3]: s = "itcast:php,python,cpp-java"

In [4]: re.split(r":|,|-", s)
Out[4]: ['itcast', 'php', 'python', 'cpp', 'java']

In [2]: s = "this is a num 234-34-4321-423"

In [3]: r = re.match(r".+(\d+-\d+-\d+-\d+)", s)

In [4]: r.group(1)
Out[4]: '4-34-4321-423'

In [5]: r = re.match(r"(.+)(\d+-\d+-\d+-\d+)", s)

In [6]: r.groups()
Out[6]: ('this is a num 23', '4-34-4321-423')

# 在* ? + {m,n}后面加上? -----------> 非贪婪

In [7]: r = re.match(r"(.+?)(\d+-\d+-\d+-\d+)", s)

In [8]: r.groups()
Out[8]: ('this is a num ', '234-34-4321-423')

In [9]: re.match(r"aa(\d+)", "aa2343ddd").group(1)
Out[9]: '2343'

In [10]: re.match(r"aa(\d+?)", "aa2343ddd").group(1)
Out[10]: '2'

In [11]: re.match(r"aa(\d+)ddd", "aa2343ddd").group(1)
Out[11]: '2343'

In [12]: re.match(r"aa(\d+?)ddd", "aa2343ddd").group(1)
Out[12]: '2343'	# 关闭了贪婪模式，还是匹配全部数字，因为前后的字母要匹配，只能把数字给中间的分组
---------------------------------------------------------------------------------
In [2]: s = "world world ha ha"

In [3]: re.split(r" +", s)
Out[3]: ['world', 'world', 'ha', 'ha']

In [4]: re.findall(r"\b[a-z][A-Z]+\b", s)	# 脑袋昏昏了
Out[4]: []

In [5]: re.findall(r"\b[a-zA-Z]+\b", s)
Out[5]: ['world', 'world', 'ha', 'ha']

