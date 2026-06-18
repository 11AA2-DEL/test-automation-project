#设置表格
"""
class student:
    name = None
    age = None
    gender = None
    #类中的函数称为方法
    def say(self): #self属于格式要求，翻译不输出
        print(f"{self.name}")# 加入self.xxx才可以调用类中的name变量
    def say_2(self,mag):
        print(f"{self.name},{mag} ")
#创建表格内容
stu_1 = student()
stu_2 = student()
#填写表格内容
stu_1.name = ("张三")
stu_2.name = ("李四")
stu_1.age = 18
stu_2.age = 22
stu_1.gender = "男"
stu_2.gender = "男"
stu_2.say_2("可以啊")
"""
from os import name

"""
class Clock:
    id = None
    price = None
    def ring(self):
        import winsound
        winsound.Beep(2000,3000)
clock1 = Clock()
clock1.id = "闹钟"
clock1.price = 100
print(f"产品名称是{clock1.id},产品价格是{clock1.price}")
clock1.ring()
"""
"""
class student:
    name = None
    age = None
    gender = None
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        print(f"{name,age,gender}")
stu = student(1,12,1)
"""
"""
class student:

    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
        print(f"学生姓名{name},年龄{age},地址{address}")
students = []
for i in range(10):
    print(f"请输入第{i+1}个同学的个人信息")
    name = input("请输入同学姓名 : ")
    age = input("请输入学生年龄: ")
    address = input("请输入学生地址: " )
    stu = student(name,age,address)
    students.append(stu)
    print(f"学生{i+1}信息录入成功,姓名：{name},年龄：{age},地址{address}")
"""
"""
class Phone:
    __current_voltage = None
    def __keep__single_core(self): #__私有化
        print("cpu运行")
    def call_bu_5g(self,__current_voltage):
        self.__current_voltage = __current_voltage
        if self.__current_voltage == 5:
            print("5g通话开启")
        else:
            print("电压不支持正常运行")
phone = Phone()
phone.call_bu_5g(4)
"""
class  Phone:
    __current_voltage = None
