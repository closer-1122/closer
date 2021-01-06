"""
定义一个方法，判断用户输入的账号密码是否符合规范
"""
def checkusername(username,password):
    if len(username)>=5 and len(username)<=8:
        if username[0] in "qwertyuiopasdfghjklzxcvbnm":
            if len(password)>=6 and len(password)<=12:
                return "注册成功"
            else:
                return "密码必须是6-12位"
        else:
            return "账号必须以小写字母开头"
    else:
        return "账号必须是5-8位"
print(checkusername("龚智勇","123456789"))