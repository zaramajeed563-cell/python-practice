#Ask user for a number and print its square.
#If the input is not a number, print: “Invalid input”.
try:
 user_input=int(input("enter number: "))
 square=user_input*user_input
 print("square is:",square)
except ValueError:
 print("enter valid input")
 
#Ask user to enter age.
#If they enter negative or text, print “Enter a valid age”.
try:
 age=int(input("enter age: "))
 print("age is:",age)
except ValueError:
 print("enter valid age")

#Try to convert "hello" to int using try/except.
try:
    user_input=int(input("enter number: "))
    print(user_input)
except ValueError:
    print("enter valid input")

#Ask user for a number and divide 100 by it.
#Handle both:
#ValueError
#ZeroDivisionError
try:
 user_input=int(input("enter number: "))
 division=100%user_input
 print(division)
except ValueError:
 print("enter valid input")
except ZeroDivisionError:
 print("zero cant be divisible")
 
#Make a simple calculator:
#Take two numbers
#Take an operator (+, -, *, /)
#Handle errors (wrong operator, wrong number, divide by zero)
a,b=map(int,input("enter number :").split())
operator=input("enter operator *,+,-,% : ")
try:
 if operator=='+':
  result=a+b
  print(result)
 elif operator=='-':
  result=a-b
  print(result)
 elif operator=='*':
  result=a*b
  print(result)
 elif operator=='%':
  result=a%b
  print(result)
 else:
  print("invalid operator")

except ZeroDivisionError:
 print("zero cant be divisible")

except ValueError:
 print("invalid input")

#Write a program to open a file name given by the user.
#If the file doesn’t exist, show a friendly error message.
try:
 with open("ZARA MAJEED CV.","r") as file:
  content=file.read()
  print(content)
except FileNotFoundError:
 print("file not found")

#Ask user for a name and print marks.
#If name doesn't exist → show error message using try/except.
students = {"aimen": 90, "zara": 85}
user_input=input("enter name :")
try:
    for i in students:
        if i==user_input:
            print(i,students[i])
except ValueError:
    print("name doesnot exist")

#Write code to read a list index from user.
#Handle:
#alueError (if user enters text)
#IndexError (if index is out of range)
numbers=[1,3,5,7]
user_input=int(input("enter index:"))
try:
    for i in range(len(numbers)):
        if user_input==i:
         print(numbers[i])        
except ValueError:
    print("input is not valid")
except IndexError:
    print("index out of range")


 



