import requests 
import bs4

URL = input("Enter the url (ex: https://google.com/)   : ")

response = requests.get(URL)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
links = soup.select('a')
for link in links:
  if link.get('href') != None:
    if 'https://' in link.get('href'):
      print(link.get('href'))
