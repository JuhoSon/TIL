from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # 사용자가 index/로 요청을 보내면 views.py에 있는 index라는 이름의 함수를 호출 할겁니다!
    path('index/practice/', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('dtl-practice/', views.dtl_practice, name='dtl'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    # str은 기본값! (생략 가능)
    path('hello/<str:name>/<name2>/', views.hello, name='hello'),    
    path('food/<name>/<int:num>/', views.food, name='food'),
]
