# 1、计算某班级学生考试的平均分
# # 定义计算班级平均数
# def avgScore(scores,n=10):
#     score = 0
#     for i in range(len(scores)):
#         score += scores[i]
#     return score/n
# # 主程序
# scores=[90,88,76,45,77,95,66,88,91]
# # 按班级人数计算平均值并打印
# print("按班级人数计算的平均值:{:.2f}".format(avgScore(scores)))
# # 按实际考试人数计算平均值并打印
# print("按考试人数计算的平均值:{:.2f}".format(avgScore(scores,len(scores))))

# 2、基本数据统计
import random
lst = []
for i in range(10):
    lst.append((random.randint(75,100)))

def avg(ln):
    nAvg = sum(ln) / len(ln)
    return nAvg

def var(ln):
    nAvg=avg(ln)
    tAvr=0
    for item in ln:
         tAvr=(item-nAvg)**2
    tAvr/=len(ln)
    tAvr=tAvr**0.5
    return tAvr

def medin(ln):
    ln.sort()
    n=len(ln)
    if n % 2 == 1:
        medin=ln[int(n / 2)]
    else:
        medin=(ln[int(n / 2)] + ln[int(n / 2) - 1]) / 2
        return medin
print(f"该列表{lst}的基本数据统计如下:\n平均值是{avg(lst):.2f},方差是{var(lst):.2f},中位数是{medin(lst):}")

# 3、利用可变参数计算一组数的平均值
# def maxnum(*nums):
#     l = len(nums)
#     sum = 0
#
#     if l == 0:
#         return 0.0
#
#     i = 0
#     while i < l:
#         sum += nums[i]
#         i += 1
#
#     return sum*1.0/l
#
# print(maxnum(-1,34,-9,56))
# print(maxnum(1,4,95,3,78))

# 4、求和
# n = int(input("输入一个数:"))
# def i(n):
#     a=1
#     sum=0
#     for b in range(1,n+1):
#         a = a*b
#         sum +=a
#     return sum
# print(i(n))

