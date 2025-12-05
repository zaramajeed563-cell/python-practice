# * printing
i=1
n=5
while i<=n:
     print(i * '*')
     i=i+1

# triangle printing
i=1
n=5
while i<=n:
     spaces=n-i
     star=2*i-1
     print(" "*spaces +"*" *star)
     i=i+1

# reverse digit printing
reverse=0
number=int(input("enter number"))
while number>0:
    last_digit=number%10
    number = number // 10
    reverse=10*reverse+last_digit
    print(reverse)

print("done")

# table printing
table=int(input("enter input for table :"))
i=1
while i<=10:
    ans=table*i
    #print(ans)
    print(f"{table}*{i}={ans}")
    i=i+1