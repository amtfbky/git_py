mkvirtualenv xxx
workon xxx
pip list
pip freeze
pip install django==1.8.2
django-admin startproject 项目名
deactivate

MVC model 对数据库层的封装，模型？
    view 向用户展示结果，模板
    controller 核心，处理请求、获取数据、返回结果
核心思想：解耦，降低各功能之间的耦合性，方便变更，更容易重构代码，最大程度上实现代码的重用

高可扩展性
向后兼容
低耦合 高内聚

MVT model 与数据库交互
    view 核心，接收请求、获取数据、返回结果
    template 呈现内容到浏览器

第一步：客户端向视图view发送请求
第二步：view向model模型发送客户端请求
第三步：模型model从数据库获取数据
    第1小步：
    第2小步：
第四步：view从模型接收数据后传给模板template
第五步：模板template处理后返回内容到view
第六步：view最终给客户端返回内容

视图view：
    接收请求，逻辑处理，调用数据，输出响应
    配置URL：在自己的应用中配置正则URL（正则表达式,视图的名称）

--------------------------------------------------------------
模型Model：负责与数据库交互
面向对象：模型对象，列表
    定义模型类：指定属性及类型，以确定表的结构，迁移
    后台管理：创建管理员，启动服务器，admin，注册admin.py

模板Template：
    定义显示的样子
    加载：读取文件的内容到内存
    渲染：填坑
--------------------------------------------------------------
一、模型
开发流程：
1.创建虚拟环境
2.安装django
3.创建项目
4.创建应用
5.在models.py中定义模型类
6.定义视图
7.配置url
8.创建模板

过程中5-8重复

pip install mysql-python

django-admin startproject test2
cd test2
python manage.py startapp booktest
cd booktest
vi models
cd test2
python manage.py makemigrations
python manage.py migrate

mysql> show tables;
+----------------------------+
| Tables_in_test2            |
+----------------------------+
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| bookinfo                   |
| booktest_heroinfo          |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
+----------------------------+
mysql> desc bookinfo;
+----------+-------------+------+-----+---------+----------------+
| Field    | Type        | Null | Key | Default | Extra          |
+----------+-------------+------+-----+---------+----------------+
| id       | int(11)     | NO   | PRI | NULL    | auto_increment |
| btitle   | varchar(20) | NO   |     | NULL    |                |
| pub_date | datetime(6) | NO   |     | NULL    |                |
| bread    | int(11)     | NO   |     | NULL    |                |
| bcommet  | int(11)     | NO   |     | NULL    |                |
| isDelete | tinyint(1)  | NO   |     | NULL    |                |
+----------+-------------+------+-----+---------+----------------+


