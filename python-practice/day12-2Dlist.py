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