import random
board = [
    {'0': '-', '1': '-', '2': '-'},
    {'0': '-', '1': '-', '2': '-'},
    {'0': '-', '1': '-', '2': '-'}
]

choose_players =int(input("Chose 1 for 1vs1 or 2 for 1vsPC or 3 for PCvsPC: "))
def player1 ():
    print("Player 1 Turn")
    if choose_players == 3:
        input1_column = random.randint(0,2)
        input1c_row = random.randint(0,2)
    else:
        input1_column = int(input("Choose a column: "))
        input1c_row = int(input("Choose a row: "))
    if board[input1c_row][str(input1_column)] == '-':
        board[input1c_row][str(input1_column)] = 'X'
    else:
        print("Choose another Column or Row")
        player1()

def player2 ():
    print("Player 2 Turn")
    if choose_players == 1:
        input1_column = int(input("Choose a column: "))
        input1c_row = int(input("Choose a row: "))
    else:
        input1_column = random.randint(0,2)
        input1c_row = random.randint(0,2)
    if board[input1c_row][str(input1_column)] == '-':
        board[input1c_row][str(input1_column)] = 'O'
    else:
        print("Choose another Column or Row")
        player2()

def print_board():
    for row in board:
        for key in row:
            print(row[key], end=' ')
        print('')

def check_winner():
    # check rows
    for row in board:
        if row['0'] == row['1'] == row['2'] != '-':
            return False

    # check columns
    for col in ['0', '1', '2']:
        if board[0][col] == board[1][col] == board[2][col] != '-':
            return False

    # check diagonals
    if board[0]['0'] == board[1]['1'] == board[2]['2'] != '-':
        return False
    if board[0]['2'] == board[1]['1'] == board[2]['0'] != '-':
        return False

    return True


for i in range(9):
    if i%2==0:
        print_board()
        player1 ()
        if check_winner() == False:
            print_board()
            print("Player 1 has won")
            break
    else:
        print_board()
        player2 ()
        if check_winner() == False:
            print_board()
            print("Player 2 has won")
            break
else:
    print_board()
    print("The game is a draw")



