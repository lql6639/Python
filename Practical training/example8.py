# 1、模拟饮品自动售货机
#
# # 所有商品信息
# def all_goods():
#     goods = {"可口可乐": 2.5, "百事可乐": 2.5, "冰红茶": 3, "脉动": 3.5, "果缤纷": 3,"绿茶": 3, "茉莉花茶": 3, "尖叫": 2.5}
#     return goods
#
# # 函数功能：显示/打印所有商品信息
# # 输入参数：无
# # 输出参数：无
#
# # 展示商品信息
# def showALLgoods():
#     lGoods = all_goods()
#     print("所有商品信息".center(17))
#     print("{:<12}{:>6}".format("饮品","价格"))
#     print(20 * "=")
#     # 请在此处完成所有商品信息打印
#     for name,price in lGoods.items():
#         print(name,"{:>12}".format(price),"元",sep="")
#     print("输入'q'结束商品购买！！")
#     print(20 * "=")
#     print("请开始选购您的商品！！！")
#     return
#
# # 函数功能：结账
# # 输入参数：以字典数据类型进行储存的选购商品
# # 输出参数：支付总额
#
# # 计算总额
# def total(chooseGoods={}):
#     tallGoods = all_goods()
#     tMoney = 0
#     for name,num in chooseGoods.items():
#         spend = tallGoods[name] * num
#         # 总金额
#         tMoney += spend
#     return tMoney
#
# def main():
#     chooseGoods = {}
#     showALLgoods()
#     # 完成购物的过程
#     while True:
#         goods_name = input("请输入购物的商品：")
#         if goods_name == 'q':
#             break
#         if goods_name in [g_name for g_name in  all_goods().keys()]:
#             goods_num = input("请输入购物数量：")
#             if goods_num.isdigit():
#                 chooseGoods[goods_name] = float(goods_num)
#             else:
#                 print("商品数量不合法！")
#         else:
#             print("请输入正确的商品名称！")
#     print("需要支付金额：",total(chooseGoods),"元")
#
# if __name__ == '__main__':
#     main()

# 2、学生管理系统

stuInfo = []         #全局变量

#用于打印学生管理系统的功能菜单
def print_menu():
    print("="*30)
    print("学生管理系统 V10.0")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查询所有学生信息")
    print("0.退出系统")
    print("="*30)
    return

#用于添加学生的信息
def add_stu_info():
    newName=input("请输入新学生的姓名：")
    newSex=input("请输入新学生的性别：")
    newPhone=input("请输入新学生的手机号码：")
    newInfo={}
    newInfo['name'] = newName
    newInfo['sex'] = newSex
    newInfo['phone'] = newPhone
    stuInfo.append(newInfo)
    return

#用于删除学生的信息
def del_stu_info():
    delNum=int(input("请输入要删除的学生的序号："))-1
    del stuInfo[delNum]
    print("删除成功！")
    return

#用于修改学生的信息
def modify_stu_info():
    if len(stuInfo) != 0:
        stuID = int(input("请输入要修改学生的序号："))
        newName = input("请输入要修改学生的姓名：")
        newSex = input("请输入要修改学生的性别：（男/女）：")
        newPhone = input("请输入要修改学生的手机号码：")
        stuInfo[stuID-1]['name'] = newName
        stuInfo[stuID-1]['sex'] = newSex
        stuInfo[stuID-1]['phone'] = newPhone
    else:
        print("当前学生信息表为空！")
    return

#用于显示所有学生的信息
def show_stu_info():
    print("学生信息如下：")
    print("="*30)
    print("序号    姓名     性别     手机号码")
    i=1
    for itemIfo in stuInfo:
        print("{:<6} {:<6} {:<6} {:<13}".format(i,itemIfo['name'],itemIfo['sex'],itemIfo['phone']))
        i+=1
    return

#定义主程序，用于控制一次使用学生管理系统的完整流程
def main():
    while True:
        print_menu()         #打印功能菜单
        keyNum = input("请输入功能对应的数字：\n")
        if keyNum == '1':
            add_stu_info()
        elif keyNum == '2':
            del_stu_info()
        elif keyNum == '3':
            modify_stu_info()
        elif keyNum == '4':
            show_stu_info()
        elif keyNum == '0':
            quitTips=input("亲，真的要退出么？（yes or No）：".lower())
            if quitTips == 'yes':
                print("谢谢使用！")
                break
            elif quitTips == 'no':
                continue
            else:
                print('输入有误！')
        else:
            print("输入有误，请重新输入！")
    return

if __name__=='__main__':
    main()

