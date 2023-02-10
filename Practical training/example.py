# 1、兔子数列

# def fibonacci(month):
#     if month == 0 or month == 1:
#         return 1
#     else:
#         return fibonacci(month-1) + fibonacci(month-2)
# # 测试经过12个月份后的兔子对数
# result = fibonacci(12)
# print(result)

# 2、归并排序

# def merge_sort(li):
#     n = len(li)
#     if n == 1:
#         return li
#     # 把数据分成左右两部分
#     mid = n // 2
#     left = li[:mid]
#     right = li[mid:]
#
#     # 递归拆分
#     left_res = merge_sort(left)
#     right_res = merge_sort(right)
#     # 把下层返回上来的数据，组成有序序列
#     result = merge(left_res, right_res)
#     # 合并
#     return result
#
#
# def merge(left, right):
#     result = []
#     left_index = 0
#     right_index = 0
#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] <= right[right_index]:
#             result.append(left[left_index])
#             left_index += 1
#         else:
#             result.append(right[right_index])
#             right_index += 1
#     # while循环结束后，把剩下的数据添加进来
#     result += right[right_index:]
#     result += left[left_index:]
#     return result
#
#
# if __name__ == '__main__':
#     list_demo = [6, 5, 7, 4, 3, 1]
#     print(merge_sort(list_demo))

# 3、角谷猜想

def guess(number):
    i = 0  # 统计变换的次数
    original_number = number  # 记录最初的number
    while number != 1:
        if number % 2 == 0:  # number为偶数
            number = number / 2
        else:  # number为奇数
            number = number * 3 + 1
        i += 1
    print(f"{original_number}经过{i}次变换后回到1")


num = int(input("请输入一个大于1的正整数:"))
guess(num)





