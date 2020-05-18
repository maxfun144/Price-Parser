import requests
from bs4 import BeautifulSoup

# url2 = "https://finskie-dveri.ru/dvustvorchatye-dveri-mejkomnatnye-alavus-250-6lr-pari"
# # 'class="price"+class="values_wrapper""'
# page2 = requests.get(url2)
# soup2 = BeautifulSoup(page2.content, "html.parser")
# # print(soup.prettify())
# soup2 = soup2.find(class_="j-product__price__current price")
# print("=========================")
# print(soup2.prettify())
# print("=========================")
#
# print(soup2.text)



url = "https://findveri.ru/mezhkomnatnaya-dver-model-vd201.html"
# 'class="price"+class="values_wrapper""'
content = requests.get(url).content
# content = open("site.html", "r").read()
soup1 = BeautifulSoup(content, "html.parser")
soup2 = BeautifulSoup(content, "html.parser")

soup1 = soup1.find_all(lambda tag: (tag.get('id') == 'sv-prod-price' or tag.get('id') == 'sv-prod-price'.split() and tag.text.strip() != ""))
# soup2 = soup2.find_all(id="sv-prod-price")
# for el in soup2:
#     print("el id: ", el.get('id'))
#     print("Type of id: ", type(el.get('id')))
print(soup1[0].text)
# print(soup2)
# soup1 = soup1.find_all(class_="price discount")
# print("Len(soup) = ", len(soup1))
# for e in soup1:
#     print(e.get("class"))
#
# soup2 = soup2.find_all(lambda tag: tag.get('class') == ["price", "discount"] and tag.text.strip() != "")
# # soup = soup(lambda x: x.text.strip() != "")
# print("New len(soup) = ", len(soup2))
# for sp in soup2:
#     print("Price discount text = " + sp.text.strip())
# print(soup.prettify())
# print("Soup find" + str((soup.find(class_="Bugaga") is None)))
# soup = soup.find_all(lambda tag: tag.get('class') == ["price"])
# for sp in soup:
#     if sp.find(class_="values_wrapper").text is not '':
#         soup = sp.find(class_="values_wrapper").text
#         break
# print("=========================")
# print(soup)
# print("=========================")

# print(soup.text)
# print(soup.find(class_="price").find(class_="values_wrapper").text)
