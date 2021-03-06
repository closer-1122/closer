#元组，下标，从0开始标号，也可以从右开始 从-1开始编号
a = (1,2,3,"哈哈","嘻嘻",True,False)
print(a[4])  #代表打印第五位

# 如果元组中的数据太多，无法直接数出目标数据的下标，可以通过查询方法获取下标
print(a.index("嘻嘻"))

"""
运行结果如下：
C:\workhome\github\closer>python 元组.py        
嘻嘻
4
"""

# 如果要查找的数据有多个  查出的下标则是最前面的一个
b = (1,2,3,"哈哈","哈哈","哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False)
print(b.index("哈哈"))  # 查询该数据的下标
print(b.count("哈哈"))  # 统计哈哈的数量


# 切片  将b = (1,2,3,"哈哈","哈哈","哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False) 分组
print(b[0:6])  #即可打印编号0-5的数据，运行结果只显示前6个数据  因为左闭右开
print(b[6:9])
print(b[9:])   # 最后个编号可以不写  当然 第一个编号也可以不写
print(b[:])
print(b)       # 这两条程序结果一样

