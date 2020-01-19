# -*- conding: utf-8 -*-
# @Time      :2020/1/19 14:02
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :basic07_object.py
class LemonTeacher:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        pass

    name = "jack"
    age =19
    def coding(self,language):
        print(self.name+"写{}代码".format(language))
    def earn(self):
        print("3w")
    def cooking(self):
        print("cooking")
    @classmethod #不用实例化直接调用
    def swimming(self):
        print("swimming")

    @staticmethod #不用实例化直接调用
    def song(self):
        print("song")
if __name__ == '__main__':
    t1 = LemonTeacher("jack","18")
    t2 = LemonTeacher("tom","20")
    t3 = LemonTeacher("tony","18")

    t1.swimming()
    t2.cooking()
    t3.coding("python")