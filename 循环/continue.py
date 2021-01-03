for i in range(10):
    if i==5:
        continue # 会跳过5
    print(i)

for i in range(10):
    if i==5:
        break # 会跳出 只针对一层循环生效
    print(i)
print("************************************")
for a in range(1,10):
    for b in range(1,a+1):
        if a==3 :
            break
        print(b,"X",a,"=",b*a,end="  ")  # end 控制其不换行，并以end=" " 引号中的数据结尾
    print() #相当于换行