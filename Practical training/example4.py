#1、阶乘求和
# n=eval(input("请输入正整数："))
# s=0
# for i in range(1,n+1):
#     q=1
#     for j in range(1,i+1):
#         q=q*j
#     s=s+q
# print(s)

#2、鸡兔同笼问题

# 鸡兔同笼，头35个，脚94只，问鸡、兔各多少？

# XrabFeet = 35*4         #假设笼子里都是兔子，一共有多少只脚
# ChickenFeet = XrabFeet-94
# chickens = ChickenFeet/2
# rabbits = 35-chickens
# print(f"鸡有: {int(chickens)}个")
# print(f"兔子有: {int(rabbits)}个")

# nHead=35
# nLeg=94
# for i in range(nHead+1):         #假设兔子有i只
#     nChick=nHead-i         #鸡的只数
#     if i*4+nChick*2==94:         #如果兔子和鸡的脚的总数和为94.
#         print('兔子有{}只,鸡有{}只'.format(i,nChick))

#3、字符串的使用
# k='ssd mobilenet.xml'
# print('filename:{}'.format(k[0:13]))
# print('ext:{}'.format(k[14:]))
#
# str1='ssd_mobilenet.xml'
# nid=str1.index('.')         #或者str1.find('.')#获取某字符的索引号 #查找字符串的位置
# filename=str1[0:nid]
# ext=str1[nid+1:]
# print('文件名：',filename,'的后缀为：',ext,sep="")

#4、进度条打印
# import time
# nL=80         #表示显示的长度
# s1="开始下载"
# s2="下载完成"
# print("{0:=^{1}}".format(s1,nL))
# nL+=len(s1)-6
# nT=0
# for i in range(1,nL+1):
#     nT=i/nL
#     print("\r{:3.0%}[{}{}]".format(nT,i*'*',(nL-i)*"."),end="")
#     time.sleep(0.1)
# print("\n{0:=^{1}}".format(s2,nL+2))

#5、两层循环+分支语句，输出如下图像
# n=int(input('请输入正方形的边数:'))
# print(' * '*n)
# for i in range(n-2):
#     print(' *','   '*(n-2),'*')
# print(' * '*n)

#6、圆周率的近似计算
pi = 0
N = 1000
for k in range(N):
    pi += 1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
print("圆周率值为：{}".format(pi))

#7、蒙特卡罗方法
import random

