import requests
from bs4 import BeautifulSoup
page = requests.get('https://www.seniortalktalk.com/maps')
soup = BeautifulSoup(page.content, 'html.parser')

a = soup.find_all('p', class_='p-title')
print(a)