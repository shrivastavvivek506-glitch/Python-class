a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
c = int(input("Enter the third number :"))

if a > b and  a > c:
    print("First number is the grater number :")

elif b > a and b > c:
    print("Second number is the grater number :")

elif c > a and c > b:
    print("Third number is the grater number :")

else:
    print("All  number are the equle :")