import requests
from pprint import pprint


def credits(title):
    # 1. URL 및 요청변수 설정
    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = '/search/movie'
    params = {
        'api_key' : '98cac53a564deda195214a5707cb4da4',
        'region' : 'KR',
        'language' : 'ko',
        'query' : title
    }

    # 2. 요청 보낸 결과 저장
    response = requests.get(BASE_URL+PATH, params=params).json()['results']
    # 3. 조작 ...
    movie_id_li = []
    if len(response) == 0:
        return None
    for dic in response:
        movie_id_li.append(dic.get('id', None))
    
    # 4. 크레딧 조회
    credits_dic = dict()  # init
    cast_li = []
    crew_li = []
    for movie_id in movie_id_li:
        PATH = f'/movie/{movie_id}/credits'
        params = {
            'api_key' : '98cac53a564deda195214a5707cb4da4',
            'region' : 'KR',
            'language' : 'ko'
        }
        cast_response = requests.get(BASE_URL+PATH, params=params).json()['cast']
        crew_response = requests.get(BASE_URL+PATH, params=params).json()['crew']
        
        for cas in cast_response:
            if cas['cast_id'] < 10:
                cast_li.append(cas['original_name'])
        
        for cre in crew_response:
            if cre['known_for_department'] == 'Directing':
                crew_li.append(cre['original_name'])

    return {'cast':cast_li, 'crew':crew_li}


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록(cast)과 제작진(crew).
    영화 id검색에 실패할 경우 None.
    """
    pprint(credits('기생충'))
    # => {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # => None
