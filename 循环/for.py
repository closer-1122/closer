# 遍历 会逐字的查询
a="你好！今天你吃了吗？"
for i in a :
    print(i)

#range
b=list(range(0,100))  #左闭右开
print(b)

for i in range(100):
    print(i)

#步进
b=list(range(0,100,2))  # 会打印出 0,2,4,6,8 等等 以2位间隔
print(b)

"""
练习：
现在有多个学生的成绩，需要录入到系统中。
这些人分别是：张三、李四、王麻子、流云、浪晋、希希、小梁、二狗、陈平安、朱珠、亚索
而且名字和成绩要对应上。
而且大于60的和小于60的需要分开存放
"""
studentlist=["张三","李四","王麻子","流云","浪晋","希希","小梁","二狗","陈平安","朱珠","亚索"]
highchengji={}
lowchengji={}
for i in studentlist:
    chengji=int(input("请输入"+i+"的成绩："))
    if chengji >= 60:
        highchengji[i]=chengji
    else:
        lowchengji[i]=chengji
print("大于60的成绩",highchengji)
print("小于60的成绩",lowchengji)