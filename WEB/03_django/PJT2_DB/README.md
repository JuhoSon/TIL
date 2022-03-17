# Project 03_반응형 웹 페이지 구성

## 1. 프로젝트 소개

- 진행 일시: 2022.03.11 (금)

- 프로젝트 내용 요약

    - 게시판 만들기

    

## 2. 해결 과정

### 1) urls

```python
# project urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    
]

# app urls.py
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/edit/', views.edit, name='edit'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
    
]

```



- parameter로 넘어가는 방식이 어렵다. 한번에 여러가지 일을하고 페이지를 띄우다보니 어디서 에러났는지 찾기가 너무 오래걸린다.



### 2) views.py

```python
from django.shortcuts import redirect, render
from .models import Movie


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)


def new(request):
    
    return render(request, 'movies/new.html')


def create(request):
    # get POST API
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')

    # add DB
    movie = Movie()
    movie.title = title
    movie.audience = audience
    movie.release_date = release_date
    movie.genre = genre
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    movie.save()

    return redirect('movies:detail', movie.pk)


def detail(request, movie_pk):
    # get movie from DB
    movie = Movie.objects.get(pk=movie_pk)
    # fill context
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)


def edit(request, movie_pk):
    # get movie from DB
    movie = Movie.objects.get(pk=movie_pk)
    # fill context
    context = {
        'movie': movie,
        'genre_list': ['comedy', 'jazz']
    }
    print(movie.release_date, type(movie.release_date))
    return render(request, 'movies/edit.html', context)


def update(request, movie_pk):
    # get movie from DB
    movie = Movie.objects.get(pk=movie_pk)

    # get new info from POST API
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')

    # update DB
    movie.title = title
    movie.audience = audience
    movie.release_date = release_date
    movie.genre = genre
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    movie.save()

    return redirect('movies:detail', movie.pk)


def delete(request, movie_pk):
    # delete from 
    if request.method == 'POST':
        article = Movie.objects.get(pk=movie_pk)
        article.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie_pk)
```

- 함수만 구현하면 되고, reutrn 할때 render, redirect만 주의하면 되서 비교적 간단한 파트. 적성에 맞는것같다.



### 3) templates

```html
{% extends 'base.html' %}

{% block body %}
  <h1>IDNEX</h1>
  <a href="{% url 'movies:new' %}">[NEW]</a>
  <hr>
  {% for movie in movies %}
    <a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a>
    <p>{{ movie.score }}</p>
    <hr>
  {% endfor %}
{% endblock body %}

{% extends 'base.html' %}

{% block body %}
  <h1>DETAIL</h1>
  <hr>
  <img src="{{ movie.poster_url }}" alt="movie_poster">
  <br>
  <p>{{ movie.title }}</p>
  <br>
  <p>Audience : {{ movie.audience }}</p>
  <br>
  <p>Release Dates : {{ movie.release_date }}</p>
  <br>
  <p>Genre : {{ movie.genre }}</p>
  <br>
  <p>Score : {{ movie.score }}</p>
  <br>
  <p>{{ movie.description }}</p>
  <br>
  
  <a href="{% url 'movies:edit' movie.pk %}">EDIT</a>
  <a href="#" onclick='document.getElementById("delete").submit();'>
    DELETE</a>

  <form id='delete' action="{% url 'movies:delete' movie.pk %}" method='POST' hidden>
    {% csrf_token %}
    <button>delete</button>
  </form>
  <br>


  <a href="{% url 'movies:index' %}">BACK</a>

{% endblock body %}



{% extends 'base.html' %}

{% block body %}
  <h1>EDIT</h1>
  <hr>

  <form action="{% url 'movies:update' movie.pk %}" method='POST'>
    {% csrf_token %}
    <label for="title">TITLE</label>
    <input type="text" id='title' name='title' value={{ movie.title }}>
    <br>
    <label for="audience">AUDIENCE</label>
    <input type="text" id='audience' name='audience' value={{ movie.audience }}>
    <br>
    <label for="release_date">RELEASE_DATE</label>
    <input type="date" id='release_date' name='release_date' value={{ movie.release_date|date:"Y-m-d" }}>
    <br>
    <label for="genre">GENRE</label>
    <select name="genre" id="genre" >
      {% for genre in genre_list %}
        {% if genre == movie.genre %}
          <option value={{ genre }} selected='selected'>{{ genre}}</option>
        {% else %}
          <option value={{ genre }}>{{ genre }}</option>
        {% endif %}
      {% endfor %}
    </select>
    <br>
    <label for="score">SCORE</label>
    <input type="text" id='score' name='score' value={{ movie.score }}>
    <br>
    <label for="poster_url">POSTER_URL</label>
    <input type="text" id='poster_url' name='poster_url' value={{ movie.poster_url }}>
    <br>
    <label for="description">DESCRIPTION</label>
    <textarea name="description" id="description" cols="30" rows="5">{{ movie.description }}</textarea>
    <br>
    <input type="reset" value='Reset'>
    <input type="submit" value='Submit'>
  </form>
  <hr>
  <a href="{% url 'movies:index' %}">BACK</a>
{% endblock body %}


{% extends 'base.html' %}

{% block body %}
  <h1>NEW</h1>
  <hr>
  <form action="{% url 'movies:create' %}" method='POST'>
    {% csrf_token %}
    <label for="title">TITLE</label>
    <input type="text" id='title' name='title'>
    <br>
    <label for="audience">AUDIENCE</label>
    <input type="text" id='audience' name='audience'>
    <br>
    <label for="release_date">RELEASE_DATE</label>
    <input type="date" id='release_date' name='release_date'>
    <br>
    <label for="genre">GENRE</label>
    <select name="genre" id="genre">
      <option value="comedy">comdey</option>
      <option value="jazz">jazz</option>
    </select>
    <br>
    <label for="score">SCORE</label>
    <input type="text" id='score' name='score'>
    <br>
    <label for="poster_url">POSTER_URL</label>
    <input type="text" id='poster_url' name='poster_url'>
    <br>
    <label for="description">DESCRIPTION</label>
    <textarea name="description" id="description" cols="30" rows="5"></textarea>
    <br>
    <button>Submit</button>
  </form>
  <hr>
  <a href="{% url 'movies:index' %}">BACK</a>
{% endblock body %}
```



- 순서대로 detail, edit, index, new인데 DTL이 생각보다 어렵다. 프론트엔드가 내가알던게 전부가 아니었다 .. 생각보다 장고템플릿으로 디테일하게 조정해야하고, 인터넷에 검색하면 장고로 된 글보다는 php 가 많아서 이것도  언어에따라 다르구나 싶다. 그리고 죄다 jquery, javascript 가 많아서 프론트의 세상은 넓고도 넓구나싶다.





## 3. 후기

💡프론트엔드도 생각보다 기교부릴 부분이 많다.

💡백엔드에서 어떻게 트래픽을 처리하는가가 제일 중요한점인거같은데 그런 과정도 좀 배울 수 있으면 너무 좋겠다.

🙂 잘한 점

1. 코드를 복붙하지않고 혼자 작성하다가 모르는부분을 참고하며 만드니 기억에 오래남는다.

🙁 아쉬운 점

1. 프론트엔드에 더이상 꾸미고싶은 흥미가 생기지 않는다.. 