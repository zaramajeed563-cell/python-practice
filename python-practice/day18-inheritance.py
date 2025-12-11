#Create a class Vehicle method: start() Create child class Car Car has method: drive()
class vehicle():
    def start(self):
        print("you car is start")
class car(vehicle):
    def drive(self):
        print("car is driving")

v=car()
v.start()
v.drive()

""" Parent class: Person
attributes: name, age
method: show_details()
Child class: Employee
attribute: salary
method: show_salary() """
class person():
    def __init__(self,name ,age):
        self.name=name
        self.age=age
    def show_details(self):
        print(f"employee name is {self.name} and age is {self.age}")
class employee(person):
    def __init__(self,name,age,salary):
        self.salary=salary
        super().__init__(name,age)
    def show_salary(self):
        print(self.salary,"is salary")
        
p=employee("zara",25,2500)
p.show_details()
p.show_salary()

""" Parent class: Animal
method: eat()
Child class: Cat
method: meow()
Make an object of Cat and call both methods. """
class animal():
    def eat(self):
        print("animal is eating")


class cat(animal):
    def meow(self):
        print("cat says meow")
        

a=cat()
a.eat()
a.meow()

""" Parent class: BankAccount
balance attribute
deposit()
withdraw()
Child class: SavingAccount
method: apply_interest() → add 5% interest """
class BankAccount():
    def __init__(self,balance):
        self.balance=balance
    def deposit(self):
        amount=int(input("enter amount for deposit:"))
        self.balance+=amount
        print("deposit successfully")
    def withdrawal(self):
        amount=int(input("enter amount for withdrawal:"))
        if amount<self.balance:
         self.balance-=amount
         print("withdraw succesfull")
        else:
           print("balance insufficient")
class SavingAccount(BankAccount):
   
   def apply_interest(self):
      interest=0.05*self.balance
      self.balance+=interest
      print("Interest added:", interest)
      print("New balance:", self.balance)

a=SavingAccount(500)
a.deposit()
a.withdrawal()
a.apply_interest()
      
