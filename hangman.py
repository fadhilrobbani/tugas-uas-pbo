import random

class Hangman:
    def __init__(self):
        self.word_list = ["python", "hangman", "computer", "programming", "game", "openai"]
        self.chosen_word = random.choice(self.word_list)
        self.guessed_letters = []
        self.tries = 6

    def play(self):
        while self.tries > 0:
            word_status = ""
            for letter in self.chosen_word:
                if letter in self.guessed_letters:
                    word_status += letter
                else:
                    word_status += "_"

            if word_status == self.chosen_word:
                print("Congratulations! You guessed the word:", self.chosen_word)
                break

            self.display_hangman()
            print("Guess the word:", word_status)
            print("Tries left:", self.tries)

            guess = input("Enter a letter: ").lower()

            if len(guess) != 1:
                print("Please enter a single letter.")
                continue

            if guess in self.guessed_letters:
                print("You've already guessed that letter.")
                continue

            if guess not in self.chosen_word:
                print("Wrong guess!")
                self.tries -= 1

            self.guessed_letters.append(guess)

        else:
            self.display_hangman()
            print("Game over! The word was", self.chosen_word)

    def display_hangman(self):
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

        print(hangman_states[6 - self.tries])

game = Hangman()
game.play()
