""" Create a class Dog with:
attributes: name, breed
method: bark() → print “Woof! Woof!” """

class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):
        print(self.name,self.breed)
        print("whoof whoof!")
a=Dog("puppy","German Shepherd")
a.bark()

""" Create a class Calculator with:
attributes: a, b
methods: add(), sub(), mul(), div() """

class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        result=self.a+self.b
        print(f"{self.a}+{self.b}=",result)
    def subtract(self):
        result=self.a-self.b
        print(f"{self.a}-{self.b}=",result)
    def multiply(self):
        result=self.a*self.b
        print(f"{self.a}*{self.b}=",result)
a=calculator(2,4)
a.sum()
a.multiply()
a.subtract()


""" Create a BankAccount class with:
balance attribute (start 0)
deposit(amount)
withdraw(amount)
show_balance() """
class bank:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self):
        amount=int(input("enter amount for deposit: "))
        self.balance=self.balance+amount
        print("amount deposited")
    def withdraw(self):
        amount=int(input("enter amount for withdrawal: ")) 
        if amount<self.balance:
            self.balance-=amount
            print("withdraw succesfull")
        else:
            print("balance insufficient")  
        
    def Show_balnce(self):
          print("total balance is:",self.balance)
a=bank(0)
a.deposit()
a.withdraw()
a.Show_balnce()

""" Q4: Make a class Person with:

name, age

method: can_vote() → print if age >= 18 """
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def can_vote(self):
        if self.age>=18:
            print("you can vote")
        else:
            print("you cant vote")
a=person('zara',12)
a.can_vote()

""" Create a Student class:
name, marks
method: grade()
marks >= 90 → A
marks >= 80 → B
marks >= 70 → C
else → Fail """

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def grade(self):
        if self.marks>=90:
            print("A grade")
        elif self.marks>=80:
            print("grade is B")
        elif self.marks>=70:
            print("grade is C")
        else:
            print("fail")
s=student('zara',100)
s.grade()

