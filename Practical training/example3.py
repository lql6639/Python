#1、猜数字
# import random
# tN=random.randint(0,100)
# frequency_num=1
# while True:
#     myN=eval(input("请输入一个0~100的正整数："))
#     if myN>tN:
#         print("很遗憾，你猜大了！")
#         frequency_num += 1
#     elif myN<tN:
#         print("很遗憾，你猜小了！")
#         frequency_num += 1
#     else:
#         print("恭喜，猜数成功！",end="")
#         print("您一共猜了",frequency_num,"次！")
#         break

#2、逢7拍手游戏
# for i in range(1, 101):
#     if i%7==0 or '7' in str(i):
#         print("**",end="\t")
#     else:
#         print(i,end="\t")
#     if i % 10 == 0:
#         print()

#3、用户输入整数n，输出打印如下图形
# m=eval(input('请输入行数：'))
# for i in range(1,m+1):
#     for x in range(1,2*i):
#         print('*',end='')
#     print()
#
# a=eval(input('请输入行数：'))
# for a in range(1,a+1):
#     while a:
#         print((2*a-1)*'*')
#         break

#4、九九乘法表的打印

#九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f'{j}*{i}={i*j}\t', end='')
#     print()
#
#九九乘法表
# i = 1
# while i <= 9:
#     j = 1
#     while(j <= i):    # j的大小是由i来控制的
#         print(f'{j}*{i}={i*j}', end='\t')
#         j += 1
#     print('')
#     i += 1

#5、*形图的绘制

#只限奇数输入
# while True:
#     n=eval(input("请输入一个奇数："))
#     if n%2!=0:
#         break
# for i in range(1,n+1):
#     if i<=n/2+1:
#         print(((2*i-1)*"*").center(n))
#     else:
#         print(((2*(n-i)+1)*"*").center(n))

#奇数、偶数都可
n = eval(input("请输入输出行数："))
if n%2:
    for i in range(1,int(n/2+1.5)):
        for j in range(0,int(n/2-i+1)):
            print(" ",end="")
        for k in range(1,i*2):
            print("*",end="")
        for l in range(0,int(n/2-i+1)):
            print(" ",end="")
        print("")
    for i in range(1,int(n/2+0.5)):
        for j in range(0,i):
            print(" ",end="")
        for k in range(1,int(n/2-i+0.5)*2):
            print("*",end="")
        for l in range(0,i):
            print(" ",end="")
        print("")
else:
    for i in range(1,int(n/2+1)):
        for j in range(0,int(n/2-i)):
            print(" ",end="")
        for k in range(1,i*2):
            print("*",end="")
        for l in range(0,int(n/2-i)):
            print(" ",end="")
        print("")
    for i in range(1,int(n/2+1)):
        for j in range(1,i):
            print(" ",end="")
        for k in range(1,int((n/2-i+1)*2)):
            print("*",end="")
        for l in range(1,i):
            print(" ",end="")
        print("")

