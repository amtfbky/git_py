# -*- coding:utf-8  -*-
import re

s = """<div>
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

            </div>"""

#res = re.sub(r"<.+>", "", s)
#res = re.sub(r"<\w+>", "", s)
res = re.sub(r"</?\w+>", "", s)
#res = re.sub(r"</?\w\s+>", "", s)
print(res)
