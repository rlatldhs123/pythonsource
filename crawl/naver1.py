# requests, BeautifulSoup 모듈 import
import requests
from bs4 import BeautifulSoup

# HTTPError 예외 처리를 위해 urllib 모듈에서 HTTPError import
from urllib.error import HTTPError

# 네이버 블로그 검색 API URL
url = "https://openapi.naver.com/v1/search/blog.json"

# 네이버 API를 사용하기 위한 인증 정보 설정
headers = {
    "X-Naver-Client-Id": "Psi2M0ymsLbfP5xS8FRw",  # 클라이언트 ID
    "X-Naver-Client-Secret": "5HOvRjnQno",  # 클라이언트 시크릿
}

# requests 모듈을 사용하여 API에 GET 요청을 보냄
# params 매개변수를 사용하여 검색어를 전달
r = requests.get(
    url, headers=headers, params={"query": "파이선"}, display=100, sort="date"
)

# API 응답을 JSON 형식으로 파싱하여 변수에 저장
data = r.json()

# 검색된 블로그 게시글 항목을 출력
# enumerate 함수를 사용하여 각 항목의 인덱스와 함께 순회
for idx, item in enumerate(data["items"], 1):
    # 인덱스, 제목, 링크를 출력
    print(idx, item["title"], item["link"])


base_dir = "./crawl/file/"
wb.save(base_dir + "naver.xlsx")
wb.close()
