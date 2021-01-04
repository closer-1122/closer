def checkusername(username):
    """
    自动判断账号是否是5-8位，且以小写首字母开头
    """
    if len(username)>=5 and len(username)<=8:
        if username[0] in "qwertyuiopasdfghjklzxcvbnm":
            print("用户名OK")
        else:
            print("账号没有以小写开头")
    else:
        print("请输入符合规范的用户名：要求账号长度是5-8位")

checkusername("1busabi")

#def 方法的声明
#checkname 方法名
#（）方法参数
# """
# 方法的说明
# """

