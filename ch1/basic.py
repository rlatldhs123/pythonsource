# 모듈

# 함수, 변수 , 클래스를 모아 놓은 파이선 파일


# 파이썬에서 제공하는 기본 모듈

# import math

# print(math.ceil(3.14))
# print(math.sin(1))
# print(math.cos(1))
# print(math.floor(3.14))


# import random

# print(random.random())
# print(random.randrange(1, 10))  # 1 10 범위
# print(random.randrange(10))  # 0~ 19
# print(random.choice([1, 2, 3, 4, 5, 6]))  # 리스트 내부의 요소중 임의 선택
# print(random.shuffle([1, 2, 3, 4, 5, 6]))  # 그냥 섞는거
# print(random.sample([1, 2, 3, 4, 5, 6], k=2))  # 리스트 내부의 요소중  k 개 추출

# print()

# import time

# print("지금부터 5초 정지")
# time.sleep(5)
# print("프로그램 종료")


# import datetime


# # 현재 날짜와 시간 객체 생성
# now = datetime.datetime.now()

# # 년, 월, 일, 시, 분, 초 출력
# print(f"년: {now.year}")
# print(f"월: {now.month}")
# print(f"일: {now.day}")
# print(f"시: {now.hour}")
# print(f"분: {now.minute}")
# print(f"초: {now.second}")

# 모듈 import
# import 모듈명
# from 모듈명 import 사용할 것만
# from math import sin, cos, floor, ceil



# print(f"ceil(3.14): {ceil(3.14)}")
# print(f"sin(1): {sin(1)}")
# print(f"cos(1): {cos(1)}")
# print(f"floor(3.14): {floor(3.14)}")

# as 로 별명 부여 가능
import math as m

