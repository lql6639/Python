# 1、凯撒加解密算法的实现
# # 加密
# sMw="I am a student,and i am 18 years old!"         #原明文
# sW=""         #密文
# nDeta=3         #偏移量
# for sP in sMw:
#     if 'a' <=sP<= 'z':
#         nP = ord(sP)
#         nC = (nP - ord('a') + nDeta) % 26 + ord('a')
#         sC = chr(nC)
#     elif 'A' <=sP<= 'Z':
#         nP = ord(sP)
#         nC = (nP - ord('A') + nDeta) % 26 + ord('A')
#         sC = chr(nC)
#     else:
#         sC=sP
#     sW+=sC
# print(f"明文：{sMw}\n加密后\n密文：{sW}")
# # 解密
# sMwm=""         #解密后所得明文
# for sp in sW:
#     if 'a' <=sp<= 'z':
#         np = ord(sp)
#         nc = (np - ord('a') - nDeta) % 26 + ord('a')
#         sc = chr(nc)
#     elif 'A' <=sp<= 'Z':
#         np = ord(sp)
#         nc = (np - ord('A') - nDeta) % 26 + ord('A')
#         sc = chr(nc)
#     else:
#         sc=sp
#     sMwm+=sc
# print(f"解密后\n明文：{sMwm}")
# # 验证真伪性
# if sMwm == sMw:
#     print("\n解密后明文与原明文一致")
# else:
#     print("\n解密后明文与原明文不一致")

# 2、文字排版工具
# string = "  他   问,你知 道cba是 什 么单词的缩写么    ?    "
# print(string)
# print("1:删除空格")
# print("2:英文标点替换为中文标点")
# print("3:字母全部大写")
# print("4:退出")
# while True:
#     option = input("请输入功能:\n")
#     if option == '1':
#         string = string.replace(' ', '')
#         print(string)
#     elif option == '2':
#         for i in string:
#             if i == ',':
#                 string = string.replace(',', '，')
#             elif i == '.':
#                 string = string.replace('.', '。')
#             elif i == '?':
#                 string = string.replace('?', '？')
#             elif i == '’':
#                 string = string.replace("'", "‘")
#             string = string
#         print(string)
#     elif option == '3':
#         string = string.upper()
#         print(string)
#     elif option == '4':
#         print("退出")
#         break

# 3、列表的基本操作
# lt=list()
# lt=[7,16,23,30,34]
# lt[1]=17
# print(f"修改lt中第2个元素后：{lt}")
# lt.insert(1,12)
# print(f"向lt中第2个位置增加一个元素后：{lt}")
# del(lt[0])
# print(f"从lt中第1个位置删除一个元素后：{lt}")
# del(lt[0:3])
# print(f"删除lt中第1-3位置元素后：{lt}")
# print(f"判断lt中是否包含数字0：{0 in lt}")
# lt.append(0)
# print(f"向lt新增数字0后：{lt}")
# print(f"返回数字0所在lt中的索引后：{lt.index(0)}")
# print(f"lt的长度：{len(lt)}")
# print(f"lt中最大元素：{max(lt)}")
# print(f"清空lt后：{lt.clear()}")

# 4、六位随机验证码生成
# import random
# s=[]
# code = ""
# for i in range(48,58):         #数字
#     s+=chr(i)
# for i in range(97,123):        #小写字母
#     s+=chr(i)
# for i in range(65,91):         #大写字母
#     s+=chr(i)
# for i in range(6):
#     code += random.choice(s)
# print("所产生的六位随机验证码为：",code,sep="")

# 5、基本数据统计
# 定义一组数组
lst1=[23,30,34,39,44,45,60,62]
# 总个数
nL=len(lst1)
print("该组数组总共",nL,"个数")
# 和
nS=0
for i in lst1:
    nS+=i
print("该组数组和为",nS)
# 中位数
lst1.sort()
nZw=0
if nL % 2 == 1:
    nZw=lst1[nL//2]
else:
    nZw=(lst1[nL//2-1]+lst1[nL//2])/2
print("该组数组中位数为",nZw)
# 平均值
nAvg=nS/nL
print("该组数组平均值为",nAvg)
# 方差
squ=0
for j in lst1:
    squ = squ + ((j-nAvg)**2)
    nFc = squ / nL
print("该组数组方差为",nFc)

