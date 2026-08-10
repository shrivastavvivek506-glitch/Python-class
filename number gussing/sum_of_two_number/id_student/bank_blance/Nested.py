# Nested If Example

age = 20
has_id = True

if age >= 18:
    print("You are eligible by age.")

    if has_id:
        print("Entry allowed.")
    else:
        print("ID card required.")

else:
    print("You are underage.")