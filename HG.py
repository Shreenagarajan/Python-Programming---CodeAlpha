import random

def hangman():
    # Predefined list of words
    words = ["python", "apple", "banana", "computer", "elephant"]
    
    # Randomly choose a word
    word = random.choice(words)
    guessed_letters = []  # To store the guessed letters
    attempts = 6          # Number of allowed incorrect guesses
    
    print("🎯 Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("_ " * len(word))
    
    # Main game loop
    while attempts > 0:
        guess = input("\nEnter a letter: ").lower()
        
        # Check for valid input
        if len(guess) != 1 or not guess.isalpha():
            print("❗ Please enter a single valid letter.")
            continue
        
        # Check if letter already guessed
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        # If the guessed letter is in the word
        if guess in word:
            print("✅ Good guess!")
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")
        
        # Display the current progress
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)
        
        # Check if the player has guessed all letters
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("\n💀 Out of attempts! The word was:", word)

# Run the game
hangman()
