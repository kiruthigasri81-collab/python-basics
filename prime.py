num=int(input("Enter the num:"))
if num <= 1:
    print("Not a prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime")
            break
        else:
            print("Prime")   