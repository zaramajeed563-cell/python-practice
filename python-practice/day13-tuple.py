#Multiple operations
#Create a tuple t = (5, 10, 15, 20, 25)
#Find sum of all elements
#Check if 15 is in the tuple
#Print the index of 20
t = (5, 10, 15, 20, 25)
sum=0
for i in range(len(t)):
    sum+=t[i]
print("sum is:",sum)
if 15 in t:
    print("15 is in tuple")
    for j in range(len(t)):
        if t[j]==20:
            print("index of 20 is", j)

#Tuple immutability check
#Given t = (1, 2, 3, [4, 5])
#Try to append 6 to the list inside tuple
#Print the tuple to see what changed
t=(1,2,3,[4,5])
t[3].append(6)
print(t)

#Given a tuple t = ("Python", "is", "fun") 
#Unpack the tuple into 3 variables and print them individually
t = ("Python", "is", "fun") 
a,b,c=t
print(a,b,c)

#Create a tuple with a single number 7 and print its type.
t=(7,)
print(type(t))

#Create and access
#Create a tuple t = (10, 20, 30, 40, 50)
#Print first element
#Print last element
#Print elements from index 1 to 3 (inclusive)
t = (10, 20, 30, 40, 50)
print("first element:",t[0])
print("second element",t[4])
print("the three elements are")
for i in range(1,(len(t)-1)):
    print(t[i])



