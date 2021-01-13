# Exercise 21

# Take the code from the How To Decode A Website exercise 
# (if you didn’t do it or just want to play with some different code, use the code from the solution)
# and instead of printing the results to a screen, write the results to a txt file. In your code,
# just make up a name for the file you are saving to.

# Extras:

# Ask the user to specify the name of the output file that will be saved.


import requests
from bs4 import BeautifulSoup


def run():
    
    name_file_txt = str(input('Ingresa el nombre del archivo : '))
    create_file(name_file_txt)


def create_file(name_file_txt):

    articles = get_articles()

    with open(name_file_txt, 'w') as open_file:
        for article in articles:
            open_file.write(f'{article.get_text()} \n')


def get_articles():

    url = "https://www.nytimes.com/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('h2')

    return articles

if __name__ == '__main__':
    run()
