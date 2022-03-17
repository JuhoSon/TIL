from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # index: articles/
    path('', views.index, name='index'),

    # new: articles/new/ -> throw
    path('new/', views.new, name='new'),
    # create: articles/create/ -> catch
    path('create/', views.create, name='create'),
    
    # detail: articles/2/ & articles/3/ & articles/4/....
    path('<int:article_pk>/', views.detail, name='detail'),

    # delete: articles/2/delete/ & articles/3/delete/
    path('<int:article_pk>/delete/', views.delete, name='delete'),

    # edit: articles/2/edit/ -> throw
    path('<int:article_pk>/edit/', views.edit, name='edit'),
    # update: articles/2/update/ -> catch
    path('<int:article_pk>/update/', views.update, name='update'),
]