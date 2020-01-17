# -*- conding: utf-8 -*-
# @Time      :2020/1/15 10:32
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :basic.py
#数据类型 整型/浮点型/列表/元组/字典

#1.数字类型：整型 浮点型

#整型： 关键字 int
a = 10  #int 类型
#浮点类型： 关键字 float
b = 10.0  # float类型

#2.布尔类型：True False 关键字bool
t = True
f = False
#3.字符串类型 str
a = 'hello world'
b= "你好啊"
c = '''666'''
d = """888"""
e = '0123456789q'
print(type(a)) #type 判断字符串类型
print(len(a)) #len 判断字符串长度 空格也算1个长度
print(b[2]) #字符串里的元素：所有字母数字符号都称为一个元素 索引从0开始
print(a[-1]) #从倒数第一个开始定位
#切片 字符串名[索引头：索引尾：步长]
print(a[1:3])  #前包后不包
print(e[1:10])
print(e[1:10:2])
print(e[:3]) #取索引3之前的元素
print(e[3:]) #取索引3之后的元素 包括3
#考题：倒序输出e的字符串
print(e[::-1])
#字符串分割： 字符串.split()
s = ' hello'
print(s.split(' '))#切掉空格元素
print(s.split("e")) #切掉e元素
print(s.split("l",1)) #切掉1元素 一次
# 字符串替换
s = ' hello'
new = s.replace('l','@',1) #替换l为@一次
print(new)
# 字符串去除指定字符
s = '666hello!666'
print(len(s))
new = s.strip('6') #默认去掉空格 只能去掉收尾的元素
print(new)
print(len(new))

#字符串拼接
s_1 = 'python11,'
s_2 = '中秋快乐!'
s_3 = 666
print(s_1+s_2,s_3) #不同字符类型不能拼接

#字符串格式化输出
age = 18
name = '小恒星'
print('python11的{1}今年{1}岁'.format(name,age))
#格式化输出：%s字符串 %d数字 %f 浮点数
print('python11的%s今年%d岁'%(name,age)) #数字型可格式化字符型

#4.列表 list 符号[]
a = [1,0.02,'hello',[1,2,3],True]
a.append("秦天") #列表添加数据 添加在末尾
a.insert(2,"moncia") #插入到指定索引
a.pop() #默认删除最后一个元素
print(a)
a.remove("hello")#指定删除某个索引的值
print(a)
a.pop(3) #指定删除索引位置的元素
print(a)
res = a.pop(2) #指定返回被删除的元素
print(res)
#修改
a = [1,0.02,'hello',[1,2,3],True]
a [2] = "world"
print(a)

#5.元组 tuple 符号()
a = (1,0.02,'hello',[1,2,3],True)
print(a[2:]) #切片和字符串有同样的操作 不支持修改
c =("r",) #如果元组里只有一个元素需要加逗号
print(type(c))

#6.字典 dict 符号{} 大括号 key:value
a = {'class':'python11',
     'student':119,
     'teacher': 'girl',
     't_age': 20,
     'score': [99,88.8,100.5]}
print(len(a))
print(a["teacher"])
#删除
a.pop("student") #删除键 键值对都将删除
print(a)
#新增
a["name"] = "jack"
#修改
a['teacher'] = "boy"
print(a)




