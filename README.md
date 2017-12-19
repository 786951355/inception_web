# Inception_web
本系统是MySQL自动化管理工具，配合Inception使用，基于archer进行二次开发，进行了一些补充优化。
我fork了原作者https://github.com/496080199/inception_web.git的然后修改一些小地方。

## 功能说明：
- __SQL自主审核__
- __自动审核+人工审核__
- __定时执行SQL__
- __主副人工审核__（可配置)
- __回滚sql查看与直接回滚__
- __数据库配置__
- __用户权限配置__
- __用户分配数据库权限__
- __工单查询管理__
- __工单邮件通知__（可配置）
- __查看慢查询__
- __MySQLTuner生成配置分析报告__（需安装perl)
- __SQLAdvisor语句优化功能__（安装模块）
## 配置文件：
config.py
## 安装配置：
要求：python2.7<br>
建议系统环境：CentOS 7/Ubuntu 14+

1.安装MySQL 5.6+数据库，用于存放系统数据和回滚sql。<br>
建立数据库和用户：<br>
create database inception_web character set utf8;<br>
grant all privileges on \*.\* to inception_web@'%' identified by 'inception_web';<br>
flush privileges;<br>

2.安装Inception(参考文档：http://mysql-inception.github.io/inception-document/install/ ）<br>
inc.cnf使用之前创建的mysql主机帐号密码<br>

3.下载系统源码<br>
# 源地址
#git clone https://github.com/496080199/inception_web.git<br>
git clone https://github.com/786951355/inception_web.git<br>
或使用zip包下载<br>

3.安装python2.7依赖<br>
安装pip工具，具体网上搜索(下载配置加速可参见https://pypi-mirrors.org/ ）<br>
cd inception_web<br>
pip install -r requirements.txt<br>

4.配置修改<br>
复制config_example.py为config.py<br>
根据自己的环境进行相应修改config.py中参数<br>
注：查看慢查询需设置mysql的参数log_output=table将慢查询记录输出到mysql库的slow_log表中
测试的时候发现mysql binlog的格式为ROW的时候无法生成回滚，mixed可以，但是官方说两者都可以。

5.启动运行<br>
测试环境：<br>
chmod +x debug.sh<br>
./debug.sh <br>

生产环境：<br>
chmod +x start.sh stop.sh<br>
pip install gunicorn<br>
启动：./start.sh<br>
关闭：./stop.sh<br>

6.访问<br>
原作者没有将首页跳转到Login，此处已修复
http://(部署服务器IP):5000/<br>
初始帐号密码：admin/admin<br>
注：防火墙端口5000需要放开<br>

7.依次添加数据库，开发人员（分配数据库），审核人员，开始工作。

8.模块安装<br>
SQLAdvisor安装：<br>
下载 https://github.com/Meituan-Dianping/SQLAdvisor/archive/master.zip 压缩包放至本系统根目录下，<br>
即可通过模块管理进行安装，安装需要几分钟，请耐心等待后刷新页面看到。<br>
web上直接安装SQLAdvisor没成功。。。。。

<br>
<br>
设计原理来源于archer,请大家多关注<br>
https://github.com/jly8866/archer<br>
<br>
## 系统截图:<br>
1. 发起sql工单页：<br>

![image](https://github.com/496080199/inception_web/raw/master/doc/images/%E5%8F%91%E8%B5%B7sql%E5%B7%A5%E5%8D%95.png)
<br>

2. 工单图表页：<br>

![image](https://github.com/496080199/inception_web/raw/master/doc/images/%E5%B7%A5%E5%8D%95%E5%9B%BE%E8%A1%A8.png)
<br>

3. 工单处理页：<br>

![image](https://github.com/496080199/inception_web/raw/master/doc/images/%E5%B7%A5%E5%8D%95%E5%A4%84%E7%90%86.png)
<br>

4. 工单查询页：<br>

![image](https://github.com/496080199/inception_web/raw/master/doc/images/%E5%B7%A5%E5%8D%95%E6%9F%A5%E8%AF%A2.png)
<br>

5. 待审核工单页：<br>

![image](https://github.com/496080199/inception_web/raw/master/doc/images/%E5%BE%85%E5%AE%A1%E6%A0%B8%E5%B7%A5%E5%8D%95.png)
<br>

6. 登陆页：<br>

![image](https://github.com/496080199/inception_web/raw/master/doc/images/%E7%99%BB%E9%99%86%E9%A1%B5.png)
<br>

7. 管理员主页：<br>

![image](https://github.com/496080199/inception_web/raw/master/doc/images/%E7%AE%A1%E7%90%86%E5%91%98%E4%B8%BB%E9%A1%B5.png)
<br>

8. mysqltuner配置分析报告：<br>

![image](https://github.com/496080199/inception_web/raw/master/doc/images/%E9%85%8D%E7%BD%AE%E6%8A%A5%E5%91%8A.png)
<br>

9. SQLAdvisor语句优化：<br>

![image](https://github.com/496080199/inception_web/raw/master/doc/images/SQLAdvisor.png)
<br>

