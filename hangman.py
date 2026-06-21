import random

# Words with categories
word_data = {
    "python": "Programming Language",
    "apple": "Fruit",
    "computer": "Technology",
    "internship": "Career",
    "coding": "Programming"
}

word = random.choice(list(word_data.keys()))
category = word_data[word]

guessed_word = ["_"] * len(word)
incorrect_guesses = 0
max_guesses = 6
guessed_letters = []

print("🎮 Welcome to CodeAlpha Hangman Game!")
print(f"📌 Category: {category}")
print("Guess the word one letter at a time.")

while incorrect_guesses < max_guesses and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses left:", max_guesses - incorrect_guesses)

    if max_guesses - incorrect_guesses <= 3:
        print("💡 Type 'hint' for a clue!")

    guess = input("Enter a letter or 'hint': ").lower()

    if guess == "hint":
        print(f"💡 Hint: The word belongs to '{category}' category.")
        continue

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong Guess!")
        incorrect_guesses += 1

if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n😢 Game Over!")
    print("The correct word was:", word)