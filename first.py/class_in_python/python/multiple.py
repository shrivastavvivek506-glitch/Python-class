num =int (input("Enter number :"))
prod = 1
temp = num
while temp > 0:
    digit = temp % 10
    prod *=digit
    temp//=10
    print(prod)