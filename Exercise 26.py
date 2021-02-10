#Exercise 26

# This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.

# As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, 
# this is significantly more than half an hour of coding, so we’re doing it in pieces.

# Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.

# If a game of Tic Tac Toe is represented as a list of lists, like so:

# game =  [[1, 2, 0],
#	      [2, 1, 0],
#	     [2, 1, 1]]

def run():

    player_one_name = str(input('\nInserte el nombre del jugador 1 : '))
    player_two_name = str(input('Inserte el nombre del jugador 2 : '))

    winner(player_one_name, player_two_name)


def add_board(player, row, col):

    if board[row][col] == 0:
        board[row][col] = player
    else:
        print('\nCasilla ocupada, ingrese otra posicion\n')

    for row in board:
            print (row)


def horizontal():
    for i in range(3):
        current_box = board[i][0]

        new_box = True

        if 0 in board[i]:
            new_box = False

        for j in range(1,3):
            new_box = new_box and (current_box == board[i][j])

        if new_box:
            break
            
    return new_box


def vertical():
    for i in range(3):
        current_box = board[0][i]

        new_box = True

        if 0 in board[i]:
            new_box = False

        for j in range(1,3):
            new_box = new_box and (current_box == board[j][i])

        if new_box:
            break
            
    return new_box


def diagonal():
    pass

def winner(player_one_name, player_two_name):

    no_winner = True
    turns = 9
    win_counter_1 = 0
    win_counter_2 = 0

    while no_winner or turns > 1 :

        player_one_row = int(input(f'\n {player_one_name} selecciona la fila  : ')) 
        player_one_col = int(input(f' {player_one_name} selecciona la columna  : '))
        add_board(1, player_one_row, player_one_col)

        turns -= 1

        if horizontal() or vertical() :
            print('\nGano el jugador 1')
            win_counter_1 += 1
            break
            
        player_two_row = int(input(f'\n {player_two_name} selecciona la fila  : ')) 
        player_two_col = int(input(f' {player_two_name} selecciona la columna  : '))
        add_board(2, player_two_row, player_two_col)

        turns -= 1

        if horizontal() or vertical() :    
            no_winner = False
            print('\nGano el jugador 2')
            win_counter_2 += 1
            break


    print(f'\nVictorias {player_one_name} : {win_counter_1}, Victorias {player_two_name} : {win_counter_2}') 

if __name__ == "__main__":

    board = [[0, 0, 0], [0, 0, 0],[0, 0, 0]]
    run()