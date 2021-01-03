# 练习2：
# 使用代码，实现一个注册功能。
# 用户输入账号和密码，要求账号长度是5-8位，密码6-12位，并且账号必须小写开头。(账号开头必须小写不会)
# 储存到字典中，{username:passward}
a={}
username=input("请输入你的账号：")
while len(username)<5 or len(username)>8:
    username=input("请输入长度是5-8位的账号：")
passward=input("请输入密码：")
while len(passward)<6 or len(passward)>12:
    passward=input("请输入长度是6-12位的密码：")
a[username]=passward
print(a)


# 修改
username=input("请输入用户名：")
password=input("请输入密码：")
if len(username)>=5 and len(username)<=8:
    if username[0] in "qwertyuiopasdfghjklzxcvbnm":
        if len(password)>=6 and len(password)<=12:
            print("注册成功",{username:password})
        else:
            print("请输入符合规范的密码：密码6-12位")
    else:
        print("账号没有以小写开头")
else:
    print("请输入符合规范的用户名：要求账号长度是5-8位")