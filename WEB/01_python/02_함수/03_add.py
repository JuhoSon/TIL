def add(x, y):
    return x + y 

print(add(1, 2)) # 위치 - 내부에서 바인딩 x = 1; y = 2
print(add(y=2, x=1)) # 키워드 - 제가 직접 x와 y 값을 각각 지정
# print(add(x=1, 2)) 
# # SyntaxError: positional argument follows keyword argument
# 키워드로 지정하는 순간 위치가 이미 의미가 없어졌다. => 에러
print(add(1, y=2)) # 위치 지정.. 키워드
# print(add(1, 2, 3))
# TypeError: add() takes 2 positional arguments but 3 were given
# 2개 받는 함수인데 3개 줌!