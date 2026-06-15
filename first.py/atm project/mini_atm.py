balance = 1000

while True:
    print("\n🏦 ATM Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("💰 Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("✅ Deposited successfully")

    elif choice == 3:
        amount = int(input("Enter withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print("✅ Withdraw successful")
        else:
            print("❌ Insufficient balance")

    elif choice == 4:
        print("\n📊 Last 5 balance checks:")
        for i in range(1, 6):
            print("Check", i, ":", balance)
        break

    else:
        print("❌ Invalid choice")