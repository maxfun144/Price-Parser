import requests
from bs4 import BeautifulSoup
import re

# url = "http://www.adv-trade.ru/produkciya/mezhkomnatnye_dveri/dveri_gladkie/gladkaya_dver_ef400_28db_belaya/"

# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def get_total_pages(html):
#     soup = BeautifulSoup(html, "lxml")
#     # soup.find("span", {"class":"price-box"})
#     soup.find("div")
#
#     print(soup)
#     print(soup.text)


# page = requests.get(url)
# # html = get_html(url)
# soup = BeautifulSoup(page.content, "html.parser")
# # soup = soup.find("span", {"class":"price-box"})
# # soup = soup.find(class_="price")
# soup = soup.find(class_="price").text
#
# price = re.findall(r"[0-9 ]+", soup)[0].strip()
#
# print()
# print(price)
# print(soup.text)

# Сайт АДВ
# def getPrice(url):
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, "html.parser")
#     soup = soup.find(class_="price").text
#
#     price = re.findall(r"[0-9 ]+", soup)[0].strip()
#
#     return price


# urlList = []
# url = "http://www.adv-trade.ru/produkciya/mezhkomnatnye_dveri/dveri_gladkie/gladkaya_dver_ef400_28db_belaya/"
# url1 = "http://www.adv-trade.ru/produkciya/mezhkomnatnye_dveri/dveri_gladkie/2-h_stvorchataya_gladkaya_dver_pro_pari_belaya1/"
# url2 = "http://www.adv-trade.ru/produkciya/mezhkomnatnye_dveri/dveri_gladkie/framuga1/"
# url3 = "http://www.adv-trade.ru/produkciya/mezhkomnatnye_dveri/dveri_gladkie/2-h_stvorchataya_gladkaya_dver_prol1pari_belaya1/"
# url4 = "http://www.adv-trade.ru/produkciya/mezhkomnatnye_dveri/dveri_gladkie/korobka_belaya_ft-65_m7-10h24/"
# url5 = "http://www.adv-trade.ru/produkciya/mezhkomnatnye_dveri/dveri_gladkie/korobka_s_uplotnitelem_pod_magnitzamok_belaya_m7-10x25/"
#
# newUrl = "http://www.adv-trade.ru/produkciya/mezhkomnatnye_dveri/dveri_spa/dver_unique_spa_500/"
# newUrl1 = "http://www.adv-trade.ru/produkciya/dekorativnye_elementy_listatalo/dekorativnyj_element_75h75h25_mmbelyj/"
#
# urlList.append(url)
# urlList.append(url1)
# urlList.append(url2)
# urlList.append(url3)
# urlList.append(url4)
# urlList.append(url5)
# urlList.append(newUrl)
# urlList.append(newUrl1)


# for url in urlList:
#     print(getPrice(url))


# ******************
# Сканди Строй
def getPrice(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    soup = soup.find(class_="j-product__price__current price").text
    # soup = soup.find(itemprop="price").text

    price = re.findall(r"[0-9 ]+", soup)[0].strip()

    return price


# print(getPrice("https://finskie-dveri.ru/finskaya-vhodnaya-dver-jeld-wen-f2000"))
# print(getPrice("https://finskie-dveri.ru/zamok-abloy-4292-dlya-protivopojarnyh-dverey"))
#



# Сканди Строй
# def getPrice(url, keyword):
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, "html.parser")
#     # soup = soup.find(class_="j-product__price__current").text
#     soup = soup.find(class_=keyword.split("=")[-1]).text
#
#     price = re.findall(r"[0-9 ]+", soup)[0].strip()
#
#     return price
#
#
# # for i in range(100):
# #     print(getPrice("https://findveri.ru/razdvizhnaya-dver-model-505.html"))
# #     print(getPrice("https://findveri.ru/639.html"))
#
#
# url10 = "https://finskie-dveri.ru/dver-v-parnuyu-s-kvadratnym-steklom"
# keyword = 'j-product__price__current price'
#
# print(getPrice(url10, keyword))


# url = "https://www.smart-doors.su/catalog/mezhkomnatnye_dveri/tradition_clever_line/1851/?oid=4353"
# urlTest = "https://www.smart-doors.su/catalog/korobki_i_porogi/korobki/3240/"
# proxies = {
#     "https": "http://5.252.179.8"
# }
# page = requests.get(urlTest)
# print(BeautifulSoup(page.content, "html.parser").prettify())
# print("Status: " + str(page.status_code))
# soup = BeautifulSoup(page.content, "html.parser")
# # print(soup.prettify())
# soup = soup.findAll(class_="price_value")#, class_="price_value")
# print(soup)
# # for elem in soup:
# #     print(elem.findAll(class_="price_value"))
# print("\nPrice = " + soup[0].text.strip())


url = "https://finskie-dveri.ru/filenchataya-dver-s-pritvorom-n254"
print(getPrice(url))