a=1     #以下列出三种较为常见的判断写法
b=2
if a==1 :
    print("hhhhhh")


if a>b :
    print("a比b大")   #必须换行，而且空4格，即为缩进 代表代码块
else :
    print("b比a大")


age=int(input("请输入你的年龄："))  # input获取的都是字符串 切记
if age>60 :
    print("你该退休了")
elif age>30 :
    print("你的责任应该很重吧")
elif age>20 :
    print("你该好好规划职业生涯了")
else:
    print("好好学习")


print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

#in
a = "你好"
if a in "你好！吃了吗？":
    print("OK")
else:
    print("不OK")
