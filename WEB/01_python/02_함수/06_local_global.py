def ham():
    a = 'spam'
    return a

# 1.
# print(a) # NameError: name 'a' is not defined

# 2.
ham() 
print(a) # NameError: name 'a' is not defined

# 함수는 가장 기본 : local scope!
# 블랙박스의 결과를 받아보고 싶으면 반환 값을 변수에 저장해서 사용하는 것!
# 블랙박스 밖으로 결과를 주고 싶을 수 있어요! => return 해야해요