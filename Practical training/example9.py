# 七段数码管绘制当前系统时间
#
# import time
#
# # 1、函数封装：获取本地时间，格式化时间
# def getLocalTime():
#     nTime = time.time()         # 获取本地时间戳
#     nLtime = time.localtime(nTime)
#     sLtime = time.strftime("%Y-%m-%d %H:%M:%S",nLtime)
#     return sLtime
#
# import turtle
#
# # 2、绘制直线并转向
# def drawLine(isDraw):
#     if isDraw:
#         turtle.pendown()
#     else:
#         turtle.penup()
#     turtle.fd(50)
#     turtle.lt(90)
#
# # 3、绘制相对应的数字
# def drawDigist(n):
#     drawLine(False) if n in [0,1,7] else drawLine(True)
#     drawLine(False) if n in [5,6] else drawLine(True)
#     drawLine(False) if n in [1,4] else drawLine(True)
#     drawLine(False) if n in [1,2,3,7] else drawLine(True)
#     turtle.rt(90)
#     drawLine(False) if n in [1,3,4,5,7,9] else drawLine(True)
#     drawLine(False) if n in [1,4,7] else drawLine(True)
#     drawLine(False) if n in [2] else drawLine(True)
#
# # 4、封装函数：绘制间隙
# def drawGap(n):
#     turtle.seth(0)         # 方向控制
#     turtle.penup()
#     turtle.fd(n)
#     turtle.pendown()
#
# # 5、封装函数：绘制小圆点
# def drawRadius(radius):
#
#
# turtle.setup(1500,800)         # 设置窗体大小及位置
# turtle.penup()
# turtle.goto(-750,0)         # 将画笔移动到画布指定位置
# turtle.pendown()
# turtle.shape(name="turtle")
# turtle.pencolor("red")         # 画笔颜色
# turtle.pensize(5)         # 画笔大小
# turtle.speed(0)         # 画笔速度
#
# sLtime = getLocalTime()
# print(sLtime)
# for i in sLtime:
#     if i in ["-"," ",",",":"]:
#         continue
#     drawDigist(int(i))
#     drawGap(50)
# turtle.done()

# import turtle
# turtle.dot(50,"blue")
# turtle.done()

# 111111111

# import turtle, datetime
#
#
# def drawGap():  # 绘制数码管间隔
#     turtle.penup()
#     turtle.fd(5)
#
#
# def drawLine(draw):  # 绘制单段数码管
#     drawGap()
#     turtle.pendown() if draw else turtle.penup()
#     turtle.fd(40)
#     drawGap()
#     turtle.right(90)
#
#
# def drawDigit(d):  # 根据数字绘制七段数码管
#     drawLine(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
#     drawLine(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
#     drawLine(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
#     drawLine(True) if d in [0, 2, 6, 8] else drawLine(False)
#     turtle.left(90)
#     drawLine(True) if d in [0, 4, 5, 6, 8, 9] else drawLine(False)
#     drawLine(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
#     drawLine(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
#     turtle.left(180)
#     turtle.penup()
#     turtle.fd(20)
#
#
# def drawDate(date):
#     turtle.pencolor("red")
#     for i in date:
#         if i == '-':
#             turtle.write('年', font=("Arial", 18, "normal"))
#             turtle.pencolor("green")
#             turtle.fd(40)
#         elif i == '=':
#             turtle.write('月', font=("Arial", 18, "normal"))
#             turtle.pencolor("blue")
#             turtle.fd(40)
#         elif i == '+':
#             turtle.write('日', font=("Arial", 18, "normal"))
#         else:
#             drawDigit(eval(i))
#
#
# def main():
#     turtle.setup(800, 350)
#     turtle.penup()
#     turtle.fd(-350)
#     turtle.pensize(5)
#     drawDate(datetime.datetime.now().strftime('%Y-%m=%d+'))
#     turtle.hideturtle()
#     turtle.speed(0)
#
#
# main()


# 222222222

# coding:utf-8
# 绘制七段数码管，显示当前时间
import time
import turtle as tt


# 绘制间隔
def drawGap():
    tt.penup()
    tt.fd(5)


# 绘制单段数码管
def drawLine(draw):
    drawGap()

    if (draw):
        tt.pendown()
    else:
        tt.penup()

    tt.fd(50)
    drawGap()
    tt.right(90)


# 绘制当前时间
def drawDate(date):
    tt.pencolor("red")
    for i in date:
        if i == '+':
            tt.write("年", font=("黑体", 25, "normal"))
            tt.pencolor("green")
            tt.fd(50)
        elif i == '-':
            tt.write("月", font=("黑体", 25, "normal"))
            tt.pencolor("blue")
            tt.fd(50)
        elif i == '*':
            tt.write("日", font=("黑体", 25, "normal"))
            tt.pencolor("purple")
            tt.fd(50)
        elif i == '=':
            tt.write("时", font=("黑体", 25, "normal"))
            tt.pencolor("yellow")
            tt.fd(50)
        elif i == '#':
            tt.write("分", font=("黑体", 25, "normal"))
            tt.pencolor("black")
            tt.fd(50)
        elif i == '$':
            tt.write("秒", font=("黑体", 25, "normal"))

        else:
            drawDigit(eval(i))


# 绘制数码管
def drawDigit(cur_time):
    if cur_time in [2, 3, 4, 5, 6, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    if cur_time in [0, 1, 3, 4, 5, 6, 7, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    if cur_time in [0, 2, 3, 5, 6, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    if cur_time in [0, 2, 6, 8]:
        drawLine(True)
    else:
        drawLine(False)

    tt.left(90)

    if cur_time in [0, 4, 5, 6, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    if cur_time in [0, 2, 3, 5, 6, 7, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    if cur_time in [0, 1, 2, 3, 4, 7, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    tt.left(180)
    tt.penup()
    tt.fd(20)


# 主函数
def main():
    tt.setup(1600, 300)
    tt.penup()
    tt.fd(-730)
    tt.pensize(5)
    tt.speed(0)
    drawDate(time.strftime('%Y+%m-%d*%H=%M#%S$', time.localtime()))
    tt.hideturtle()
    tt.done()


if __name__ == "__main__":
    main()