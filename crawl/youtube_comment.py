from selenium import webdriver  # Selenium 웹드라이버 모듈
from selenium.webdriver import ChromeOptions  # 크롬 옵션 설정 모듈
from selenium.webdriver.chrome.service import Service  # 크롬 서비스 관리 모듈
from webdriver_manager.chrome import ChromeDriverManager  # 크롬 드라이버 자동 설치 모듈
from selenium.webdriver.common.keys import Keys  # 키 입력 관리 모듈
from selenium.webdriver.common.by import By  # 요소 선택 모듈
import time  # 시간 관련 모듈
from urllib.request import urlretrieve  # URL을 통해 파일을 다운로드하는 모듈

from bs4 import BeautifulSoup

import pandas as pd


def main():
    # 크롬 드라이버를 설정하고 브라우저를 엽니다.
    browser = set_chrome_driver()

    browser.get("https://www.youtube.com/watch?v=CapWwymf620")

    time.sleep(10)

    # 스크롤 간격(초)을 설정합니다.
    interval = 5

    # 현재 문서의 높이를 가져옵니다.
    # 유튜브의 경우  이게 아니라
    # 해당 과 같이 잡아야 한다
    current_height = browser.execute_script(
        "return document.documentElement.scrollHeight"
    )

    # 페이지 끝까지 스크롤을 내립니다.
    while True:
        # 페이지를 맨 아래로 스크롤합니다.
        browser.execute_script(
            "window.scrollTo(0,document.documentElement.scrollHeight);"
        )
        # 스크롤 후 페이지 로드를 기다립니다.
        time.sleep(interval)

        # 새로운 문서 높이를 가져옵니다.
        new_height = browser.execute_script(
            "return document.documentElement.scrollHeight"
        )

        # 현재 높이와 새로운 높이가 같으면 반복을 멈춥니다.
        if new_height == current_height:
            break

        # 현재 높이를 업데이트합니다.
        current_height = new_height

    # 스크롤을 페이지 맨 위로 올립니다.
    browser.execute_script("window.scrollTo(0,0);")

    time.sleep(3)

    # 전체 소스를 BeatifulSoup 담기

    page_source = browser.page_source

    soup = BeautifulSoup(page_source, "lxml")

    # 댓글 사용자의 아이디 및 코멘트 가져오기

    time.sleep(4)

    ids = soup.select("#author-text > span")
    comments = soup.select("#content-text > span")

    ids_list = []
    comments_list = []

    print(len(ids))
    print(len(ids))
    print(len(ids))
    print(len(ids))
    print(len(ids))
    print(len(ids))

    for idx in range(len(ids)):
        print(ids[idx].text.strip(), comments[idx].text.strip())

        clean_id = ids[idx].text.strip()
        clean_id = clean_id.replace("\n", " ")
        clean_id = clean_id.replace("\t", " ")
        ids_list.append(clean_id)

        clean_comment = comments[idx].text.strip()
        clean_comment = clean_comment.replace("\n", " ")
        clean_comment = clean_comment.replace("\t", " ")
        comments_list.append(clean_comment)

    #  확인

    # 데이터 프레임 생성

    dict_data = {"Id": ids_list, "Comments": comments_list}

    df = pd.DataFrame(dict_data)

    df.to_csv("./crawl/file/youtube.csv", index=False, encoding="utf-8-sig")


def set_chrome_driver():
    # 크롬 옵션을 설정합니다.
    options = ChromeOptions()
    # options.add_argument("--start-maximized")  # 브라우저를 최대화 모드로 엽니다.

    # 크롬 드라이버를 생성합니다.
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    return driver  # 설정된 드라이버를 반환합니다.


# 이 파일이 직접 실행되었을 때만 main() 함수를 실행합니다.
if __name__ == "__main__":
    main()
