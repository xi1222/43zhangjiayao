level = 99

if level >= 60:
    # 如果这个if的判断是True
    print("一级")
elif level >= 70:
    print("二级")

# 写一个程序，任意输入一个数，判断这个数是否是奇数还是偶数。
# number = int(input("请输入一个数:"))
# if number % 2 == 0:
#     print(f"你输入的是{number},它是一个偶数")
# else:
#     print(f"你输入的是{number},它是一个奇数")

# 输入两个数，再输入一个运算符，包括 +-*/，输入两个数字和这个运算符的运算的结果。
# 4
# 5
# *
# 20
# number1 = int(input("请输入第一个数:"))
# number2 = int(input("请输入第二个数:"))
# print(number1 + number2)
# print(number1 - number2)
# print(number1 * number2)
# print(number1 / number2)

#写一个程序，输入年和月份，输出，这个年的月份还有多少天。
# year = int(input("请输入一个年:"))
# month = int(input("请输入一个月份:"))
# if month in [1, 3, 5, 7, 8, 10, 12]:
#     print("%d月有31天" % month)
# elif month in [4, 6, 9, 11]:
#     print("%d月有30天" % month)
# elif month == 2:
#     if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#        print("%d月有29天" % (year, month))
# else:
#     print("%d月有28天" % (year, month))

#输入语文数学两门课程的成绩，两门都及格，两门都不及格，其中一门不及格。60分及格
c = float(input("请输入语文的成绩:"))
m = float(input("请输入数学的成绩:"))
if c>= 60:
    print("及格")
if c< 60:
    print("不及格")
if m>= 60:
    print("及格")
if m< 60:
    print("不及格")

#计算

