# -- coding: utf-8 --

import requests
from bs4 import BeautifulSoup
import time

"""
links = []

for i in range(1, 51):
    url = "https://books.toscrape.com/catalogue/page-" + str(i) + ".html"
    response = requests.get(url)
    print(response)

    if response.ok:
        print("Page " + str(i))
        soup = BeautifulSoup(response.text, "html.parser")
        # récuperer le titre de la page
        title = soup.find('title')
        articles = soup.find_all('article')
        # print(len(articles))
        # [print(str(article) + "\n\n") for article in articles]
        for article in articles:
            # print(article)
            a = article.find('a')
            link = a["href"]  # chercher l'attribut href de la balise a
            # print(link)
            links.append("https://books.toscrape.com/catalogue/" + link)
        time.sleep(1)

print(len(links))

with open('urls.txt', 'w') as file:
    for link in links:
        file.write(link + '\n')
"""

with open('urls.txt', 'r') as infile:
    with open('books.csv', 'w', encoding="utf-8") as outfile:
        outfile.write('Nom,Prix,Description\n')  # entete de mon csv
        for row in infile:
            url = row.strip()  # enlever les retours à la ligne
            response = requests.get(url)
            if response.ok:
                soup = BeautifulSoup(response.text, "html.parser")
                name = soup.find(
                    'div', {'class': 'col-sm-6 product_main'}).find('h1')
                price = soup.find(
                    'div', {'class': 'col-sm-6 product_main'}).find('p', {'class': 'price_color'})
                # J'utilise une fonction lambda pour sélectionner le paragraphe sans attribut

                description = soup.find('article', {'class': 'product_page'}).find(
                    'p', attrs=lambda attr: not attr)
                if (description):
                    outfile.write(name.text + ',' + price.text +
                                  ',' + description.text.replace(',', '') + '\n')
                else:
                    description = ""
                # print("Nom: " + name.text + ", Prix: " +
                #      price.text + ", Description: " + description.text)
                    outfile.write(name.text + ',' + price.text +
                                  ',' + description + '\n')
            time.sleep(1)
