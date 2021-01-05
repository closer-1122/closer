"""
比如有一些苹果
无返回值就像我只能把苹果给你看 仅仅是看看
而有返回值就像把苹果给你了 你想拿这些苹果干什么都可以
"""
def jiafa(a,b):
    """
    实现两个数相加
    """
    if type(a) is int and type(b) is int:
        print(a+b)  # 要想有返回值 可以改为 return a+b
    else:
        print("请输入正确的数值")   # return "请输入正确的数值"
print(a.append("哈哈")) # None 因为append 这个函数没有返回值 
print(a.count("哈哈"))  # 1  count有返回值
print(jiafa(2,4))  # 6 ：因为jiafa里有print结果  None ：但是jiafa这个函数没有返回值 所以是None
#运行结果如下
# None
# 1
# 6
# None