def run():
    user_num = int(input('Ingrese un numero : '))

    divisors(user_num)


def divisors(user_num):

    list_divisors = []
    for i in range(user_num):
        if user_num % (i + 1) == 0:
            list_divisors.append(i + 1)

    print(f'Lista de divisores de {user_num} : {list_divisors}')


if __name__ == '__main__':
    run()
