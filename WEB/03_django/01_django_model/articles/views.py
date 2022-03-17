from django.shortcuts import render, redirect
from .models import Article

def index(request):
    # 사용자가 작성한 모든 게시글을 보여주는 페이지
    #1. DB로부터 모든 게시글을 조회하자
    # https://docs.djangoproject.com/en/4.0/ref/models/querysets/#all

    # Python 문법 -> QuerySet
    # DB에서 오름차순으로 불러오고 -> 파이썬으로 내림차순으로 정렬
    # articles = Article.objects.all()[::-1]

    # DB에 요청 할 때부터 내림차순으로 요청
    articles = Article.objects.order_by('-pk')

    # 게시글 확인 방법 2가지
    # 첫 번째 -> print(article)
    # print(articles)
    # 두 번째 -> SQLite extension을 활용하자! 
    
    #2. context에 담자 (왼쪽이 index.html에서 사용 할 변수 이름)
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    # 사용자가 게시글을 입력할 수 있는 폼을 제공
    return render(request, 'articles/new.html')

def create(request):
    #1. html로부터 날라온 데이터를 받아
    # print(request.POST)
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    #2. DB에 저장한다.
    #2-1. 첫 번째 방법
    # article = Article()
    # article.title = title # 23번째 줄이 오른쪽
    # article.content = content # 24번째 줄이 오른쪽
    # article.save()
    
    #2-2. 두 번째 방법
    article = Article(title=title, content=content)
    article.save()
    
    #2-3. 세 번째 방법
    # .save() 필요 없음 
    # Article.objects.create(title=title, content=content)

    # return render(request, 'articles/create.html')
    # 그렇다면 바로 보여주자... 무엇을? index.html 
    # 글이 안보임..?
    # return render(request, 'articles/index.html')

    # create 함수가 해야 하는 일(==글을 DB에 저장하는 일)은 끝!  index.html에서 모든 글을 보여주는 일은 index 함수에게 맡기자!
    # https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/#redirect
    return redirect('articles:detail', article.pk)

def detail(request, article_pk):
    #1. 상세 게시글을 조회하여 (article_pk)
    # https://docs.djangoproject.com/en/4.0/ref/models/querysets/#get
    article = Article.objects.get(pk=article_pk)
    #2. context에 담자
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    # https://docs.djangoproject.com/en/4.0/ref/request-response/#django.http.HttpRequest.method
    # print(request.method)
    
    # 만약 요청이 POST라면 글을 삭제하고 index 페이지로 redirect
    if request.method == 'POST':
        #1. DB에서 삭제하고자 하는 글을 가져온다.
        article = Article.objects.get(pk=article_pk)
        #2. 삭제한다.
        article.delete()
        #3. 삭제 이후 index로 돌린다.
        return redirect('articles:index')
    # POST가 아니면(GET) detail 돌린다.
    else:
        return redirect('articles:detail', article_pk)

# new와 비교
def edit(request, article_pk):
    # new와 다르게 기존 게시글을 수정 해야하기 때문에 
    # 넘어온 pk 값을 활용하여 DB에서 기존 게시글을 불러와
    # context에 담아 넘겨주자!
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

# create와 비교
def update(request, article_pk):
    #1. DB에서 기존 게시글 가져온다.
    article = Article.objects.get(pk=article_pk)

    #2. POST 요청을 통해 request body 안에 있는 title & content를 꺼내 변수에 담자
    # print(request.POST)
    title = request.POST.get('title')
    content = request.POST.get('content')

    #3. 받아 온 데이터로 게시글을 수정하자
    article.title = title
    article.content = content

    #4. 수정한 게시글을 저장한다.
    article.save()

    #4. detail 페이지로 redirect한다.
    # return redirect('articles:detail', article_pk)
    return redirect('articles:detail', article.pk)