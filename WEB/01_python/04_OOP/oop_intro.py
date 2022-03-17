# print(type('1'))
# print(type(1))

# 사람의 행동 양식을 정의 

class Person:

    def __init__(self, name, age):
        # js.name = 'justin'
        # js.age = 100

        # ch.name = 'bruno'
        # ch.age = 20
        self.name = name
        self.age = age
    
    def greeting(self):
        # self -> ch다!
        # print(self)
        # 
        # self.name == ch.name
        print(f'{self.name}입니다. 안녕하세요!!')
    

# 철현 -> ch를 인스턴스라고 부른다!
js = Person('justin', 100)
ch = Person('bruno', 20)
# print(js.name)
# print(js.age)
print('-------------')
print(ch.name)
print(ch.age)

# ch.greeting()
# ch.name = '철현'
# ch.age = 17
# print(ch.name)
# print(ch.age)

# mj = Person() # 민지님 프로그래밍 세계에서 태어남 
# mj.name = '민지'
# mj.age = 17
# print(mj.name)
# print(mj.age)
# mj.greeting()