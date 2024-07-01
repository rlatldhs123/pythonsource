from selenium import webdriver  # Selenium 웹드라이버 모듈
from selenium.webdriver import ChromeOptions  # 크롬 옵션 설정 모듈
from selenium.webdriver.chrome.service import Service  # 크롬 서비스 관리 모듈
from webdriver_manager.chrome import ChromeDriverManager  # 크롬 드라이버 자동 설치 모듈
from selenium.webdriver.common.keys import Keys  # 키 입력 관리 모듈
from selenium.webdriver.common.by import By  # 요소 선택 모듈
import time  # 시간 관련 모듈
from urllib.request import urlretrieve  # URL을 통해 파일을 다운로드하는 모듈


def main():
    # 크롬 드라이버를 설정하고 브라우저를 엽니다.
    browser = set_chrome_driver()

    # 네이버 홈페이지를 엽니다.
    browser.get("http://www.naver.com")

    # 검색창을 찾습니다.
    search_box = browser.find_element(By.ID, "query")
    # 검색어 '아이스크림'을 입력합니다.
    search_box.send_keys("시장상품")
    # 엔터 키를 눌러 검색을 실행합니다.
    search_box.send_keys(Keys.ENTER)

    # 검색 결과 페이지가 로드될 시간을 기다립니다.
    time.sleep(2)

    # 이미지 탭을 찾습니다.
    image_tab = browser.find_element(
        By.CSS_SELECTOR,
        "div.api_flicking_wrap > div > a",
    )
    # 이미지 탭을 클릭합니다.
    image_tab.click()

    # 이미지 탭이 로드될 시간을 기다립니다.
    time.sleep(5)

    # 스크롤 간격(초)을 설정합니다.
    interval = 3

    # 현재 문서의 높이를 가져옵니다.
    current_height = browser.execute_script("return document.body.scrollHeight")

    # 페이지 끝까지 스크롤을 내립니다.
    while True:
        # 페이지를 맨 아래로 스크롤합니다.
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        # 스크롤 후 페이지 로드를 기다립니다.
        time.sleep(interval)

        # 새로운 문서 높이를 가져옵니다.
        new_height = browser.execute_script("return document.body.scrollHeight")

        # 현재 높이와 새로운 높이가 같으면 반복을 멈춥니다.
        if new_height == current_height:
            break

        # 현재 높이를 업데이트합니다.
        current_height = new_height

    # 스크롤을 페이지 맨 위로 올립니다.
    browser.execute_script("window.scrollTo(0,0);")

    # 이미지가 로드될 시간을 기다립니다.
    time.sleep(3)

    # 썸네일 이미지들을 찾습니다.
    images = browser.find_elements(By.CSS_SELECTOR, ".thumb img")

    # 이미지 다운로드를 위한 카운터 초기화
    count = 1
    # 각 썸네일 이미지를 클릭하여 큰 이미지를 엽니다.
    for img in images:
        try:
            img.click()
            time.sleep(2)

            # 큰 이미지의 URL을 가져옵니다.
            img_url = browser.find_element(
                By.CSS_SELECTOR, "div.viewer_image img"
            ).get_attribute("src")
            print(img_url)

            # URL을 통해 이미지를 다운로드합니다. 다운로드 경로와 파일명 지정.
            urlretrieve(img_url, "./crawl/download/" + str(count) + ".jpg")
            count += 1
        except:
            # 이미지 다운로드 실패 시, 예외 처리
            pass

    # 모든 작업이 끝난 후 5초 대기합니다.
    time.sleep(5)


def set_chrome_driver():
    # 크롬 옵션을 설정합니다.
    options = ChromeOptions()
    options.add_argument("--start-maximized")  # 브라우저를 최대화 모드로 엽니다.

    # 크롬 드라이버를 생성합니다.
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    return driver  # 설정된 드라이버를 반환합니다.


# 이 파일이 직접 실행되었을 때만 main() 함수를 실행합니다.
if __name__ == "__main__":
    main()
