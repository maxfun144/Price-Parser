import requests
from bs4 import BeautifulSoup

url = "https://www.smart-doors.su/catalog/korobki_i_porogi/korobki/3240/"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
soup1 = soup.findAll(class_="price")
for element in soup1:
    print(element.prettify())


print("Using 'find'.....")
soup2 = soup.find_all(class_="price discount")
print(soup2)
soup2 = soup.find(class_="values_wrapper")
print(soup2)