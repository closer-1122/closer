# 数组和元组的区别： 元组写好了不可以修改，而数组可以修改  python里是list  所以翻译为列表
a = [1,2,3,"哈哈","哈哈","哈哈","嘻嘻",True,False]

# append方法追加数据
a.append("追加的数据")
print(a)
#运行结果如下
#C:\workhome\github\closer>python 数组.py
#[1, 2, 3, '哈哈', '哈哈', '哈哈', '嘻嘻', True, False, '追加的数据']


#指定位置插入数据
a.insert(0,"insert")
print(a)


# a.pop(下标) 类似于剪切

# a.clear()  清空a数组


# extend（）
xx=["你好","不好"]
a.extend(xx)
print(a)

# 也可以通过以下方式实现  
cc=["你吃了吗","吃了"]
print(a+cc) #类似于数组拼接

# remove() 删除某个数据
c = [1,2,3,"哈哈","哈哈","哈哈","嘻嘻",True,False]
print(c)
c.remove(2)   # 注意：如果remove() 中取值是0或1则会删除 数组里的False或者True
print(c)

"""
注意事项 ： 下标不要超出范围——越界
关于括号： 所有方法都以小括号结尾 如print() input() len() ...
 元组、数组、字典的取值都用中括号 []  如 a[0]
"""

