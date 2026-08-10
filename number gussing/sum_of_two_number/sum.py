a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

total = a + b + c
print("Sum =", total)

if total % 2 == 0:
    print("The sum is Even")
else:
    print("The sum is Odd")