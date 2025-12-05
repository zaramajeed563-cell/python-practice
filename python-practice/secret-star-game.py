username=input("enter username: ")
secret_number=int(input("enter secret number: "))
while True:
    guess=int(input("guess number: "))
    if guess<1 or guess>100:
        print("invalid guess!")
        continue
    if guess==secret_number:
        print(f"username is: {username}")
        if guess % 2 == 0:
            for i in range(1, guess + 1):
                for j in range(i):
                    print("*", end="")
                print()  # <-- line break inside outer loop
        else:
            for i in range(guess,0,-1):
                for j in range(i):
                    print("*", end="")
                print()  # <-- line break inside outer loop

        break
    elif guess>secret_number:
        print("too high!")
    else:
        print("too low!")