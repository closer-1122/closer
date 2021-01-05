try:
    print("s"+1)  #如果代码正确 则执行 不正确则执行下面的
except :
    print("这行代码写错了")

#  包->类->方法->变量
#  既包含又并列的关系
#  异常类就是用来处理代码报错的

# 当无法判断用户输入的数据是否正确的情况下，可以用 try except
# 处理用户的数据

a=input("清输入您的名字")
b=input("请输入您的年龄")
try :
    if int(b)>18 :
        print(a,"成年了")
    else:
        print(a,"未成年")
except:
    print("未输入正确的年龄")