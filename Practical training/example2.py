#1、计算矩形面积
# l=eval(input("请输入矩形的长："))
# w=eval(input("请输入矩形的宽："))
# sum=round(l*w,2)         #保留两位小数
# print("此矩形的面积为：",sum,sep="")

#2、温度转换
#温度转换的初级做法
#华氏温度转摄氏温度
# f=eval(input("请输入华氏温度值："))
# c=(f-32)/1.8
# print("转换后的摄氏温度值为：%.2f"%c)
#高阶实现方式
# num=input("请输入一个带单位的温度值，例如：36.5C、86.7F等：")
# r=num[-1]         #获取字符串最后一位
# n=num[:-1]         #获取除最后一位以外的数字
# n=eval(n)
# if r=="C" or r=="c":
#     F=round(n*1.8+32,2)
#     print("转换后的华氏温度值为：",F,"F",sep="")
# elif r=="F" or r=="f":
#     C=round((n-32)/1.8,2)
#     print("转换后的摄氏温度值为：",C,"C",sep="")
# else:
#     print("请输入带单位的温度值！！！")

#3、BMI指数计算
# h=eval(input("请输入身高（m）："))
# w=eval(input("请输入体重（kg）："))
# bmi=w/h**2
# print("体质指数（BMI）值为：",bmi,sep="")
# if bmi<18.5:
#     print("国内标准：偏瘦","国际标准：偏瘦")
# elif bmi>=18.5 and bmi<=24:
#     print("国内标准：正常","国际标准：正常")
# elif bmi>24 and bmi<28:
#     print("国内标准：偏胖")
#     if bmi>24 and bmi<25:
#         print("国际标准：正常")
#     else:
#         print("国际标准：偏胖")
# else:
#     print("国内标准：偏胖")
#     if bmi>=25 and bmi<30:
#         print("国际标准：偏胖")
#     else:
#         print("国际标准：肥胖")

#4、计算圆锥体体积
# import math
# r=eval(input("请输入圆锥体的半径："))
# h=eval(input("请输入圆锥体的高："))
# v=round((math.pi*r*r*h)/3,2)         #保留两位小数
# print("此圆锥体的体积为：",v,sep="")

#5、闰年的判断
# year=eval(input("请输入年份：",))
# if year%4==0 and year%100!=0 or year%400==0:
#     print(year,"是闰年！")
# else:
#     print(year,"年是平年！",sep="")

#6、计算并输出方程的实数根
#输入:一元二次方程ax²+bx+c=0参数a、b、c；
import math
a=eval(input("请输入a的值："))
b=eval(input("请输入b的值："))
c=eval(input("请输入c的值："))
bt=b**2-4*a*c
if bt>0:
    x1=(-b+math.sqrt(bt))/2*a
    x2=(-b-math.sqrt(bt))/2*a
    print("此方程实数根x1=：",round(x1,2),sep="")         #保留两位小数
    print("此方程实数根x2=：",round(x2,2),sep="")         #保留两位小数
elif bt<0:
    print("此方程没有实数根")
else:
    x=-b/2*a
    print("此方程只有一个实数根x=：",round(x,2),sep="")         #保留两位小数

