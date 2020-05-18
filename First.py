import requests
import re
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

# resp = urlopen('https://stepik.org/media/attachments/lesson/245130/6.html') # скачиваем файл
# html = resp.read().decode('utf8') # считываем содержимое
# soup = BeautifulSoup(html, 'html.parser') # делаем суп
# table = soup.find('table', attrs = {'class' : 'wikitable sortable'})
# cnt = 0
# for tr in soup.find_all('tr'):
#     cnt += 1
#     for td in tr.find_all(['td', 'th']):
#         cnt *= 2
# print(cnt)

page = requests.get("https://stepik.org/media/attachments/lesson/209723/5.html")
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
lst = list(soup.children)
# print(lst[0])
# print(type(lst[0]))
# print(str(lst[0]))
string = " ".join([str(el) for el in soup.children])
# print(string)
result = re.findall(r"[0-9]+", string)
# result = re.findall(r'\d+', string)
print(sum(map(int, result)))
# print(soup.prettify())

# print(soup.find_all("tr"))
data = []
sum = 0
rows = soup.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    for elem in cols:
        sum += int(elem.text)
    # cols = [ele.text.strip() for ele in cols]
    # data.append([ele for ele in cols if ele])

print(sum)

