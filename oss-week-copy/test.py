import requests
from secret import API_KEY

BASE_URL = ("https://www.kobis.or.kr/kobisopenapi/webservice/rest/"
        "boxoffice/searchDailyBoxOfficeList.json")

date = 20260824
title = "호프"

# KOBIS API에 보낼 쿼리: 인증키(key)와 조회 날짜(targetDt)
params = {"key" : API_KEY, "targetDt" : date}
# 일별 박스오피스 API를 호출한다 (최대 10초 대기)
response = requests.get(BASE_URL, params = params, timeout = 10)
# 응답 본문을 JSON(딕셔너리)으로 변환한다
data = response.json()
movies = data['boxOfficeResult']['dailyBoxOfficeList']

for movie in movies[:]:
    #print(movie['movieNm'])
    if movie['movieNm'] == title:
        print(movie['audiCnt'], movie['movieNm'])



