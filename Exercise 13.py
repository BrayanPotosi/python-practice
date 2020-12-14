# Exercise 13

# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum
# of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def run():

    number_fibonacci = int(input('Cuantos numeros desea generar ? : '))
    print(check_fibonacci(number_fibonacci))


def check_fibonacci(number_fibonacci):

    fibonacci_list = []
    first_number = 0
    second_number = 1

    for i in range(number_fibonacci):

        fibonacci_list.append(first_number)

        sumn = first_number + second_number
        first_number = second_number
        second_number = sumn

    return fibonacci_list


if __name__ == '__main__':
    run()
