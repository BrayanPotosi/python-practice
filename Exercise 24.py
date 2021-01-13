# Exercise 24 

# This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.

# Time for some fake graphics! Let’s say we want to draw game boards that look like this:

def run():

    number_rows_cols = int(input('Digite la dimension del tablero : '))

    create_board(number_rows_cols)


def create_board(number_rows_cols):

    for i in range(number_rows_cols):
        print(" --- " * number_rows_cols )
        print("|    " * (number_rows_cols + 1))


if __name__ == '__main__':
    run()
