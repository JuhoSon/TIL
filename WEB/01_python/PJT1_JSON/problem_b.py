import json
from pprint import pprint


def movie_info(movie, genres):
    # 여기에 코드를 작성합니다.
    need = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    result = {k:movie[k] for k in need}
    genre_dic = dict()
    for k in result['genre_ids']:
        for dic in genres:
            if dic['id'] == k:
                genre_dic[k] = dic['name']
    result['genre_names'] = [genre_dic[k] for k in result['genre_ids']]
    return result
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))