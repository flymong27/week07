import requests
import json
from secret import API_KEY  # API 인증키는 secret.py에서 가져온다

# KOBIS 일별 박스오피스 API 주소
url = ("https://www.kobis.or.kr/kobisopenapi/webservice/rest/"
        "boxoffice/searchDailyBoxOfficeList.json")
# 인증키와 조회 날짜(YYYYMMDD). 여기서는 2026년 8월 24일
params = {"key" : API_KEY, "targetDt": "20260824"}

# API를 호출한다 (최대 10초 대기)
response = requests.get(url, params= params, timeout = 10)

# 응답 본문을 JSON(딕셔너리)으로 변환한다
data = response.json()
# 박스오피스 결과 부분만 꺼낸다
result = data['boxOfficeResult']

# 그날의 일별 박스오피스 영화 목록
movies = result['dailyBoxOfficeList']
# 목록 첫 번째 = 1위 영화
first = movies[0]
print(first['rank'])      # 순위
print(first['movieNm'])   # 영화 제목
print(first['audiCnt'])   # 그날 관객 수




#추가 맛보기~
# 목록에 있는 모든 영화를 하나씩 출력한다

for movie in movies[:]:
    rank = movie['rank']              # 순위
    name = movie['movieNm']           # 영화 제목
    audi = int(movie['audiCnt'])      # 관객 수(문자열 → 정수)
    print(f"{rank}위 {name} {audi:,} 명")  # 예: 1위 오디세이 12,345 명
