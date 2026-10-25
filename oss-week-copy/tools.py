import requests
from secret import API_KEY

BASE_URL = ("https://www.kobis.or.kr/kobisopenapi/webservice/rest/"
        "boxoffice/searchDailyBoxOfficeList.json")

def get_boxoffice_rank_1(date):
    """
    그 날짜의 박스오피스 1위 영화 제목을 알려준다. 
    받는것 : date (문자열) - 8자리 날짜. 예: "20261013"
    돌려주는것 : (문자열) 1위 영화 제목. 예: "오디세이"
    
    
    """
    # KOBIS API에 보낼 쿼리: 인증키(key)와 조회 날짜(targetDt)
    params = {"key" : API_KEY, "targetDt" : date}
    # 일별 박스오피스 API를 호출한다 (최대 10초 대기)
    response = requests.get(BASE_URL, params = params, timeout = 10)
    # 응답 본문을 JSON(딕셔너리)으로 변환한다
    data = response.json()
    # 그날의 일별 박스오피스 영화 목록을 꺼낸다
    movies = data['boxOfficeResult']['dailyBoxOfficeList']
    # 목록 첫 번째(1위) 영화의 제목을 반환한다
    return movies[0]['movieNm']

def get_movie_audience(date, title):
        # KOBIS API에 보낼 쿼리: 인증키(key)와 조회 날짜(targetDt)
        params = {"key" : API_KEY, "targetDt" : date}
        # 일별 박스오피스 API를 호출한다 (최대 10초 대기)
        response = requests.get(BASE_URL, params = params, timeout = 10)
        # 응답 본문을 JSON(딕셔너리)으로 변환한다
        data = response.json()
        movies = data['boxOfficeResult']['dailyBoxOfficeList']

        for movie in movies[:]:
                if movie['movieNm'] == title:
                        return "-> " + format(int(movie['audiCnt']), ",") + '명'
        return "그런건 없다!"


