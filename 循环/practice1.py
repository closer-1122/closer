"""
练习1：
通过print打印，模拟一个红绿灯的功能，注意：红灯30次，绿灯35次，黄灯3次(黄灯位于绿末红初之间)
"""
for green in range(1,36):
    print("绿灯还有：",36-green,"秒")
print("-------------------------------------")

for yellow in range(1,4):
    print("黄灯还有：",4-yellow,"秒")
print("-------------------------------------")
for red in range(1,31):
    print("红灯还有：",31-red,"秒")
print("-------------------------------------")


# 另一种方法 字典的方法
while True: # 死循环
    light={"红灯":30,"绿灯":35,"黄灯":3}  # 可维护性高 
    for i in light:      #这里的i取值为字典里的key 而不是value
        for j in range(light[i]):
            print(i," 倒计时 ",light[i]-j,"秒")