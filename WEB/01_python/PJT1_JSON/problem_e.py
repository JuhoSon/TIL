import json


def dec_movies(movies):
    # 여기에 코드를 작성합니다.  
    dec_idx = []    
    for idx, m in enumerate(movies):
        detail_info = json.load(open('data/movies/'+str(m['id'])+'.json', encoding='UTF8'))
        if detail_info['release_date'].split('-')[1] == '12':
            dec_idx.append(idx)
    return [movies[i]['title'] for i in dec_idx]
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))