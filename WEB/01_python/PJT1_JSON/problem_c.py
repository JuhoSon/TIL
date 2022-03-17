import json
from pprint import pprint


def movie_info(movies, genres):
    # 여기에 코드를 작성합니다.
    movie_info = []
    for m in movies:
        need = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
        result = {k:m[k] for k in need}
        genre_dic = dict()
        for k in result['genre_ids']:
            for dic in genres:
                if dic['id'] == k:
                    genre_dic[k] = dic['name']
        result['genre_names'] = [genre_dic[k] for k in result['genre_ids']]
        
        movie_info.append(result)
    return movie_info
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))