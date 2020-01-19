# -*- conding: utf-8 -*-
# @Time      :2020/1/19 13:14
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :basic06.py
#异常处理  打印三角形 冒泡排序法
import os
try:
    os.mkdir("doc")
except:
    print("this error")
finally:
    print("this big error")

#打印正三角
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(1,i+1):
        print("* ",end="")
    print()
#九九乘法表
for i in range(1,10):
    for j in range(1,1+i):
        print("{}*{}={} ".format(j,i,i*j),end="")
    print("")
#冒泡排序法
a =[9,2,4,6]
for i in range(1,len(a)-1):
    for j in range(0,len(a) - 1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)

