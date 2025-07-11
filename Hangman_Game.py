import random


word_list = ["apple", "tiger", "plane", "house", "robot"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = ["_" for _ in chosen_word]

lives = 6
guessed_letters = []

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.\n")


while lives > 0 and "_" in display:
    print("Current word:", " ".join(display))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try a new one.\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
        print("Correct guess!\n")
    else:
        lives -= 1
        print(f"Incorrect! You have {lives} lives remaining.\n")

if "_" not in display:
    print("🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("💀 Game Over! The word was:", chosen_word)
