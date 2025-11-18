#max number in list
numbers=[1,2,3,4,5]
max=numbers[0]
for number in numbers:
    if number>max:
        max=number
print(max)

#Create a list of 5 numbers and print each one
numbers=[4,5,6,7,8]
print(numbers)

#Print only the first and last element
fruits = ["apple", "banana", "mango", "kiwi", "orange"]
print(fruits[0])
print(fruits[-1])

#Change the second element into something else
colors = ["red", "blue", "green"]
colors[1]="purple"
print(colors)

#Add a new item to the list
pets = ["cat", "dog"]
pets.append("goat")
print(pets)

#Remove an item from the list
cities = ["Lahore", "Karachi", "Islamabad"]
cities.pop(0)
print(cities)

#Print all even numbers from the list
nums = [10, 21, 4, 45, 66, 93]
for number in nums:
    if number%2==0:
        print(number)

#Find the largest number
marks = [45, 12, 89, 33, 50]
max=marks[0]
for mark in marks:
    if mark>max:
        max=mark
print(max)

#Reverse the list WITHOUT using reverse()
marks=[1,2,3,4]
print("before reverse",marks)
print("after")
for mark in range(len(marks)-1,0,-1):
    print(mark)

#Count how many times “2” appears
nums = [2, 3, 2, 5, 2, 8, 2]
count=0
for num in nums:
    if num==2:
        count+=1
print(f"2 appears {count} times")

#Copy a list into another new list (no shortcut)
old_list=[1,2,3,4]
new_list=[]
for value in old_list:
    new_list.append(value)
    print(f"this is new list{new_list}")

#remove duplicate elements
nums=[1,2,2,3,4,4,5]
new_list=[]
for i in nums:
    if i not in new_list:
        new_list.append(i)
print(new_list)

#Make a new list with only numbers > 10
""" nums = [4, 12, 5, 19, 7, 25, 3]
new_list=[]
for i in nums:
    if i>=10:
        new_list.append(i)
print(new_list) """

#Create a list from 1 to 100 without typing numbers
nums=[]
for i in range(1,101,1):
    nums.append(i)
print(nums)