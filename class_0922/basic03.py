# -*- conding: utf-8 -*-
# @Time      :2020/1/16 17:45
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :basic03.py
#函数
def add(a,b):
    return (a+b)
res = add(1,3)+22
#静态参数
def make_sandwich(*args):
    print(*args)
make_sandwich("生菜","鸡蛋","培根")

#全局变量 局部变量

# a = 1 #全局变量
# def add(b):
#     a= 5 #局部变量 方法块内起作用
#     print(a+b)
# add(10)

a = 1
def add(b):
    global a #全局变量
    a = b+5
    print(a)
add(10)

a = [1,2,3,4]
print(a.pop())

if __name__ == '__main__': #主方法 程序入口
    add()