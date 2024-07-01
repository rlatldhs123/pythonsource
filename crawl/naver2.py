# requests, BeautifulSoup 모듈 import
import requests
from bs4 import BeautifulSoup

# HTTPError 예외 처리를 위해 urllib 모듈에서 HTTPError import
from urllib.error import HTTPError
from openpyxl import Workbook


wb = Workbook()  # 새 워크북 생성
ws = wb.active  # 현재 활성화된 sheet 가져옴

ws.title = "네이버 open"
# 너비 조정
ws.column_dimensions["B"].width = 100
ws.column_dimensions["c"].width = 60

ws.append(["순위", "상품명", "판매경로"])


# 네이버 API를 사용하기 위한 인증 정보 설정
headers = {
    "X-Naver-Client-Id": "Psi2M0ymsLbfP5xS8FRw",  # 클라이언트 ID
    "X-Naver-Client-Secret": "5HOvRjnQno",  # 클라이언트 시크릿
}

params = {"query": "아이폰", "display": "100"}


start = 1
num = 0

for idx in range(10):
    start_num = start + (
        idx * 100
    )  # 100개 검색하고 다음 페이지 검색 도 자동화 시켜버린다
    url = "https://openapi.naver.com/v1/search/shop.json"
    params = {"query": "아이폰", "display": "100", "start": str(start_num)}
    r = requests.get(url, params=params, headers=headers)
    print(r.url)

    # requests 모듈을 사용하여 API에 GET 요청을 보냄
    # params 매개변수를 사용하여 검색어를 전달

    # API 응답을 JSON 형식으로 파싱하여 변수에 저장
    data = r.json()

    for idx, item in enumerate(data["items"], 1):
        print(idx, item["title"], item["link"])
        ws.append([idx, item["title"], item["link"]])
        num += 1


# base_dir = "./crawl/file/"
# wb.save(base_dir + "naver.xlsx")
# wb.close()
