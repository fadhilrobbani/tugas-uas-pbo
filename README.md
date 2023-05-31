# TUGAS UAS MATA KULIAH PEMROGRAMAN BERBASIS OBJEK

Anggota Kelompok:
- G1A020036 - Fadhilla Ilham Robbani
- G1A021 
- G1A021

##ini penjelasan versi gpt sebagai referensi aj (diedit lg ntar yo)


```py
    import random
```
Baris ini mengimpor modul random yang akan digunakan untuk memilih kata secara acak dari daftar kata.



```py
class Hangman:
    def __init__(self):
        self.word_list = ["python", "hangman", "computer", "programming", "game", "openai"]
        self.chosen_word = random.choice(self.word_list)
        self.guessed_letters = []
        self.tries = 6
```
Kode ini mendefinisikan kelas Hangman. Konstruktor kelas __init__ menginisialisasi atribut-atribut seperti word_list (daftar kata yang mungkin), chosen_word (kata yang dipilih secara acak dari daftar), guessed_letters (daftar huruf yang telah ditebak), dan tries (jumlah kesempatan yang tersisa).



```py   
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
```

Metode play digunakan untuk menjalankan permainan Hangman. Selama tries (jumlah kesempatan yang tersisa) lebih besar dari 0, permainan akan berlanjut.

Dalam setiap iterasi, variabel word_status digunakan untuk membangun tampilan kata yang harus ditebak dengan underscore (_) untuk huruf-huruf yang belum ditebak.

Jika word_status sama dengan chosen_word, artinya pemain berhasil menebak seluruh huruf dalam kata yang dipilih. Pernyataan "Congratulations! You guessed the word:" akan ditampilkan, diikuti dengan kata yang benar. Loop akan dihentikan dengan break.

Jika tries habis (sudah tidak ada kesempatan lagi), pesan "Game over! The word was" akan ditampilkan, diikuti dengan kata yang benar. Loop akan selesai dengan else.


```py    
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
            # Kode ASCII art untuk state hangman lainnya
        ]

        print(hangman_states[6 - self.tries])
```

Metode display_hangman menggunakan list hangman_states yang berisi kode ASCII art untuk setiap state hangman. Sesuai dengan nilai tries, kode ASCII art yang sesuai akan dipilih dan ditampilkan menggunakan perintah print(hangman_states[6 - self.tries]).


```py
game = Hangman()
game.play()
```

Pada bagian akhir kode, sebuah objek game dibuat dari kelas Hangman, dan metode play dipanggil untuk memulai permainan. Ini menjalankan logika permainan Hangman dengan memanfaatkan kelas Hangman dan metode yang ada di dalamnya.

Dengan menjalankan kode ini, Anda dapat memainkan permainan Hangman dalam lingkungan Python. Setiap kali Anda menjalankannya, kata yang harus ditebak akan dipilih secara acak, dan Anda dapat memberikan tebakan huruf untuk menebak kata tersebut. State hangman akan ditampilkan dalam bentuk ASCII art setiap kali Anda memberikan tebakan yang salah, dan informasi tentang kata yang harus ditebak dan kesempatan yang tersisa akan ditampilkan di setiap iterasi.