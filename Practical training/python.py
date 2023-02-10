# 基本统计值计算
#
# def average_value(n):         # 平均值
#     average = sum(n) / len(n)
#     return average
#
# def median_value(n):         #中位数
#     n.sort()
#     length = len(n)
#     if length % 2 == 0:
#         median = (n[length//2-1] + n[length//2]) / 2
#     else:
#         median = n[length//2]
#     return median
#
# def standard_value(n,average):         #标准差
#     stan = 0
#     for num in n:
#         stan = stan + (num - average)**2
#     standard = pow(stan / (len(n)-1),0.5)
#     return standard
#
# def variance_value(n):         #方差
#     average = average_value(n)
#     vary = 0
#     for num in n:
#         vary = vary + ((num - average)**2) / len(n)
#     vary = vary**0.5
#     return vary
#
# list = [70,76,78,79,82,83,89]
#
# average = average_value(list)         # 平均值
#
# median = median_value(list)         #中位数
#
# standard = standard_value(list,average_value(list))         #标准差
#
# variance = variance_value(list)         #方差
#
# print("平均值:{:.2f},中位数:{},标准差:{:.2f},方差:{:.2f}".format(average,median,standard,variance))





def numbers_value(n):         # 总个数
    length = len(n)
    return length

def sum_value(n):         # 总和
    sums = sum(n)
    return sums

def average_value(n):         # 平均值
    average = sum(n) / len(n)
    return average

def variance_value(n):         #方差
    average = average_value(n)
    vary = 0
    for num in n:
        vary = vary + ((num - average)**2) / len(n)
    vary = vary**0.5
    return vary

def median_value(n):         #中位数
    n.sort()
    length = len(n)
    if length % 2 == 0:
        median = (n[length//2-1] + n[length//2]) / 2
    else:
        median = n[length//2]
    return median

list = [70,76,78,79,82,83,89]

print("列表{}的概要统计如下：\n总个数:{}\n总和:{}\n平均值:{:.2f}\n方差:{:.2f}\n中位数:{}".
      format(list,numbers_value(list),sum_value(list),average_value(list),variance_value(list),median_value(list)))

