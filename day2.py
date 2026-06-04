"""class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"书名是{self.title},作者是{self.author}"
print(book("西游记","吴承恩"))
class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius
    def __str__(self):
        f = self.celsius
        to_fahrenheit = f*9/5 + 32
        return f"{to_fahrenheit}"
print(Temperature(25))

class BankAccount:
    def __init__(self,owner,balance):
        self.balance = balance
        self.owner = owner
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if amount > self.balance:
            print("余额不足")
        else:
            self.balance -= amount

    def __str__(self):
        return f"账户:{self.owner}，余额:{self.balance}"
print(BankAccount("张三",2000))
acount = BankAccount("张三",2000)

class school:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def __str__(self):
        return f"学生:{self.name},分数：{self.score}"
class Highstudent(school):
    def __init__(self,name,score,grade):
        super().__init__(name,score)
        self.grade = grade
    def __str__(self):
        return f"高中生:{self.name},分数:{self.score},年级:{self.grade}"
    def get_rank(self):
        if self.score >=90:
            print("优秀")
        elif self.score>=60 :
            print("及格")
        else:
            print("加油")
grade_1 = Highstudent("张三",90,"高三")
print(grade_1)
print(grade_1.get_rank())
"""
