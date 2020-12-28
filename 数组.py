# 数组和元组的区别： 元组写好了不可以修改，而数组可以修改
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