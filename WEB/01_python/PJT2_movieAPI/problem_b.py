import requests
from pprint import pprint


def vote_average_movies():
    # 1. URL 및 요청변수 설정
    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = '/movie/popular'
    params = {
        'api_key' : '98cac53a564deda195214a5707cb4da4',
        'region' : 'KR',
        'language' : 'ko'
    }
    
    # 2. 요청 보낸 결과 저장
    response = requests.get(BASE_URL+PATH, params=params).json()

    # 3. 조작 ...
    result = []
    for m in response['results']:
        if m['vote_average'] >= 8:
            result.append(m)
    return result

if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    pprint(vote_average_movies())
    # => 영화정보 순서대로 출력