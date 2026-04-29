questions = ["Capital of India?", "2 + 2 = ?", "Sun rises from?"]
answers = ["delhi", "4", "east"]

score = 0

for i in range(len(questions)):
    user = input(questions[i] + " ").lower()
    if user == answers[i]:
        print("✅ Correct")
        score += 1
    else:
        print("❌ Wrong")

print("🎯 Your score:", score)

# retry using while loop
while True:
    retry = input("Play again? (yes/no): ").lower()
    if retry == "no":
        break
    elif retry == "yes":
        print("Restart the program to play again")
        break