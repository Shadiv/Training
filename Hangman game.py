# Hangman

from random_word import RandomWords


class HangmanGame:

    def __init__(self):
        self.player = input('Please, enter your name: ')
        self.field = '       \n       \n       \n       \n       \n       \n'
        self.wanna_play = ''
        self.secret_word = ''
        self.guesses = 8
        self.fails = 0
        self.blanks = []

    def wp_yorn(self):
        while True:
            self.wanna_play = input("Please enter Yes or No: ").lower()
            if self.wanna_play == 'yes':
                break
            elif self.wanna_play == 'no':
                print('See ya next time, bye')
                break
            else:
                print("I don't understand. You have to choose Yes or No")

    def start_game(self):
        rw = RandomWords().get_random_word()
        self.secret_word = [i for i in rw]
        self.blanks = ['_' for _ in self.secret_word]
        print('Well, I made up a secret word. It has this much letters')
        print(self.secret_word)
        print(self.blanks)

    @staticmethod
    def end_game_lose():
        return 'Unfortunately, you lost!'

    @staticmethod
    def end_game_win():
        return 'Congratulations! You won!'

    def guess_the_letter(self):
        player_guess = input('Guess the letter: ')
        if player_guess in self.secret_word:
            for i, w in enumerate(self.secret_word):
                if w == player_guess:
                    self.blanks[i] = w
            return True
        else:
            self.fails += 1
            return False


    def play_game(self):
        fail8 = ' _____\n |   |\n O   |\n/|\  |\n/ \  |\n     |\n'
        fail7 = ' _____\n |   |\n O   |\n/|\  |\n/    |\n     |\n'
        fail6 = ' _____\n |   |\n O   |\n/|\  |\n     |\n     |\n'
        fail5 = ' _____\n |   |\n O   |\n/|   |\n     |\n     |\n'
        fail4 = ' _____\n |   |\n O   |\n |   |\n     |\n     |\n'
        fail3 = ' _____\n |   |\n O   |\n     |\n     |\n     |\n'
        fail2 = ' _____\n |   |\n     |\n     |\n     |\n     |\n'
        fail1 = ' _____\n     |\n     |\n     |\n     |\n     |\n'

        #  _____
        #  |   |
        #  O   |
        # /|\  |
        # / \  |
        #      |
        guess = HangmanGame.guess_the_letter(self)
        if guess is True:
            print('Well done, there is such a letter! Lets add it to our word :)')
            print(self.blanks)
            if self.blanks == self.secret_word:
                return print(HangmanGame.end_game_win())
            else:
                HangmanGame.play_game(self)
        elif guess is False:
            if self.fails == 1:
                print('Unfortunately there is no such letter')
                print(fail1)
                HangmanGame.play_game(self)
            elif self.fails == 2:
                print('Unfortunately there is no such letter')
                print(fail2)
                HangmanGame.play_game(self)
            elif self.fails == 3:
                print('Unfortunately there is no such letter')
                print(fail3)
                HangmanGame.play_game(self)
            elif self.fails == 4:
                print('Unfortunately there is no such letter')
                print(fail4)
                HangmanGame.play_game(self)
            elif self.fails == 5:
                print('Unfortunately there is no such letter')
                print(fail5)
                HangmanGame.play_game(self)
            elif self.fails == 6:
                print('Unfortunately there is no such letter')
                print(fail6)
                HangmanGame.play_game(self)
            elif self.fails == 7:
                print('Unfortunately there is no such letter')
                print(fail7)
                HangmanGame.play_game(self)
            elif self.fails == 8:
                print('Unfortunately there is no such letter')
                print(fail8)
                return print(HangmanGame.end_game_lose())


hangman_game = HangmanGame()
print('Do you wanna play hangman with me? ')
hangman_game.wp_yorn()
while hangman_game.wanna_play == 'yes':
    hangman_game.fails = 0
    hangman_game.start_game()
    hangman_game.play_game()
    print('Thanks for playing. Wanna play again?')
    hangman_game.wp_yorn()