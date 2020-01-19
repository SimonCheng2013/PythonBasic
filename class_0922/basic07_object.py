# -*- conding: utf-8 -*-
# @Time      :2020/1/19 14:02
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :basic07_object.py
class Teacher:
    name = "jack"
    age =19
    def coding(self):
        print(self.name+"写代码")
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
    # b = BoyFriend()
    # b.cooking()
    Teacher().coding()