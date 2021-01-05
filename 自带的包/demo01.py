# python自带的包可以直接导出
import time
import random #随机数
import pymysql
# 导入的包习惯写在最上方
for i in range(10):
    time.sleep(1)  #停顿1秒
    print(10-i)


# random 生成随机数
a = random.randint(10,100)
print(a)