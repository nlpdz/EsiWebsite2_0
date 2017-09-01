# Connor使用手册
> 简介：Connor是一款统计在ESI数据库中WUST师生论文情况的web site
他使用Django框架搭建web站点，后台Python完成基本爬虫功能。
请配合使用Django与Python2.7的文档。

## 快速开始
1. 克隆项目：
```
git clone https://github.com/uk9921/ESIwebsite.git
```
2. 安装pip，通过pip安装Django：

```
pip install Django
```
3. 进入到ESIwebsite根目录，运行命令：

```
python manage.py runserver
```
4. 访问登陆界面，地址为：

```
127.0.0.1:8000/login
```
## 目录说明

```
├──ESIwebsite-----------------------------根目录
├────Conner-------------------------------咱们的APP
├     └──migrations-----------------------数据库迁移文件
├────ESIwebsite---------------------------Django项目的心脏
├────spider-------------------------------爬虫们
├────static-------------------------------静态文件目录
├     └──css------------------------------样式们
├     └──imgs-----------------------------图片们
├     └──js-------------------------------js们
├     └──plugins--------------------------插件们
├────templates----------------------------html们
├────db.sqlite3---------------------------数据库
├────manage.py----------------------------入口
├────README.md----------------------------广告

```
## 开发流程
1. 创建页面  
Templates文件夹下创建html页；
views.py中return页面；
urls.py中注册路径；

2. 创建model  
models.py中建类
确定settings中注册app；
python manage.py makemigrations（保存临时）；
python manage.py migrate（真正创建）；
在views.py中实现相关功能；

3. 修改model  
在models.py中修改；
python manage.py makemigrations；
python manage.py migrate；
更新model失败：给字段增加参数null=True，重新运行；

4. 静态文件更新不及时  
静态目录被访问多次后会加入缓存，可以修改一下静态文件名（推荐增加前缀）

5. 注册管理员  

```
    python manage.py createsuperuser
```
6. 注册管理员站点  
修改admin.py，其中UserInfo是表，Connor是app名字

```
    from django.contrib import admin
    from Connor.models import UserInfo
    
    admin.site.register(UserInfo)
```
7. 输入网址访问本地后台管理

```
    120.0.0.1/admin
```
8. 增添爬虫  
在spider中修改或增加爬虫，在views中调用爬虫并获得返回值，在views中插入到数据库。
在爬虫中使用model：
```
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ESIwebsite.settings")
    import django
    django.setup()
    from Connor.models import Dissertation,refer

```
------------
v1.0.2版本新增爬虫功能：  
`selenium+PhantomJS 执行页面筛选项JS`  
`断线重连，超时重连、结束会话重连` 
 
***未提及的部分请善用开源Django文档以及网络。***
