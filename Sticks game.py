import sys

def play_turn():
    # Core of the game - playturn func.
    global turns
    global sticks
    current_player = []
    turns += 1
    if turns % 2 != 0:
        current_player = p1
    elif turns % 2 == 0:
        current_player = p2
    sticks_taken = 0
    while sticks_taken not in range(1,4):
        try:
            sticks_taken = int(input(f"{current_player}, how many sticks do you take? : "))
        except ValueError:
            print("Nice try, smartass.")
        if sticks_taken not in range(1,4):
            print('Looks like wrong number of sticks to take. Try again!')
        elif sticks_taken > sticks:
            sticks_taken = 0
            print(f"You can't take more sticks than there is! Only {sticks} remains!")
    sticks -= sticks_taken
    if sticks == 0:
        if current_player == p1:
            return print(f'{p2} congratulations, you won!')
        else:
            return print(f'{p1} congratulations, you won!')
    else:
        return print(f'Starting next turn. Sticks left: {sticks}')

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


# Game itself

print("Welcome to the 10 sticks game!")
p1 = input("Player one, please enter your name: ")
p2 = input("Player two, please enter your name: ")
sticks = 10
turns = 0
print(f'Rules are simple. There are two players and {sticks} sticks on the table. Each turn player takes up to 3 sticks '
      f'from the table.Player, who picks last stick - loses. Do you want to play?')
wanna_play = " "
wp_yorn()
while wanna_play == 'yes':
    play_turn()
    if sticks > 0:
        play_turn()
        if sticks == 0:
            print('Wanna play again?')
            wp_yorn()
            turns = 0
            sticks = 10
    elif sticks == 0:
        print('Wanna play again?')
        wp_yorn()
        turns = 0
        sticks = 10
    else:
        break
