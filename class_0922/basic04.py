# -*- conding: utf-8 -*-
# @Time      :2020/1/17 13:51
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :basic04.py
'''
rw
'''
# r 只读 r+ 可读可写 先写的话，覆盖开头  先读的话，从结尾添加 （跟着光标走）
# file = open("python11.txt","r+")
# res = file.read() #读数据  读取所有与内容
# res = file.write("888")
# print(res)

# file = open("python11.txt","r+")
# res = file.write("777") #读数据
# print(res)

#w 只写
#w+ 可读可写 不管是w 还是w+ 如果文件存在就清空
# file = open("python12.txt","w",encoding="utf-8") #无文件会创建文件
# file.write("888")

# file = open("python12.txt","a+",encoding="utf-8") #追加
# file.write("\nff")

file = open("python11.txt","r+")
# res = file.readline() #按行读取
res = file.readlines() #读取所有 返回列表
print(res)