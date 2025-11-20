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