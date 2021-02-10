#Exercise 33

# For this exercise, we will keep track of when our friend’s birthdays are, 
# and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays. 
# When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. 
# The interaction should look something like this:

import json


def run():
    
    birthdays_dict = {"nombre":'aaaa', "fecha":"12/03/1883"}
    add_data(birthdays_dict)

def add_data(birthdays_dict):

    with open("birthday.json", "r") as open_jsonx:
        birthday_data = json.load(open_jsonx)


    if not 'data' in birthday_data:
        birthday_data["data"] = []

    birthday_data["data"].append(birthdays_dict)

    print(birthday_data)

    with open("birthday.json", "w") as open_jsonx:
        json.dump(birthday_data, open_jsonx, indent=4)
    
    
    {
	"May": 3,
	"November": 2,
	"December": 1
    }   

if __name__ == '__main__':
    run()