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
