"""
练习：
现在有多个学生的成绩，需要录入到系统中。
这些人分别是：张三、李四、王麻子、流云、浪晋、希希、小梁、二狗、陈平安、朱珠、亚索
而且名字和成绩要对应上。
而且大于60的和小于60的需要分开存放
"""
studentlist=["张三","李四","王麻子","流云","浪晋","希希","小梁","二狗","陈平安","朱珠","亚索"]
a=0
highchengji={}
lowchengji={}
while a < len(studentlist):
    chengji=int(input("请输入"+studentlist[a]+"的成绩："))
    if chengji >= 60:
        highchengji[studentlist[a]]=chengji
    else:
        lowchengji[studentlist[a]]=chengji
    a=a+1
print("大于60的成绩",highchengji)
print("小于60的成绩",lowchengji)