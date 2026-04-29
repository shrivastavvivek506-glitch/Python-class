import random

# Computer selects a random number
secret_number = random.randint(1, 10)

print("🎯 Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10")

attempts = 0

# WHILE LOOP → runs until user guesses correctly
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print("✅ Correct! You guessed it in", attempts, "attempts")
        break
    elif guess < secret_number:
        print("📉 Too low! Try again.")
    else:
        print("📈 Too high! Try again.")

# FOR LOOP → show a summary after game ends
print("\n📊 Game Summary:")
for i in range(1, attempts + 1):
    print("Attempt", i)