""" 1. Create a dictionary
Create a dictionary named person with keys:
name
age
city
2. Access a value
Print the value of "city" from the dictionary.
3. Add a new key
Add "country": "Pakistan" to the dictionary.
4. Update a value
Change age to any new number.
5. Delete a key
Remove "city" from the dictionary. """

person={
    'name':'zara',
    'age':25,
    'city':'wah cantt'
}
print("access city value")
print(person['city'])
print("adding country")
person['country']='pakistan'
print(person)
print("changing age value")
person['age']=26
print(person)
print("remove city from dict")
person.pop('city')
print(person)
print("we accessing both key & value")
for k in person:
   print(f"key:{k}, value:{person[k]}")


#Count how many values are integers
data = {"a": 10, "b": "hi", "c": 20, "d": 30}
count=0
for i in data:
    if type(data[i])==int:
        count+=1
print(count)

#Check if a key exists
#Check if "age" exists in the dictionary.
person={
    'name':'zara',
    'age':25,
    'city':'wah cantt'
}
if 'age' in person:
    print("yes age key exist")
else:
    print("dont exist")

#print highest marks of student
max=0
marks = {"math": 85, "english": 78, "science": 92}
for i in marks:
    if marks[i]>max:
        max=marks[i]
print(max)

#swap keys and values
a={"a": 1, "b": 2}
swap={value:key for key ,value in a.items()}
print(swap)

#count each number for how many times it come and print it in dictionary structure 
nums = [1,2,2,3,3,3,3,4]
counts={}
for i in range(len(nums)):
   count=0
   if nums[i] in counts:
        continue
   else:
    for j in range(0,(len(nums))):
       if nums[i]==nums[j]:
        count+=1
   counts[nums[i]]=count
print(counts)

#check same keys and then add same keys of values
a={"x":2,"y":3}
b={"y":4,"z":5}
c={}
for key in a:
    c[key]=a[key]
    if key in b:
     c[key]=c[key]+b[key]
for key in b:
    if key not in c:
       c[key]=b[key]
print(c)

#take the square of each key and then add into dict structure
a=[2,4,6]
b={}
for key in a:
    square=key*key
    b[key]=square
print(b)

#count the each letter for how many times it came
a = "banana"
b = {}

for i in a:
    if i in b:
        b[i] += 1   # now safe, b[i] is integer
    else:
        b[i] = 1    # initialize as integer

print(b)

#count the most repeated and print the repeated word and count
a = "success"
b = {}

for i in a:
    if i in b:
        b[i] += 1   # now safe, b[i] is integer
    else:
        b[i] = 1    # initialize as integer
max_char=max(b,key=b.get)
print("most repeated is :",max_char)
print("count: ",b[max_char])

#take input from user and count each letter
user_input=input()
print("enter input: ",user_input)
b={}
for i in user_input:
    if i in b:
        b[i]=b[i]+1
    else:
        b[i]=1
print(b)

#take input from user and only count that match with vowels
user_input=input()
print("enter input: ",user_input)
vowels=['a','e','i','o','u']
b={}
for i in user_input:
    if i in vowels:
        if i in b:
         b[i]=b[i]+1  
        else:
           b[i]=1    
    else:
       b[i]=0
print(b)

#take input and count and print only alphabets
user_input=input()
user_input=user_input.lower()
print("enter input: ",user_input)
b={}
for i in user_input:
    if i.isalpha():
     if i in b:
        b[i]=b[i]+1
     else:
        b[i]=1
    else:
       continue
print(b)


    




