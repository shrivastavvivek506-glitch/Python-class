location = input("Enter your Location: ")
if location == "New York":
    age = int (input("Enter your age :")) 
    if age > 18:
        print("Your are eligible to vote:")
    elif age < 60:
        print("You are course for age limit:")
else:
     print("You are not eligible to vote.")