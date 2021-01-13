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

    board =  [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 1]]

    player_one_name = str(input('Inserte el nombre del jugador 1 : '))
    player_two_name = str(input('Inserte el nombre del jugador 2 : '))

    winner(player_one_name, player_two_name)


def winner(player_one_name, player_two_name):

    winner_status = False

    while winner_status == False:

        player_one_option = int(input(f' {player_one_name} selecciona una casilla : ')) 
        player_two_option = int(input(f' {player_one_name} selecciona una casilla : '))
        
        
    

if __name__ == "__main__":
    run()