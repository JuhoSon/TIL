# Project 02_Python을 활용한 데이터 수집

## 1. 프로젝트 소개

- 진행 일시: 2022.01.28 (금)

- 프로젝트 내용 요약
  - 영화 커뮤니티 서비스 개발을 위한 데이터 수집 단계의 프로젝트이다.
  - python을 활용하여 dictionary, list 등 다양한 구조의 정보에서 원하는 정보를 추출해야 한다.

  

## 2. 해결 과정

### 1) problem_a

```python
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

```



- 라이브강의와 비슷해서 풀 수 있었다.



### 2) problem_b

```python
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
```

- 라이브강의와 비슷해서 풀 수 있었다.



### 3) problem_c

```python
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

```

- problem_b 를 해결하면 쉽게 풀 수 있는 문제였다.



### 4) problem_d

```python
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

```

- 같은 영화라도 id가 여러개일 수 있어서 어려웠다. 예를들어 어벤저스라면 여러개의 어벤저스가 있으므로 movie_id_li를 만들어서 루프로 구성하는게 포인트였다. 백엔드엔지니어가 된거같아서 기분이좋다.



### problem_e

```python
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

```

* d를 풀었다면 쉽게풀수있는 문제였다.



## 3. 후기

💡 라이브로 배울때와 코딩할때는 또 사뭇다르더라. 쉽네쉽네하며 넘긴것도 직접 코딩하려니 머리가 새햐얘져서 다시 라이브강의를 켰다. 역시손이 기억해야하나보다.

💡 프로젝트를 하며 깨달은 점

1. 백엔드들은 json, xml 등의 파일로 로그 관리하고 고객정보 관리하던데 발을 들인거같아서 기분이 좋다. 거기서부터 전처리의 시작이고 해당 데이터 정리 후 모델개발 및 배포하는것이 나의 꿈인데 한발짝 다가간것같아서 기분이좋다.

🙂 잘한 점

1. 복습잘했다.

🙁 아쉬운 점

1. 코드가 다소 더러운것같다. 시중에 refactoring, clean code 등의 책이 있던데 다 엄청두꺼워서 … 우선순위에는 밀려있다. 그거얼른 읽고싶게만드는 순간이었다.