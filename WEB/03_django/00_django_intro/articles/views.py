from unittest import result
from django.shortcuts import render

def index(request):
    # request -> 요청과 관련된 다양한 정보가 들어가 있는 객체구나! (HttpRequest라는 클래스의 인스턴스)
    # print(dir(request))
    # print(request.user)
    context = {
        'name': 'JUSTIN',
        'hobby': 'pizza',
    }
    # template을 찾는 기본 원칙 
    # - app 밑에 있는 'templates'라는 이름의 폴더 내부에서 .html 파일을 찾아 렌더링한다.
    # - 하지만 app이 여러 개 있는 경우는 위에서부터 .html 파일을 찾아가기 때문에 동일한 이름이라면
    # settings.py INSTALLED_APPS에 등록된 선순위 앱의 .html 파일을 먼저 읽어오게 된다.
    # - 그렇기 때문에 각 앱 이름으로 templates 내부를 한번 더 래핑한다. 
    # ex 1) articles -> templates/articles/index.html
    # ex 2) pages -> templates/pages/index.html

    # -> render 함수의 두번째 인자를 부를 때 articles/index.html or pages/index.html 처럼 불러야 한다!
    # 왜? 그냥 부르면 기본값은 app 아래 있는 templates에서 해당하는 파일의 이름을 찾기 때문이다!

    return render(request, 'articles/index.html', context)

def detail(request):
    return render(request, 'articles/detail.html')

def dtl_practice(request):
    foods = ['짜장면', '탕수육', '짬뽕', '양장피']
    fruits = ['apple', 'banana', 'cucumber', 'mango']
    user_list = []
    context = {
        'foods': foods,
        'fruits': fruits,
        'user_list': user_list,
    }
    return render(request, 'articles/dtl_practice.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    # print(dir(request))
    print(request.GET.get('ball'))
    result = request.GET.get('ball')
    context = {
        'result': result,
    }
    return render(request, 'articles/catch.html', context)

def hello(request, name, name2):
    print(name)
    print(name2)

def food(request, name, num):
    print(type(num))
    context = {
        'food': name,
        'num': num,
    }
    return render(request, 'articles/food.html', context)