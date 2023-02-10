#1、说句心里话
# name=input("请输入你的名字：")
# speak=input("心里话：")
# content=name+"，我想对你说："+speak
# print(content)

#2、N的多次方
# n=eval(input("请输入一个数（整数、浮点数）："))
# print(n**0,n**1,n**2,n**3,n**4,n**5)
# for i in range(6):
#     print(n**i,end=" ")

#3、计算5种数学运算结果
#M与N的和、M与N的乘积、M的N次幂、M除N的余数、M和N中较大的值

#4、累和操作
n=eval(input("请输入一个正整数："))
sum=0
for i in range(1,n+1,1):
    sum+=i
print(sum)

