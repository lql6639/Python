# 基本统计值计算

def average_value(n):         # 平均值
    average = sum(n) / len(n)
    return average

def median_value(n):         #中位数
    n.sort()
    length = len(n)
    if length % 2 == 0:
        median = (n[length//2-1] + n[length//2]) / 2
    else:
        median = n[length//2]
    return median

def standard_value(n,average):         #标准差
    stan = 0
    for num in n:
        stan = stan + (num - average)**2
    standard = pow(stan / (len(n)-1),0.5)
    return standard

def variance_value(n):         #方差
    average = average_value(n)
    vary = 0
    for num in n:
        vary = (num - average)**2
    vary /= len(n)
    vary = vary**0.5
    return vary

list = [17,19,23,26,30,34]

average = average_value(list)         # 平均值

median = median_value(list)         #中位数

standard = standard_value(list,average_value(list))         #标准差

variance = variance_value(list)         #方差

print("平均值:{:.2f},中位数:{},标准差:{:.2f},方差:{:.2f}".format(average,median,standard,variance))

