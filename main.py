# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""
from traceback import print_tb

f"""
#对append的使用
list = [] #创建空列表用[]而不是（）
List_1 = list.append("a") #当用变量接收时，返回的是None,而不是一个新数组,
# append本质是给原来的列表加一个新数字， 会直接改变原对象
print(list)
#对insert的使用
num =[1,2,3,4]
num.insert(0,"a") #insert(a,b) insert需要传入两个参数，a是数组位置,b是传入的内容
num.insert(len(num),"abc") #本质上就是使用append
print(num)
##append，insert这些原地修改数组的返回值都是None

#对pop的使用
num = [10,20,30]
num_1 = num.pop(-2) #为（）没有内容时，默认提出数组最后一个数据
print(num_1) #变量num_1可以接收从num进行pop提取出来的数据
print(num)

#（）[stand:end:step]对与切片的练习
numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
cup = numbers[0:6] #找出前六个元素
print(cup)
cup_1 = numbers[-6:] #找出后六个元素
print(cup_1)
cup_2 = numbers[2::2] #从2索引到15，步长为2
print(cup_2)
cup_3 = numbers[::-1] #彻底反转
print(cup_3)

#推导式（Comprehension）
# 是 Python 中一种简洁、高效的创建序列（列表、字典、集合等）的语法。
# 它可以用一行代码代替多行的循环语句。
#推导式的练习，

num = [x*3 for x in range(10)]
print(num)
#生成0-9每个数的平方
num_1 = [x**2 for x in range(10)]
print(num_1)
#生成0-9每个数的立方
num_2 = [x**3 for x in range(10)]
print(num_2)
#生成1-10每个数的倒数（保留小数)
num_3 = [round(1/x,1) for x in range(1,11)] #round(x,2)表示对x保留2位小数
print(num_3)

#生成0-20中偶数
num = [x for x in range(20) if x%2 == 0]
print(num)
#生成0-20中的奇数
num_1 = [x for x in range(20) if x%2 != 0]
print(num_1)
#生成0-50中能被5整除的数
num_3 = [x for x in range(50) if x%5 == 0]
print(num_3)
#生成0-50中能被3整除但不能被5整除的数
num_4 = [x for x in range(50) if x%3 == 0 and x%5 != 0]
print(num_4)

#将列表中字符串全部转换为大写
num = ["hello","world","python"]
big_num = [x.upper() for x in num] #将字符串转换为大写格式是.upper()
print(big_num)
#生成乘法口诀
num_1 = [x*j for x in range(1,10) for j in range(1,10) ]
print(num_1)
#将0-9中的偶数保留原数，奇数变为‘odd’
num_2 = [x if x%2 == 0 else 'odd' for x in range(10)]
print(num_2)
#将0-9中的数，如果大于5则输出'大'，否侧输出'小'
num_3 = ['大' if x>5 else '小'for x in range(10)]
print(num_3)
#将列表中的负数取绝对值，正数不变
num_4 = [x if x>=0 else abs(x) for x in range(-3,3)] #abs(x) 表示对x求绝对值
print(num_4)

scores = [95,72,58,88,45,91]
target = ['A' if x>=90 else  'B' if 60<=x<90 else 'C' for x in scores]
#
print(target)

#字典的练习与熟悉
student= {} #创建字典
#对字典直接赋值
student["name"] = "张三"
student['age'] = 17
student['gender'] = '男'

#更改字典内容
student["age"] = 18

#使用update用法
student.update({"city":"北京"})
#合并两个字典
student_1 ={}
student_1.update({
    "name":"李四",
    "age":20,
    "city":"南京"

                  })
#student.update(student_1)
#print(student) # 字典1.update(字典2) 字典1会覆盖字典2
                # 字典1|字典2 创建新字典，字典2无影响 
information = student|student_1
print(information)

#字典.pop（键） 删除对应键值
dates = {}
dates.update({
    "date" : "6月3号",
    "work" : "do_work"
})
dates_1 = dates.pop("date")
dates.update({
    "content":"go_home"
})
#字典.popitem() 删除最后进入的键值（key，value)
dates_2 = dates.popitem()
print(dates)
print(dates_2)

#字典.get(key，value)输入key,可以返回value,如果value不存在，则输出None
weathers = {}
weathers.update({
    "date": 6.3,
    "weather":"sun"
})
weathers.update({
    "date_1": 6.4,
    "weather_1":"rain"
})
print(weathers)
weathers.update({
    "date_2": 6.5,
    "weather_2":"cloudy"
})
del_1 = weathers.popitem()
print(del_1)
mation = weathers.get("date")
print(mation)
print(weathers.keys()) #历遍字典weathers中的所有键（key）
print(weathers.values())#历遍字典weathers中的所有值(value）
print(weathers.items()) ##历遍字典weathers中的所有键对（key:value)

#字典推导式练习

names = ["苹果","香蕉","橙子"]
prices = [5,3,4]
result = {k:v for k, v in zip(names,prices) }
print(result)

students = ["s1","s2","s3"]
scores = [85,92,78]
result_1 = {k:v for k,v in zip(students,scores)}
print(result_1)

students = ['小明', '小红', '小刚,'小丽]
scores = [85, 45,92, 58]
#定义一个函数：将分数转换为等级制
def grade(scores):
    if scores>=90:
        return("A")
    elif scores>=80:
        return("B")
    else:
        return("C")
grades = {k:grade(scores) for k,scores in zip(students,scores)}
print(grades)


#去重：set(列表)
lis=[7,2,4,4,4,6,7,7,9,3,5]
list_1 = set(lis) #去除列表中的重复字符，但可能会改变原列表的顺序
print(list_1)
# &(交集的使用)
list_1 = [1,4,2,9]
list_10 = list(set(lis) & set(list_1))
print(list_10)
# |（并集的使用）
list_20 = list(set(lis) | set(list_1))
print(list_20)
#-（差集的使用）
list_30 = list(set(lis) - set(list_1))
print(list_30)

# 函数： 五种参数类型
#位置参数
def  greet(name,age):  #按照位置顺序进行传参
    print(f"我的名字是{name},年龄是{age}")
greet("luming",18)
#默认参数
def greet_1(name,age=20):
    print(f"{name}")
greet_1("bay")
#关键字传参
def greet_2(name,age,agender):
    print(f"姓名{name},年龄{age},{agender}")
greet_2(name = 'low',age = 30,agender = 'high' )
greet_2("low",age = 30,agender = 'low') #关键字参数必须在位置参数背后

#args*参数：接收任意数量的位置参数，打包成元组
def sum_numbers(*args):
    print(f"接收到的参数{args}")
    return sum(args)
print(sum_numbers(1,2,3,4,5,6))
#**kwargs ：接收任意数量的关键字参数，打包成字典
def print_info(**kwargs):
    print(f"接收到的参数:{kwargs}")
    for k,v in kwargs.items():
        print(f"{k}:{v}")
print(print_info(name="小明", age=18, city="北京"))

def my_average(*nums):
    if not nums:
        return 0
    return sum(nums)/len(nums)
assert my_average(1,2,3,4) == 2.5
assert my_average(1,2,3,4,5,6) == 21/6
print("通过啦！！")

with open(r"C:\Users\1\Desktop\process\day1.txt","r",encoding = 'utf-8') as f:
    #content = f.read()
    content_1 = f.readlines()
    #print(content)
    print(content_1)
for line in content_1:
    print(line)

with open(r"C:/Users/1/Desktop/process/test.txt","r",encoding = "utf-8") as f:
    contents = f.read()
    print(contents)
result = contents.split()
"""


