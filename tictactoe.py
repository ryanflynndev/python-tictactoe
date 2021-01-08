game_board = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
            ]


def display_game(game_board):
    print('Here is the current board:')
    for i in game_board:
        print(i)
    
def user_choice():

    choice = 'WRONG'
    acceptable_range = range(1,9)
    within_range = False

    while choice.isdigit() == False or within_range == False :
        choice = input("Please enter your position as a number (1-9): ")
        if choice.isdigit() == False:
            print("Sorry that is not a number!")
        if choice.isdigit():
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('Sorry the number must be 1-9!')
                within_range = False

    return int(choice)

def handle_input(user_choice):
    if user_choice in range(1, 3):
        game_board[0][user_choice - 1] = 'X'
    elif user_choice in range(4, 6):
        game_board[1][user_choice - 1] = 'X'
    else:
        game_board[1][user_choice - 1] = 'X'

display_game(game_board)
user_input = user_choice()
handle_input(user_input)
display_game(game_board)