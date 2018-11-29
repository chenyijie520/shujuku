def get_user_pass(file):
	user_passwd = {}
	with open(file,'r') as f:
		for d in f:
			for kv in [d.strip().split(',')]:
				user_passwd[kv[0]]=kv[1]
	return user_passwd
# 定义一个函数，判断输入的参数是否为空，为空的话继续输入，直到输入不为空为止
def input_data(data_type,get_data):
	while True:
		get_data=input('请输入%s：'%data_type)
		if len(get_data)==0:
			continue
		else:
			break
		return get_data
user_pass =get_user_pass('1.txt')
while True:
	username=input_data('注册账号','name')
    # 判断注册账号是否存在，已存在的话持续循环
	if username in user_pass.keys():
		print('您输入的账号已存在，请重新输入：')
		continue
	else:
		password = input_data('账号密码', 'name')
		confirm_pass=input_data('确认密码','name')
   # 判断确认密码和密码是否一致
		if password!=confirm_pass:
			print('您输入的确认密码与密码不一致，请重新输入:')
			continue
		else:
			print('恭喜您注册成功，请记住您的注册信息：\n您的账号是:%s\n您的密码是:%s'%(username,password))
			break
#将新注册的用户写入expandtion.txt保存
with open('1.txt', 'a') as f:
	f.write(username+','+password+'\n')
user_pass =get_user_pass('1.txt')
#设置i用来记录登录信息输入错误次数啊
i=1
while i<4:
	print('第%s次登录,登录超过三次仍然失败，将不允许登录,'%i)
	i+= 1
	get_user=input('please input username:')
	get_pass=input('please input password:')
     #判断账号是否存在expandtion.txt文件中
	if get_user not in user_pass.keys():
		print('账号或密码有误，请重新输入！')
		continue
	else:
       #根据账号获取到该账号的密码
	   	password = user_pass[get_user]
         # 判断密码是否和对应的账号匹
		if get_pass!=password:
             print('账号或密码有误，请重新输入！')
             continue
			 
		else:
             print('欢迎%s登录！'%get_user)
             break
#登录超过三次时给出提示
else:
	print('账号或密码错误次数已超过三次，请明年再来登录！')
