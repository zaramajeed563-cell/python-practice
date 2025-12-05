#if statement
temperature=45
if temperature < 20:
      print("today is monday")
elif temperature ==20:
      print("today is not monday")
else:
      print("today is tuesday")

# exercise weight convertor
Weight=float(input("enter weight "))
Unit=(input("is this in kgs or lbs "))
if Unit=='K':
     converted=Weight*2.20462
     print("weight in lb is ",converted)
elif Unit.upper()=="L":
     converted=Weight*0.453592
     print("weight in kg is ",converted)
else:
     print("Weight Unit is not correct")

# Even/odd check
Value=int(input("Enter Value "))
if Value%2==0:
     print("Value is Even ")
else:
     print("Value is odd")

#Max two Num
First_Val=int(input("Enter First Value "))
Second_Val=int(input("Enter Second Value "))
if First_Val>Second_Val:
     print("First value is greater")
else:
     print("Second is larger")

#password checker
Password=input("Enter password ")
if Password=="python123":
     print("Access granted")
else:
     print("Wrong password")

#grades printing
math=int(input("enter maths number "))
english=int(input("enter english number "))
urdu=int(input("enter urdu number "))
total_marks=100
math_per=(math/total_marks)*100
english_per=(english/total_marks)*100
urdu_per=(urdu/total_marks)*100
if math_per>90:
     print("Math Grade is A")
if english_per>90:
     print("english Grade is A")
if urdu_per>90:
     print("urdu Grade is A")
else:
     print("grade is not mentioned")