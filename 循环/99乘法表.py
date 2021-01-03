# 练习 打印99乘法表
for a in range(1,10):
    for b in range(1,a+1):
        print(b,"X",a,"=",b*a,end="  ")  # end 控制其不换行，并以end=" " 引号中的数据结尾
    print() #相当于换行

# end 的用法
a = ["张三","李四","王麻子","流云","浪晋","希希","小梁","二狗","陈平安","朱珠","亚索"]
for i in a:
    print(i)


for i in a:
    print(i,end=" 你好！")