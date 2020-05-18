import requests
import re
from bs4 import BeautifulSoup


def getPrice(url: str, keywords: list):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    # args = []
    # args = list(map(lambda x: re.findall(r"[^\'\"]+", x)[0], keywords[0].split("=")))
    # soup = soup.find_all(lambda tag: tag.get('class') == [args[1]])
    s = ""
    print(recursive(soup, keywords, s))


    return re.findall(r"[\d ]+", soup.text)[0].replace(" ", "")


def recursive(soup, keywords, s):
    args = list(map(lambda x: re.findall(r"[^\'\"]+", x)[0], keywords[0].split("=")))
    soup = soup.find_all(lambda tag: tag.get('class') == [args[1]])
    print(soup)
    if len(soup) == 0: return ""

    if len(keywords) == 1:
        c = ""
        for element in soup:
            c += element.text
        return c

    else:
        for element in soup:
            return s + recursive(element, keywords[1:], s)




url = "https://www.smart-doors.su/catalog/mezhkomnatnye_dveri/tradition_clever_line/2494/"
keywords = ['class=prices_block"', 'class="price discount"', 'class="values_wrapper"']
getPrice(url, keywords)










        #     if args[0] == "class":
#         soup = soup.find(lambda tag: tag.get('class') == [args[1]])
#     elif args[0] == "id":
#         soup = soup.find(lambda tag: tag.get('id') == [args[1]])
#     elif args[0] == "itemprop":
#         soup = soup.find(lambda tag: tag.get('itemprop') == [args[1]])
#     else:
#         soup = None