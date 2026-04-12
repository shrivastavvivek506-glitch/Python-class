a = int(input("Enter number:"))
b = int(input("Enter number:"))
c = int(input("Enter number:"))

if a>b and a>c:
    print("Maximum:", a)

elif b>a and b>c:
    print("Maximum:", b)

elif c>a and b>c:
    print("maximum:", c)

else:
    print("All are equle")            