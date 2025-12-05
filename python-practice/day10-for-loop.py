#🔹 Example 1: 1 se 5 tak numbers print 
for i in range(1,6):
    print(i) 

 #🔹 Example 2: String ke characters print karna
for char in "zara":
    print(char) 

#🔹 Example 3: List ke elements print karna
for list in [1,2,3,6,7]:
    print(list)

# Example 4 loop with end parameter
for language in ["C++","Java","Python"]:
    print(language, end="  ")

# 1 se 10 tak numbers ka sum nikalna
total=0
for i in range(1,5):
    total=total+i
    print(total)

# Table print karo (user se number lena)
table=int(input("enter value for table :"))
for i in range(1,11):
    result=table*i
    print(f"{table}*{i}={result}")

# Even numbers print karo (1 to 20)
for i in range(1,21):
    if i%2==0:
        print(i)


# 10 se 1 tak reverse counting
for i in range(10, 0,-1):
    print(i)

# Sirf odd numbers print karo (1 to 15)
for i in range(1,16):
    if i%2!=0:
        print(i)

 # sum of list 
words =([1,2,3,4,5,6])
count = 0
for word in words:
    count += (word)
print("Total sum:", count)

# character counting in list 
words =(["Python","C++"])
count = 0
for word in words:
    count += len(word)
print("Total sum:", count)


# using if and range printing those numbers that divisible by 3
for i in range(1,21):
    if i%3==0:
        print(i) 

#reverse string printing
word="python"
for i in range(len(word)-1,-1,-1):
 print(word[i],end="")

#vowel and consonants printing
sentence="i love python"
vowels =0
consonants=0
for i in sentence:
    if i.isalpha():
       if i.lower() in 'aeiou':
        vowels+=1
       else:
        consonants+=1
print(i, "-> vowels:", vowels, "consonants:", consonants)


#nested loop for 1-5 table printing
for table in range(1,6):
    for value in range(1,11):
        result=table*value
        print(f"{table}*{value}={result}")
    print(" ")

#print F with nested loop
num=[5,2,5,2,2]
for x in range(0,len(num)):
    for y in range(num[x]):
        print("*"*num[x],end=" ")
        print()
        break
    
        
    
    