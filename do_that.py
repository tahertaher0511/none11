import random

global variables
game_still_going = True
winner = None
current_player = 'X'
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def display_board():
    global board
    print('-' * 9)
    print('| ' + board[0] + ' ' + board[1] + ' ' + board[2] + ' |', '               ', '>',     '(1 1)' '(2 3)' '(3 3)')
    print('| ' + board[3] + ' ' + board[4] + ' ' + board[5] + ' |', '               ', '>',     '(1 2)' '(2 2)' '(3 2)')
    print('| ' + board[6] + ' ' + board[7] + ' ' + board[8] + ' |', '               ', '>',     '(1 1)' '(2 1)' '(3 1)')
    print('-' * 9)


def play_game():
    display_board()
    while game_still_going:
        process_input()
        check_if_game_over()
        move_easy()

        # the gamed has ended.
    if winner is None:
        print('Draw')
    elif winner == 'X' or winner == 'O':
        print(winner, 'wins')


def process_input():
    global current_player
    while True:
        try:
            coordinates_input = input('Enter the coordinates: ').split()
            if coordinates_input[0].isnumeric() is False or coordinates_input[1].isnumeric() is False:
                print('You should enter numbers!')
            else:
                x = int(coordinates_input[0])
                y = int(coordinates_input[1])
                if 1 <= x <= 3 and 1 <= y <= 3:
                    if board[(3 - y) * 3 + (x - 1)] == ' ':
                        board[(3 - y) * 3 + (x - 1)] = current_player
                        display_board()
                        check_if_game_over()
                        break
                    else:
                        print('This cell is occupied choose another one!')
                else:
                    print('Coordinates should be from 1 to 3!')
        except IndexError or NameError or ValueError:
            print('Coordinates should be from 1 to 3!')


def move_easy():
    for i in range(100):
        a = random.randint(0, 8)
        if board[a] == ' ' and board[a] != '_':
            board[a] = 'O'
            print('Making move level"easy"')
            display_board()
            check_if_game_over()
            break


def check_if_game_over():
    check_if_win()
    check_if_draw()

    return


def check_if_win():
    global winner
    rows_winner = check_rows()
    col_winner = check_col()
    diagonal_winner = check_diagnoal()
    if rows_winner:
        winner = rows_winner
    elif col_winner:
        winner = col_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != ' '
    row_2 = board[3] == board[4] == board[5] != ' '
    row_3 = board[6] == board[7] == board[8] != ' '
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]


def check_col():
    global game_still_going
    col_1 = board[0] == board[3] == board[6] != ' '
    col_2 = board[1] == board[4] == board[7] != ' '
    col_3 = board[2] == board[5] == board[8] != ' '
    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return board[0]
    elif col_2:
        return [1]
    elif col_3:
        return board[2]


def check_diagnoal():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != ' '
    diagonal_2 = board[2] == board[4] == board[6] != ' '
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None


def check_if_draw():
    global game_still_going
    if ' ' not in board:
        game_still_going = False
        return True
    else:
        return False


play_game()
