# 练习：
#     获取用户输入的个人信息：并且存储到字典中
#     个人信息包括：name,age,sex

a=input("请输入您的名字: ")
b=input("请输入您的性别：")
c=input("请输入您的年龄：")
PersonalData={"name":a,"age":b,"sex":c}
print(PersonalData)

print("________________________________________________")

A={}
A.update(name=input("姓名："))
A.update(sex=input("性别："))
A.update(age=input("年龄："))
print(A)
