import json


def max_revenue(movies):
    # 여기에 코드를 작성합니다.  
    max_idx = -9999  # init
    rev = -9999
    for idx, m in enumerate(movies):
        detail_info = json.load(open('data/movies/'+str(m['id'])+'.json', encoding='UTF8'))
        if detail_info['revenue'] > rev:
            rev = detail_info['revenue']
            max_idx = idx
    return movies[max_idx]['title']
        
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))