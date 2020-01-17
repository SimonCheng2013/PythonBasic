# -*- conding: utf-8 -*-
# @Time      :2020/1/15 16:10
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :basic02.py

#运算符

#算数运算符 + - * / %
a = 5
print(a%2) #取余运算

#赋值运算符 = += -=
a = 5 #赋值运算
a += 1 #等于 a = a+5
print(a)

#比较运算符
a = 1
b = 1
print(a<b)
print(a==b)
print("get"=="GET".lower())

#逻辑运算符 and or not
a = 10
b = 5
print(a>11 or b > 4) #or 两个都为假 为假 一个为真就为真
print(a>11 and b > 4) #and 两个都为真才为真 一个为假就为假
#成员运算符
s = 'hello'
l = [1,2,3]
d = {"age":13,"name":"tom"}
print("age" in d)

#判断语句
# age = int(input("tell me your age:"))
# if age<18:
#     print("you is a boy")
# elif 100>age>70:
#     print("you is old man")
# else:
#     print("you is 23333")
s = 'hello'
if "o" in s:
    print("o in word")
if s: #s 为空则不执行 不为空则执行
    print("i can")
if True: #为True 则执行 为False 则不执行
    print("this is True")

#一家商场促销，消费50-10给10%折扣 大于100给20%折扣
# total= int(input("购买价格："))
# if 50 <= total <= 100:
#     print("购买价：{} 享受折扣 10%".format(total))
# elif total>100:
#     print("购买价：{} 享受折扣 20%".format(total))
# else:
#     print('不享受折扣')

#生成随机数，从1-9中取，输入一个数字，大了就打印big 小了打印 less 等于打印equal
import random
# number = random.randint(1,9)
# odd = int(input("请输入："))
# if odd>number:
#     print("输入的是%s"%number)
#     print("big")
# elif odd<number:
#     print("输入的是%s" % number)
#     print("less")
# else:
#     print("输入的是%s" % number)
#     print("equal")

#for循环
s = "hello"
d = {"age":18,4:"num"}
for item in d:
    print(item)
for i in d.keys():
    print(i)
for i in d.values():
    print(i)

# L = [5,6,7,8,9]
# num = 0
# for i in L:
#     num +=i
# print(num)

# sum =0
# for item in range(10):
#     age = int(input("请问几岁："))
#     # name = input("请问名字：")
#
#     if age>=10 and age<=12:
#         print("你符合条件")
#         sum += 1
#     else:
#         print("你不符合条件")
# print(sum)

# for i in range(1,5,2):
#     print(i)

print(list(range(1,5,2)))

# sum = 0
# for i in range(1,101):
#     sum+=i
# print(sum)

# L = [["jack","tony","tom"],["lua","java","python"]]
# for item in L:
#     for i in item:
#         print(i)

name=["jack","tony","tom"]
# username = input('请输入名字：')
# if username in name:
#     print('存在')
# else:
#     print('不存在')

# for i in name:
#     username = input('请输入名字：')
#     if username == i:
#         print("i为：%s"%i)
#         print('存在')
#     else:
#         print("i为：%s" % i)
#         print('不存在')
# sum=0
# a= 1
# while a<=100:
#     sum=sum+a
#     a+=1
# print(sum)
