import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

url = "https://finance.naver.com/"

userAgent = UserAgent()

headers = {"user-agent": userAgent.chrome}

with requests.Session() as s:
    r = s.get(url, headers=headers)
    # print(r.text)
    # print(r.status_code)

    soup = BeautifulSoup(r.text, "lxml")

    # 해외증시
    # container > div.aside > div > div.aside_area.aside_stock > table > tbody > tr:nth-child(1) > th > a
    global_stock = soup.select(
        "#container > div.aside > div > div.aside_area.aside_stock > table > tbody > tr th a"
    )
    # print(global_stock)
    for item in global_stock:
        print(item.get_text())

    print("=" * 5)

    # 인기검색
    stock = soup.select("div.aside_area.aside_popular > table > tbody > tr")
    # print(stock)
    for item in stock:
        # 회사명
        company_name = item.select_one("a").string
        # 현재금액
        current_amount = item.select_one("td").string

        print(company_name, current_amount)
