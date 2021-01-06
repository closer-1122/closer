"""
class 声明类的名字
类名首字母必须大写
面向对象编程
类里面所有的方法，都必须要传一个参数，叫self
"""
class GirlFriend():
    """
    女朋友
    """
    def __init__(self):  # 初始化 属性
        self.sex = "女"
        self.age = "18岁"
        self.height = "160cm"
        self.weight = "50kg"

    def caiyi(self,num):
        """
        才艺表演
        """
        print("你的身高"+self.height+"体重"+self.weight+"年龄"+self.age+"性别"+self.sex+"的女朋友开始才艺表演")
        if num == 1:
            print("胸口碎大石")
        elif num == 2:
            print("唱跳RAP篮球")
        else:
            print("单手开瓶盖")
    
    def chuyi(self):
        """
        厨艺
        """
        print("你的身高"+self.height+"体重"+self.weight+"年龄"+self.age+"性别"+self.sex+"的女朋友开始做饭")
        print("八大菜系，样样精通，中西融合，秀外慧中，啥都会")
    

    def work(self):
    
        """
        工作
        """
        print("你的身高"+self.height+"体重"+self.weight+"年龄"+self.age+"性别"+self.sex+"的女朋友开始工作")
        print("开挖掘机!")


#类的实例化
shierly = GirlFriend()
shierly.caiyi(1)
shierly.work()
print(shierly.age)