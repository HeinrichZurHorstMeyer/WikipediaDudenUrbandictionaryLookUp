import urllib3
import html.parser
from bs4 import BeautifulSoup

Wort = input('Nach welchem Wort suchen Sie? \n').replace(' ', '%20')

#DUDEN

URL = 'https://www.duden.de/rechtschreibung/' + Wort
print('\nQuelle: ',URL, '\n')

http = urllib3.PoolManager()
r = http.request('GET', URL)

if (r.status != 200):
    print('Der gesuchte Begriff konnte nicht gefunden werden.')

soup = BeautifulSoup(r.data, "html5lib")
soup_found = soup.find('div', class_="enumeration__text")

if (soup_found == None):
    soup_found = soup.find('ol', class_="enumeration__text")

if (soup_found == None):
    soup_found = 'Das gesuchte Wort existiert vermutlich nicht.'

try:
    while True:
        print(soup.find('div', class_="enumeration__text").extract().get_text())
except:
    pass

#WIKIPEDIA

URL = 'https://de.wikipedia.org/wiki/' + Wort
print('\nQuelle: ',URL, '\n')

http = urllib3.PoolManager()
r = http.request('GET', URL)

if (r.status != 200):
    print('Es gab ein Problem.')
    print('Fehlercode: ', r.status)

soup = BeautifulSoup(r.data, "html5lib")
print(soup.find('p').get_text())

#URBAN DICTIONARY

URL = 'https://www.urbandictionary.com/define.php?term=' + Wort

print('\nQuelle: ',URL, '\n')

http = urllib3.PoolManager()
r = http.request('GET', URL)

if (r.status != 200):
    print('Es gab ein Problem.')
    print('Fehlercode: ', r.status)

soup = BeautifulSoup(r.data, "html5lib")
try:
    print(soup.find('div', class_="meaning").get_text())
except:
    if (r.status == 404):
        print('Der Begriff konnte nicht gefunden werden.')
    else:
        print('Es gab ein unbekanntes Problem.')

input('\nDrücken Sie Enter um das Programm zu beenden.\n')
