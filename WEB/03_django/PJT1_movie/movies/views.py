from django.shortcuts import render
import requests
import random

# Create your views here.
def index(request):
    return render(request, 'movies/index.html')


def get_recom(title):
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
        movie_id_li.append(dic.get('id', None))  # 쇼생크탈출 영화 번호
    
    # 4. 추천영화 목록 조회
    movie_li = []  # init
    for movie_id in movie_id_li:
        PATH = f'/movie/{movie_id}/recommendations'
        params = {
            'api_key' : '98cac53a564deda195214a5707cb4da4',
            'region' : 'KR',
            'language' : 'ko'
        }
        response = requests.get(BASE_URL+PATH, params=params).json()['results']
        
        if len(response) > 0:
            movie_li += response

    # 5. 랜덤 선택
    seed = random.randint(0, len(movie_li)-1)
    movie = movie_li[seed]

    # 6. 영화 조회
    movie_id = movie['id']
    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = f'/movie/{movie_id}'
    params = {
        'api_key' : '98cac53a564deda195214a5707cb4da4',
        'region' : 'KR',
        'language' : 'ko',
        'query' : movie_id
    }
    response = requests.get(BASE_URL+PATH, params=params).json()
    
    return response


def recommendations(request):
    recom_movie_info = get_recom('쇼생크 탈출')
    movie_id = recom_movie_info['id']
    poster = 'https://image.tmdb.org/t/p/w500' + recom_movie_info['poster_path']
    title = recom_movie_info['original_title']
    content = recom_movie_info['overview']
    release_date = recom_movie_info['release_date']
    vote_average = recom_movie_info['vote_average']
    detail = 'https://www.themoviedb.org/movie/' + str(movie_id)
    print(poster)

    context = {
        'img': poster,
        'title': title,
        'vote_average': vote_average,
        'content': content,
        'release_date': release_date,
        'detail': detail,
    }

    return render(request, "movies/recommendations.html", context)