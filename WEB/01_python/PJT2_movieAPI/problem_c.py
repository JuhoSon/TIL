import requests
from pprint import pprint


def ranking():
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
    result = sorted(response['results'], 
                    key=lambda arr: arr['vote_average'],
                    reverse=True)[:5]
    return result


if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화.
    """
    pprint(ranking())
    # => 영화정보 순서대로 출력
