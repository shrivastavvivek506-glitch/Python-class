location = input("Enter your loction : ")
if location == "motihari":
    age  = int(input("Enter your age: "))

    if age >= 18 and age < 60:
        print("you are eligible to vote: ")
    elif age >= 60:
        print("you are above the age limit ")
    else:
        print("You are below the minimum age.")
    
else:
    print("You are not eligible to vote.")

