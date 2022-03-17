import requests
from pprint import pprint


def recommendation(title):
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
    
    # 4. 추천영화 목록 조회
    title_li = []  # init
    for movie_id in movie_id_li:
        PATH = f'/movie/{movie_id}/recommendations'
        params = {
            'api_key' : '98cac53a564deda195214a5707cb4da4',
            'region' : 'KR',
            'language' : 'ko'
        }
        response = requests.get(BASE_URL+PATH, params=params).json()['results']
        
        if len(response) > 0:
            title_li += [dic['original_title'] for dic in response]

    return title_li


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록 구성.
    추천 영화가 없을 경우 [].
    영화 id검색에 실패할 경우 None.
    """
    pprint(recommendation('기생충'))
    # ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
    pprint(recommendation('그래비티'))
    # []  => 추천 영화 없음
    pprint(recommendation('검색할 수 없는 영화'))
    # => None
