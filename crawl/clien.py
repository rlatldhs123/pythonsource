import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from xlsx_write import write_excel_template
from datetime import datetime


# https://www.clien.net/service/board/lecture?&od=T31&category=0&po=0
# https://www.clien.net/service/board/lecture?&od=T31&category=0&po=1
# https://www.clien.net/service/board/lecture?&od=T31&category=0&po=2
# https://www.clien.net/service/board/lecture?&od=T31&category=0&po=3
# https://www.clien.net/service/board/lecture?&od=T31&category=0&po=4


userAgent = UserAgent()

headers = {"user-agent": userAgent.chrome}

# 데이터 담을 리스트 생성
# lists = []
lists = list()


with requests.Session() as s:

    for page in range(5):
        url = "https://www.clien.net/service/board/lecture?&od=T31&category=0&po="
        url = url + str(page)
        r = s.get(url, headers=headers)
        # print(r.text)
        # print(r.status_code)

        soup = BeautifulSoup(r.text, "lxml")
        # print(soup)

        # 행 가져오기
        rows = soup.select("div.list_content > div.list_item.symph_row")

        for row in rows:

            title = row.select_one("div.list_title > a > span.subject_fixed")
            time = row.select_one("div.list_time > span > span")

            # 2024-04-27 07:22:02 ==> 2024-04-27
            print(title.text.strip(), time.text.strip()[:10])
            lists.append([title.text.strip(), time.text.strip()[:10]])

        print()

    # 파일 저장 : clien_240527.xlsx
    # 오늘날짜
    today = datetime.now().strftime("%Y%m%d")

    write_excel_template(f"clien_{today}.xlsx", "팁과강좌", lists)
