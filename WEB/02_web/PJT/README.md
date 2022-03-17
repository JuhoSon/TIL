# Project 03_반응형 웹 페이지 구성

## 1. 프로젝트 소개

- 진행 일시: 2022.02.11 (금)

- 프로젝트 내용 요약
  - HTML, CSS, Bootstrap(component, grid)
  
  

## 2. 해결 과정

### 1) problem_a

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
  <!-- Custom CSS -->
  <link rel="stylesheet" href="01_nav_footer.css">

  <title>Navbar Footer Test</title>
</head>
<body>
  <!-- 01_nav_footer.html -->
  <nav class="navbar sticky-top navbar-expand-md navbar-dark bg-dark">
    <div class="container-fluid justify-content-between">
      <a class="navbar-brand" href="./02_home.html">
        <img class="img-fluid" src="./images/logo.png" alt="logo" style="width: 200px">
        <!-- 20%로 하니까 brand가 차지하는 a태그 너비가 너무 넓어지는데 왜일까.. -->
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNavDropdown">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="./02_home.html">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="./03_community.html">Community</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#loginModal">Login</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  
  <!-- Modal -->
  <div class="modal fade" id="loginModal" tabindex="-1" aria-labelledby="loginModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="loginModalLabel">Login</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="form-group">
              <label for="exampleInputEmail1">ID</label>
              <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="ID">
            </div>
            <div class="form-group">
              <label for="exampleInputPassword1">Password</label>
              <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-dark">Login</button>
        </div>
      </div>
    </div>
  </div>

  <footer class="fixed-bottom justify-content-center text-center mb-2">Web-bootstrap PJT, by zoohoson</footer>

  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
</body>
</html>

```



- brand 이미지 넣을 때, 사이즈가 마음대로 조절이 안되서 그냥 200px로 고정했다. 맞는건지 ... 정답을 알수없다..



### 2) problem_b

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
  <!-- Custom CSS -->
  <link rel="stylesheet" href="01_nav_footer.css">
  <link rel="stylesheet" href="02_home.css">
  
  <title>Home</title>
</head>
<body>
  
  <!-- 01_nav_footer.html -->
  <!-- 01_nav_footer 에서 완성한 Navigation bar 코드를 붙여넣어 주세요. -->
  <nav class="navbar sticky-top navbar-expand-md navbar-dark bg-dark">
    <div class="container-fluid justify-content-between">
      <a class="navbar-brand" href="./02_home.html">
        <img class="img-fluid" src="./images/logo.png" alt="logo" style="width: 200px">
        <!-- 20%로 하니까 brand가 차지하는 a태그 너비가 너무 넓어지는데 왜일까.. -->
      </a>
      <button class="navbar-toggler col-md" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNavDropdown">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="./02_home.html">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="./03_community.html">Community</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#loginModal">Login</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Modal -->
  <div class="modal fade" id="loginModal" tabindex="-1" aria-labelledby="loginModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="loginModalLabel">Login</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="form-group">
              <label for="exampleInputEmail1">ID</label>
              <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="ID">
            </div>
            <div class="form-group">
              <label for="exampleInputPassword1">Password</label>
              <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-dark">Login</button>
        </div>
      </div>
    </div>
  </div>

  <!-- 02_home.html -->
  <header>
    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
      <ol class="carousel-indicators">
        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
      </ol>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img class="d-block w-100" src="./images/header1.jpg" alt="First slide">
        </div>
        <div class="carousel-item">
          <img class="d-block w-100" src="./images/header2.jpg" alt="Second slide">
        </div>
        <div class="carousel-item">
          <img class="d-block w-100" src="./images/header3.jpg" alt="Third slide">
        </div>
      </div>
      <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only"></span>
      </a>
      <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only"></span>
      </a>
    </div>
  </header>

  <h1 class="text-dark text-center my-3">Boxoffice</h1>

  <section class="container d-flex justify-content-center">
    <article class="mt-4 row col-6 col-sm-12">
      <div class="card-deck"></div>
        <div class="card" style="width: 14rem;">
          <img class="card-img-top" src="./images/movie1.jpg" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title text-center">Card title</h5>
            <p class="card-text text-center">blahblah</p>
          </div>
        </div>
        <div class="card" style="width: 14rem;">
          <img class="card-img-top" src="./images/movie2.jpg" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title text-center">Card title</h5>
            <p class="card-text text-center">blahblah</p>
          </div>
        </div>
        <div class="card" style="width: 14rem;">
          <img class="card-img-top" src="./images/movie3.jpg" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title text-center">Card title</h5>
            <p class="card-text text-center">blah</p>
          </div>
        </div>
        <div class="card" style="width: 14rem;">
          <img class="card-img-top" src="./images/movie4.jpg" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title text-center">Card title</h5>
            <p class="card-text text-center">blahblah</p>
          </div>
        </div>
        <div class="card" style="width: 14rem;">
          <img class="card-img-top" src="./images/movie5.jpg" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title text-center">Card title</h5>
            <p class="card-text text-center">blahblah</p>
          </div>
        </div>
        <div class="card" style="width: 14rem;">
          <img class="card-img-top" src="./images/movie6.jpg" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title text-center">Card title</h5>
            <p class="card-text text-center">blabla</p>
          </div>
        </div>
      </article>
    </div>
  </section>

  <!-- 01_nav_footer.html -->
  <!-- 01_nav_footer 에서 완성한 Footer 코드를 붙여넣어 주세요. -->
  <footer class="fixed-bottom justify-content-center text-center mb-2">Web-bootstrap PJT, by zoohoson</footer>
  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>  
</body>
</html>
```

- 캐주얼이 분명히 코드 그대로 넣었는데 동작이 잘 안된다 .. 자바스크립트 버전 에러일까? ㅠ 



### 3) problem_c

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

  <!-- Custom CSS -->
  <link rel="stylesheet" href="01_nav_footer.css">
  <link rel="stylesheet" href="03_community.css">

  <title>Community</title>
</head>
<body>

  <!-- 01_nav_footer.html -->
  <!-- 01_nav_footer 에서 완성한 Navigation bar 코드를 붙여넣어 주세요. -->
  <nav class="navbar sticky-top navbar-expand-md navbar-dark bg-dark">
    <div class="container-fluid justify-content-between">
      <a class="navbar-brand" href="./02_home.html">
        <img class="img-fluid" src="./images/logo.png" alt="logo" style="width: 200px">
        <!-- 20%로 하니까 brand가 차지하는 a태그 너비가 너무 넓어지는데 왜일까.. -->
      </a>
      <button class="navbar-toggler col-md" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNavDropdown">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link" aria-current="page" href="./02_home.html">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" href="./03_community.html">Community</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#loginModal">Login</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Modal -->
  <div class="modal fade" id="loginModal" tabindex="-1" aria-labelledby="loginModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="loginModalLabel">Login</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="form-group">
              <label for="exampleInputEmail1">ID</label>
              <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="ID">
            </div>
            <div class="form-group">
              <label for="exampleInputPassword1">Password</label>
              <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-dark">Login</button>
        </div>
      </div>
    </div>
  </div>

  <!-- 03_community.html -->
  <h1 class="text-center my-5">Community</h1>
  <div class="main container row d-flex justify-content-center">
    <!-- Sidebar -->
    <aside class="col-12 col-lg-2">
      <ul class="list-group">
        <li class="list-group-item">
          <a href="#" class="text-decoration-none">Boxoffice</a>
        </li>
        <li class="list-group-item"><a href="#" class="text-decoration-none">Movies</a></li>
        <li class="list-group-item"><a href="#" class="text-decoration-none">Genres</a></li>
        <li class="list-group-item"><a href="#" class="text-decoration-none">Actors</a></li>
      </ul>
    </aside>

    <!-- Board -->
    <section class="col-12 col-lg-10">
      <div>
        <table class="body-table table table-striped my-4">
          <thead class="thead-dark">
            <tr>
              <th scope="col">영화 제목</th>
              <th scope="col">글 제목</th>
              <th scope="col">작성자</th>
              <th scope="col">작성 시간</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">ever</th>
              <td>hi</td>
              <td>itsme</td>
              <td>1 min ago</td>
            </tr>
            <tr>
              <th scope="row">note</th>
              <td>hello</td>
              <td>realme</td>
              <td>1 min ago</td>
            </tr>
          </tbody>
        </table>
        
      <div class="body-article">
        <article>
          <hr class="my-2">
          <h3>ever</h3>
          <div>hi</div>
          <div>1 min ago</div>
          <div>itsme</div>

          <hr class="my-2">
          <h3>note</h3>
          <div>hello</div>
          <div>1 min ago</div>
          <div>realme</div>
        </article>
      </div>

      <nav aria-label="Page navigation example">
        <ul class="pagination justify-content-center">
          <li class="page-item"><a class="page-link" href="#">Previous</a></li>
          <li class="page-item"><a class="page-link" href="#">1</a></li>
          <li class="page-item"><a class="page-link" href="#">2</a></li>
          <li class="page-item"><a class="page-link" href="#">3</a></li>
          <li class="page-item"><a class="page-link" href="#">Next</a></li>
        </ul>
      </nav>
    </section>
  </div>

  <!-- 01_nav_footer.html -->
  <!-- 01_nav_footer 에서 완성한 Footer 코드를 붙여넣어 주세요. -->

  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

</body>
</html>
```

```css
/* 03_community.css */
/* 아래에 코드를 작성해 주세요. */
@media screen and (min-width: 992px){
  .body-article{
    display:none;
  }
}

@media screen and (max-width: 992px){
  .body-table{
    display:none;
  }
}
```



- 미디어커리를 활용해서 테이블과 article을 왔다갔다 했다.





## 3. 후기

💡 프론트엔드 ... 넘나 망망대해에 떠있는 기분이다

💡 분명 수업들을땐 너무 재밌고 오 .. 저렇게 뚝딱뚝딱만들수있단말이야? 이러는데 내가하면 다 안된다. 그림 엇나가고 사이즈 조절안되고 ..... 속상하다.

🙂 잘한 점

1. 가물가물한 기억을 더듬어가며 여러 component를 사용할 수 있었고, 완벽한 코드는 아니지만 레아아웃과 비슷하게 만드는 날 보면서 직장인이 된것같았다.

🙁 아쉬운 점

1. 끝가지 파고들어서 세세한 작동방식을 다 알면 좋을텐데, HTML CSS bootstrap의 작동방식을 하나하나 공부할 만큼 재미가 없는 것 같아 아쉽다.(노션에 아티클이나 수업참고자료를 다읽어봤는데 흥미가 없다...) 얼른 백엔드배워보고싶다.