import random

def hangman():
    word_list = ["python", "hangman", "computer", "programming", "game", "openai"]
    chosen_word = random.choice(word_list)
    guessed_letters = []
    tries = 6

    hangman_states = [
        """
           _______
          |/      |
          |      
          |      
          |       
          |      
          |
         _|_
        |   |______
        |          |
        |__________|
        """,
        """
           _______
          |/      |
          |      (_)
          |      
          |       
          |      
          |
         _|_
        |   |______
        |          |
        |__________|
        """,
        """
           _______
          |/      |
          |      (_)
          |       |
          |       |
          |       
          |
         _|_
        |   |______
        |          |
        |__________|
        """,
        """
           _______
          |/      |
          |      (_)
          |      \\|
          |       |
          |       
          |
         _|_
        |   |______
        |          |
        |__________|
        """,
        """
           _______
          |/      |
          |      (_)
          |      \\|/
          |       |
          |       
          |
         _|_
        |   |______
        |          |
        |__________|
        """,
        """
           _______
          |/      |
          |      (_)
          |      \\|/
          |       |
          |      / 
          |
         _|_
        |   |______
        |          |
        |__________|
        """,
        """
           _______
          |/      |
          |      (_)
          |      \\|/
          |       |
          |      / \\
          |
         _|_
        |   |______
        |          |
        |__________|
        """
    ]

    while tries > 0:
        word_status = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                word_status += letter
            else:
                word_status += "_"

        if word_status == chosen_word:
            print("Congratulations! You guessed the word:", chosen_word)
            break

        print(hangman_states[6 - tries])
        print("Guess the word:", word_status)
        print("Tries left:", tries)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        if guess not in chosen_word:
            print("Wrong guess!")
            tries -= 1

        guessed_letters.append(guess)

    else:
        print(hangman_states[6 - tries])
        print("Game over! The word was", chosen_word)

hangman()