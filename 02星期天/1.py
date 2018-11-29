注册
#先使用pymysql
import pymysql
import re
#创建一个mysql 连接
#:param host: Host where the database server is located(连接数据库时用的ip)
#:param user: Username to log in as(登陆的用户名))
#:param password: Password to use.(登陆的密码)
#:param database: Database to use, None to not use a particular one.(设置你要操作的数据库)
#:param port: MySQL port to use, default is usually OK. (default: 3306)(设置端口号)
#:param charset: Charset you want to use.(设置你想使用的字符集)
mysql1=pymysql.connect(host='localhost',user='root',password='cyj5201314',database='02xingqi',charset='utf8')
#创建游标
cursor=mysql1.cursor()
username=str(input('请输入用户名:'))
while True:
    if len(username)>5:
        print('用户名最多五个字,请重新输入:')
        username=str(input('请输入用户名:'))
    elif len(username)<2:
        print('用户名最少２个字,请重新输入:')
        username=str(input('请输入用户名:'))
    elif len(username)>=2 and len(username)<=5:
       # print('哦了')
        break       

#查看数据
sql="""
    select * from homework where uname=%s
"""

#执行sql语句
cursor.execute(sql,[username])
#判断用户名是否存在
while len(cursor.fetchall())>0:
    username=input('该用户名已存在请重新输入:')
    sql="""
    select * from homework where uname=%s
"""
    cursor.execute(sql,[username])

pwd=input('请输入密码:')
#sub_str=pwd
#ret=re.match('[a-z][A-Z][1-9]{6,18}|[a-z][1-9][A-Z]{6,18}|[A-Z][a-z][0-9]{6,18}|[A-Z][0-9][a-z]{6,18}|[0-9][A-Z][a-z]{6,18}|[0-9][a-z][A-Z]{6,18}',pwd)

while len(pwd)<8:#密码长度判断
    pwd=input("密码少于八位，不安全请重新输入：")
ret=re.findall('[A-Z]',pwd)
while len(ret)<=0:#判断是否有大写字母
    pwd=input("密码没有大写字母，不安全请重新输入：")
    ret=re.findall('[A-Z]',pwd)
ret=re.findall('[a-z]',pwd)
while len(ret)<=0:#判断是非有小写字母
    pwd=input("密码没有小写字母，不安全请重新输入：")
    ret=re.findall('[a-z]',pwd)

pwd2=input('请确认密码:')
while True:#判断确认密码
    if pwd!=pwd2:
        print('密码输入错误．请重新输入')
        pwd2=input('请确认密码:')
    elif pwd==pwd2:
        break

email=input('请输入email:')
gender=int(input('请输入性别[1男,0女]:'))
age=int(input('请输入年龄:'))

sql="""
    insert into homework(utoken,uname,uemail,ugender,uage,upassword)
    values(%s,%s,%s,%s,%s,%s)
"""


#提交数据
cursor.execute(sql,[username,username,email,gender,age,pwd])
mysql1.commit()
