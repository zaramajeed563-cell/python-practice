#Print every element of a 2D list one by one.
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in A:
    for i in row:
        print(i)

#Print the first row of a 2D list.
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(A[0])

#Print the last row of a 2D list.
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(A[2])

#Print the first element of each row.
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in A:
    print(row[0])

#Print the last element of each row.
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in A:
    print(row[-1])

#For each row, print all elements on the same line.
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in A:
    for i in row:
        print(i,end=" ")

#Count how many numbers are in the 2D list.
count=0
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in A:
    count+=len(row)
print(count)

#Calculate the sum of all numbers in the 2D list.
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum=0
for row in A:
    for i in row:
        sum+=i
print(f"sum is {sum}")

#Find the largest number in the 2D list.
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
max=A[0][1]
for i in A:
    for y in i:
     if y>=max:
        max=y
print(max)

#Find the smallest number in the 2D list.
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
min=A[0][1]
for i in A:
    for y in i:
     if y<=min:
        min=y
print(min)

#Count how many even numbers exist.
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
count=0
for row in A:
    for i in row:
        if i%2==0:
            count+=1
print(f"total even numbers are = {count}")

#Count how many odd numbers exist.
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
count=0
for row in A:
    for i in row:
        if i%2!=0:
            count+=1
print(f"total odd numbers are = {count}")

#Print all numbers greater than 10.
D = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [100, 110, 120]
]
print("greater than 100:")
#f=D[0][0]
for row in D:
    for i in row:
        if i>100:
            print(i)

#Replace every even number with "EVEN" in a new 2D list.
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
new_list=[]
for row in A:
    new_row=[]
    for i in row:
        if i%2==0:
            new_row.append("EVEN")
        else:
            new_row.append(i)
    new_list.append(new_row)
print(new_list)

#Count how many times a specific number (like 5) appears in the 2D list.
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
count=0
for row in A:
    for i in row:
        if i==5:
            count+=1
print(f"5 came for {count} time only")

#Print the sum of each row separately.
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
new_list=[]
sum=0
for row in A:
    new_row=[]
    for i in row:
     sum+=i
    new_row.append(sum)
    new_list.append(new_row)
print(new_list)

#Print the sum of each column separately.
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
new_list=[]
for col in range(len(A[0])):
    sum=0
    for row in range(len(A)):
        sum+=A[row][col]
    new_list.append(sum)
print(new_list)

#Print each column on a separate line
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for col in range(len(A[0])):
    for row in range(len(A)):
        print(A[row][col],end=" ")
    print()

#Print only the first column
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in range(len(A)):
    print(A[row][0])

#Print only the last column
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in range(len(A)):
    print(A[row][2])

#Count how many even numbers are in each column
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for col in range(len(A[0])):
    count=0
    for row in range(len(A)):
            if A[row][col]%2==0:
                count+=1
    print(f"{col} Column {count} even")

#Find the maximum number in each column
A = [
    [1, 2, 3],
    [4, 11, 6],
    [7, 8, 9]
]
for col in range(len(A[0])):
    max = A[0][col]
    for row in range(len(A)):
            if A[row][col]>=max:
                max=A[row][col]
    print(max)

#transpose rows into columns
A = [
    [1, 2, 3],
    [4, 11, 6],
    [7, 8, 9]
]
for col in range(len(A[0])):
    for row in range(len(A)):
        print(A[row][col],end=" ")
    print()
#sort the columns
A = [
    [8, 2, 3],
    [4, 11, 6],
    [7, 8, 9]
]
for col in range(len(A[0])):
    new_list=[]
    print()
    for row in range(len(A)):
        new_list.append(A[row][col]) 
    new_list.sort() 
    print(new_list,end=" ")

# 1D sorting
A = [8, 2, 3]
for i in range(len(A)):
    for j in range(len(A)-1):
        if A[j]>=A[j+1]:
            A[j],A[j+1]=A[j+1],A[j]
print(A)

# 2d row sorting
A = [
    [8, 2, 3],
    [4, 11, 6],
    [7, 8, 9]
]
for row in range(len(A)):
    for col in range(len(A)-1):
        if A[row][col]>=A[row][col+1]:
            A[row][col],A[row][col+1]=A[row][col+1],A[row][col]
print(A)

# 2d column sorting
A = [
    [8, 2, 3],
    [4, 11, 6],
    [7, 8, 9]
]
for col in range(len(A)):
    for row in range(len(A)-1):
        if A[row][col]>=A[row+1][col]:
            A[row][col],A[row+1][col]=A[row+1][col],A[row][col]
for row in A:
    print(row)

    





