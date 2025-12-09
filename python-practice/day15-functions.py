#Write a function that prints "Hello Python".
def data():
    print("hello python")
data()

#Write a function that takes a number and prints whether it is even or odd.

def even_odd(num):
    if num%2==0:
       return "its even"
    else:
        return"its odd"
number=int(input("enter number"))
print(even_odd(number))   

#Create a function that takes two numbers and prints their sum.
def sum(a,b):
    result=a+b
    return result

a=int(input("enter value of a: "))
b=int(input("enter value of b:"))
print(sum(a,b))

#Write a function full_name(first, last) that prints the full name.
def full_name(first_name,last_name):
    return first_name +' '+ last_name

first=input("enter first name: ")
last=input("enter first name: ")
print(full_name(first,last))

#Create a function that takes a list and prints the length of the list.

def len_num(numbers):
    return len(numbers)
num=[1,2,3,4]
print(len_num(num))

#Write a function that takes 3 numbers and prints the largest.
def largest(a,b,c):

   if a>b and a>c:
    return "a is largest"
   elif b>a and b>c:
    return "b is largest"
   else:
    return "c is largest"

a, b, c = map(int, input("Enter 3 numbers: ").split())
print(largest(a,b,c))

#Write a function that takes a list of numbers and 
#returns a new list with only the even numbers.

def even_num(numbers):
    for i in numbers:
        if i%2==0:
            new_list.append(i)
            return new_list
numbers=[1,3,6,7,9]
new_list=[]
print(even_num(numbers))

#Create a function that returns "Palindrome"
#if a string is palindrome, otherwise "Not Palindrome".

def is_palindrome(palindrome):
    reverse_palindrome=palindrome[::-1]
    if palindrome==reverse_palindrome:
        return "yes its palindrome"
    else:
        return not palindrome

palindrome="mam"
print(is_palindrome(palindrome))

#Make a calculator function with parameters: a, b, operation
#Example: calc(5, 3, "multiply") → returns 15.
def calc(a,b,multiply):
    result=a*b
    return result
print(calc(2,3,"multiply"))

#Write a function that takes a string and returns how many vowels it contains.

def is_vowel(user_input):
    count=0
    for i in range(len(user_input)):
        for j in range(len(vowels)):
          #if i.isalpha():
            if user_input[i]==vowels[j]:
                count+=1
    return count
user_input=input("enter string: ")
a=user_input[0:]
vowels=["a","e","i","o","u"]
print(is_vowel(user_input))

#Write a function that returns the area of a circle (πr²).
import math
def area_of_circle(r):
    area=math.pi*r*r
    return area

r=int(input("enter r value :"))
print(area_of_circle(r))







