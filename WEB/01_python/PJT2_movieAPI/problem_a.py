# 0. import
import requests


def popular_count():
    # 1. URL 및 요청변수 설정
    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = '/movie/popular'
    params = {
        'api_key' : '98cac53a564deda195214a5707cb4da4',
        'region' : 'KR',
        'language' : 'ko'
    }
    
    # 2. 요청 보낸 결과 저장
    response = requests.get(BASE_URL+PATH, params=params)

    # 3. 조작 ...
    return len(response.json()['results'])


if __name__ == '__main__':
    """
    popular 영화목록의 개수 출력.
    """
    print(popular_count())
    # => 20
