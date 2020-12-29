"""
字典的特点：
  1、字典中的值没有顺序
  2、字典的结构必须是键值对  key：value
"""
a={"name":"张三","表情":"哈哈","年龄":"22"}  # 相当于把数组里的下标自定义了, 另外字符串在任何地方都要加引号
print(a)

#取值
print(a["name"])

#新增
a["height"]="183cm"
print(a)

#修改
a["name"]="closer"
print(a)

# get方法
b=a.get("name")
print(b)


print("-------------------------------------")

# updata
print(a)
c=a.update(name="倾心淡雪")
print(a)

print("-------------------------------------")

# get 和 直接打印取值的区别：
print(a)
print(a.get("name"))
print(a["name"])
#{'name': '倾心淡雪', '表情': '哈哈', '年龄': '22', 'height': '183cm'}
#倾心淡雪
#倾心淡雪             可以看出运行结果一致
# print(a)
# print(a.get("name11"))
# print(a["name11"])
# None
# Traceback (most recent call last):
#   File "字典.py", line 43, in <module>
#     print(a["name11"])
# KeyError: 'name11'       可以看出 用get方法 显示为空  而用key值方法则报错

print("——————————————————————————————————————————————————————")

# pop方法切片
print(a)
b=a.pop("name")
print(b)
print(a)