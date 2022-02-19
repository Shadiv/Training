class GameField:
    field = []

    def __init__(self):
        GameField.field = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
        print('\n', GameField.field[:3], '\n', GameField.field[3:6], '\n', GameField.field[6:])

    @staticmethod
    def win_cond():
        win_1x = [i for i in GameField.field[:3] if i == "X"]
        win_1o = [i for i in GameField.field[:3] if i == "O"]
        win_2x = [i for i in GameField.field[3:6] if i == "X"]
        win_2o = [i for i in GameField.field[6:] if i == "X"]
        win_3x = [i for i in GameField.field[3:6] if i == "O"]
        win_3o = [i for i in GameField.field[6:] if i == "O"]
        win_4x = [i for i in GameField.field[1::3] if i == "X"]
        win_4o = [i for i in GameField.field[1::3] if i == "O"]
        win_5x = [i for i in GameField.field[2::3] if i == "X"]
        win_5o = [i for i in GameField.field[2::3] if i == "O"]
        win_6x = [i for i in GameField.field[::4] if i == "X"]
        win_6o = [i for i in GameField.field[::4] if i == "O"]
        win_7x = [i for i in GameField.field[2:7:1] if i == "X"]
        win_7o = [i for i in GameField.field[2:7:1] if i == "O"]
        if len(win_1o) == 3 or len(win_2o) == 3 or len(win_3o) == 3 or len(win_4o) == 3 or len(win_5o) == 3 or \
                len(win_6o) == 3 or len(win_7o) == 3:
            print('player two (O) wins!')
            return 1
        elif len(win_1x) == 3 or len(win_2x) == 3 or len(win_3x) == 3 or len(win_4x) == 3 or len(win_5x) == 3 or \
                len(win_6x) == 3 or len(win_7x) == 3:
            print('player one (X) wins!')
            return 1
        else:
            return 0


class Game(GameField):

    turns = 0

    def __init__(self, p1, p2):
        super().__init__()
        self.p1 = p1
        self.p2 = p2

    def play_turn(self):
        Game.turns += 1
        current_player = []
        if Game.turns % 2 != 0:
            current_player = self.p1
        elif Game.turns % 2 == 0:
            current_player = self.p2
        print(f'{current_player} your turn')
        avaliable_fields = [i for i, item in enumerate(GameField.field) if item == "_"]
        print(f'Please, enter number of field you want to fill {avaliable_fields}')
        while True:
            play = ""
            try:
                play = int(input("Please enter field number: "))
            except ValueError:
                print("Nice try, smartass.")
            if play in avaliable_fields:
                break
            else:
                print('Seems like wrong number of field, try again')
        if current_player == self.p1:
            GameField.field[play] = 'X'
        if current_player == self.p2:
            GameField.field[play] = 'O'
        print('\n', GameField.field[:3], '\n', GameField.field[3:6], '\n', GameField.field[6:])
        GameField.win_cond()


def wp_yorn():
    while True:
        global wanna_play
        wanna_play = input("Please enter Yes or No: ").lower()
        if wanna_play == 'yes':
            break
        elif wanna_play == 'no':
            print('See you next time! Bye!')
            break
        else:
            print("You have to choose Yes or No")


wanna_play = " "
print('Hello, welcome to the game. Do you want to play X/O? ')
wp_yorn()
x_o_game = Game(p1=input('Player one please enter your name: '), p2=input('Player two please enter your name: '))
while wanna_play == "yes":
    field_x_o = GameField
    x_o_game.play_turn()
    field_x_o.win_cond()
    if field_x_o.win_cond() == 0:
        x_o_game.play_turn()
    else:
        print('Wanna play again? ')
        wp_yorn()
        field_x_o.field = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
        x_o_game.turns = 0

print('Thanks for playing')


