# -*- conding: utf-8 -*-
# @Time      :2020/1/19 14:35
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :basic08_extend.py
#继承
class RobotOne:
    def __init__(self,year,name):
        self.year = year
        self.name = name
    def walking_on_ground(self):
        print(self.name+"walking_on_ground")
    def robot_info(self):
        print("{0} made in china of {1}".format(self.year,self.name))
class RobotTwo(RobotOne): #第二代机器人继承第一代机器人的类
    def __init__(self,name):
        self.name = name
    def walking_on_ground(self):
        print(self.name+"walking_on_ground")
    def walking_aviod_block(self):
        self.robot_info() #子类实例化调用父类方法
        print(self.name+"walking_aviod_block")

class RobotThree(RobotTwo,RobotOne):  # 多继承
    def jump(self):
        print(self.name+"jump")
#父类有 继承后 可以拿过来用
r3 = RobotThree("大王")
r3.jump()
r3.walking_on_ground()
#具有两个父类的属性方法，如果两个父类有同名的方法 就近原则



# r2 = RobotTwo("1990","jack")
# r2.robot_info()
# r2.walking_on_ground()
# r2.walking_aviod_block()