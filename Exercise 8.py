# Exercise 8

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

from os import system
from getpass import getpass


def run():

    play_or_exit()


def play_or_exit():

    por_option = ''

    while por_option != 'p' or por_option != 'q':

        por_option = str(input('\nBienvenido, para jugar una partida presione P, para salir presione Q : ')).lower()

        if por_option == 'p':
            system('cls')
            input_players()

        elif por_option == 'q':
            system(exit())


def input_players():

    print('*' * 55)
    print('\t\tPiedra Papel o Tijeras')
    print('*' * 55)

    player_one_name = str(input('\nCual es el nombre del jugador 1 ? : '))
    player_two_name = str(input('Cual es el nombre del jugador 2 ? : '))
    system('cls')

    player_one_option = str(getpass(f'{player_one_name} escribe piedra, papel o tijeras : ')).lower()
    player_two_option = str(getpass(f'{player_two_name} escribe piedra, papel o tijeras : ')).lower()
    system('cls')

    print_winner(player_one_name, player_two_name, player_one_option, player_two_option)


def print_winner(player_one_name, player_two_name, player_one_option, player_two_option):

    list_words = ['piedra', 'papel', 'tijeras']

    if player_one_option not in list_words:
        print(f'{player_one_name} La palabra que ingresaste no es valida')

    elif player_two_option not in list_words:
        print(f'{player_two_name} La palabra que ingresaste no es valida')

    else:

        status = 'No definido'

        if player_one_option == player_two_option:
            status = 'Empate'

        elif player_one_option == 'piedra':
            if player_two_option == 'papel':
                status = f'Victoria para {player_two_name}'
            else:
                status = f'Victoria para {player_one_name}'

        elif player_one_option == 'papel':
            if player_two_option == 'piedra':
                status = f'Victoria para {player_one_name}'
            else:
                status = f'Victoria para {player_two_name}'

        elif player_one_option == 'tijeras':
            if player_two_option == 'papel':
                status = f'Victoria para {player_one_name}'
            else:
                status = f'Victoria para {player_one_name}'

        print(f'''
            Resultado de la partida 
            
            {player_one_name} selecciono {player_one_option}
            {player_two_name} selecciono {player_two_option}
            
            Por lo tanto es {status}
        ''')

        (input('Presiona una tecla para continuar...'))
        system('cls')


if __name__ == '__main__':
    run()
