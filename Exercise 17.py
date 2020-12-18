# Exercise 17

# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on
# the New York Times homepage.

import requests
from bs4 import BeautifulSoup


def run():

    url = "https://www.nytimes.com/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('h2', attrs={'class': 'css-1sk5x1x e1voiwgp0'})

    for article in articles:
        title = article.get_text()
        print(title)


if __name__ == '__main__':
    run()
