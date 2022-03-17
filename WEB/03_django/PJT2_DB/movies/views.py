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