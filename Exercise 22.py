# Exercise 22

# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, 
# and print out the results to the screen. I have a .txt file for you, if you want to use it!

def run():

    names_dict = {}
    count_names(names_dict)


def count_names(names_dict):

    with open('names.txt', 'r') as file_names:
        line = file_names.readline()

        while line:

            line = line.strip()

            if line in names_dict:
                names_dict[line] += 1
            else:
                names_dict[line] = 1

            line = file_names.readline()
    
    print (names_dict)

if __name__ == '__main__':
    run()
