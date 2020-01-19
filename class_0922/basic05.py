# -*- conding: utf-8 -*-
# @Time      :2020/1/17 17:15
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :basic05.py
import os

# os.mkdir("D:\PycharmProjects\PythonBasic\class_0922\\aa") #创建文件夹

# path = os.getcwd() #获取当前文件根路径
# path_2 = os.path.realpath(__file__) #获取当前文件路径
# print(path_2)

#拼接路径
new_path = os.path.join(os.getcwd(),"python333","hhh")
print(new_path)

print(os.path.isfile(os.getcwd()))
print(os.path.isdir(os.getcwd()))

print(os.path.exists(os.getcwd()))
print(os.listdir(os.getcwd()))

print(os.listdir(os.getcwd())) #罗列所有文件和目录 以列表格式

