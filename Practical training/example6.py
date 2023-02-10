# 1、字典的基本操作
# # 创建空集合
# lt=list()
# # 创建空字典
# d=dict()
# # 向d新增2个键值对元素，比如“姓名”、“学号”
# d['姓名']='张三'
# d['学号']='521'
# print("添加后",d)
# # 修改学号的值
# d['学号']='1314521'
# print("修改后",d)
# # 新增“年龄”键值对
# d['年龄']='18'
# print("新增后",d)
# # 判断字符"性别"是否是d的键
# print("判断后",'性别' in d)
# # 计算d的长度
# print("长度为",len(d))
# # 清空d
# print("清空后",d.clear())

# 2、歌手排名
# print("输入quit表示选手成绩录入完毕！")
# # 创建字典
# singers={}
# while True:
#     name=input("请输入选手名称：")
#     if name == 'quit':
#         break
#     point=eval(input("请输入选手票数："))
#     singers[name]=point
# # 输入后各选手及对应票数
# # print("输入后各选手及对应票数：\n",singers)
# # 排序
# singers_list = sorted(singers.items(),key=lambda x:x[1],reverse=True)
# # print("排序：\n",singers_list)
# # 排名
# print("第1名：",singers_list[0][0],"，成绩为","{:.1f}".format(singers_list[0][1]),"分",sep="")
# print("第2名：",singers_list[1][0],"，成绩为","{:.1f}".format(singers_list[1][1]),"分",sep="")
# print("第3名：",singers_list[2][0],"，成绩为","{:.1f}".format(singers_list[2][1]),"分",sep="")

# 3、三国演义人物分析


# 4、十大歌手比赛

# 字典实现法

# 评委
listkeys = ['1评','2评','3评','4评','5评','6评','7评','8评','9评','10评']
# 分数
listvalues = []
for i in range(1,11):
    score = eval(input(f"请第{i}位评委输入评分:\n",))
    listvalues.append(score)
# 创建字典
dict = dict(zip(listkeys,listvalues))
print("各评委对应分数：\n",dict)
# 操作前字典中的值进行排序且以字典形式输出
print("操作前字典中的值进行排序输出：\n",sorted(dict.items(),key=lambda x:x[1]))
# # 返回字典中的最小值对应的键
# print("字典中的最小值对应的键：",min(dict,key=dict.get))
# 最低分
print("去掉最低分：","{:.1f}".format(min(dict.values())))
# # 返回字典中的最大值对应的键
# print("字典中的最小值对应的键：",max(dict,key=dict.get))
# 最高分
print("去掉最高分：","{:.1f}".format(max(dict.values())))
# 去掉最低分
del(dict[min(dict,key=dict.get)])
# 去掉最高分
del(dict[max(dict,key=dict.get)])
print("操作后字典：",dict)
# 操作后字典中的值进行排序且以字典形式输出
print("操作后字典中的值进行排序输出：\n",sorted(dict.items(),key=lambda x:x[1]))
# 去掉后最终得分（即平均分）
print("选手最终得分为：",round(sum(dict.values())/len(dict.values()),1))         #保留1位小数

