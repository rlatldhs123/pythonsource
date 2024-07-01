# 크롤링

# requests : 해당 패키지는 웹서버로 요청시 사용

import requests

urls = ["https://www.naver.com/", "https://www.python.org/"]

file_name = "robots.txt"

for url in urls:
    robots = requests.get(url=file_name)
    print(robots.text)
