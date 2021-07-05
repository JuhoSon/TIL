'''6273
list)한 학생의 국어, 수학 점수를 튜플로 저장하고 이 튜플을 항목으로 갖는 리스트 객체가 있습니다.
이 때 첫 번째 학생은 (90, 80), 두 번째 학생은 (85, 75), 세 번째 학생은 (90, 100)의 점수를 갖습니다.
다음과 같이 결과를 만들기 위한 프로그램을 작성하십시오.
'''
score = [(90, 80), (85, 75), (90, 100)]
for i in range(len(score)):
    print('{}번 학생의 총점은 {}점이고, 평균은 {}입니다.'.format(i+1, sum(score[i]), sum(score[i])/len(score[i])))

'''6275
list)리스트 내포 기능을 이용해 다음 문장으로부터 모음('aeiou')을 제거하십시오.
'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
'''
sen = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
# ''.join(list(filter(lambda x: x not in 'aeiou', sen)))
print(''.join([i for i in sen if i not in 'aeiou']))

'''6276
list)다음의 결과와 같이 구구단 2단부터 9단의 결과값 중에 3의 배수거나 7의 배수인 수를
제외한 값을 리스트 객체 result 안에 각 단마다 리스트를 만들어 삽입하고 이를 출력하십시오.
'''
stages = [2, 3, 4, 5, 6, 7, 8, 9]
steps = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [[stage*step for step in steps if (stage*step%3!=0)and(stage*step%7!=0)]
 for stage in stages]
print(result)

'''6277
list)리스트 내포 기능을 활용해 입력된 정수 값 5개의 평균을 출력하는 프로그램을 작성하십시오.
'''
uil = [int(input()) for _ in range(5)]
print('입력된 값 {}의 평균은 {}입니다.'.format(
    uil, sum(uil)/len(uil)
))

'''6280
list)다음의 결과와 같이 정수를 입력하면 약수를 리스트에 추가해 출력하는 코드를 작성하십시오.
'''
user_input = int(input())
print([i for i in range(1, user_input+1) if user_input % i == 0])

'''6281
list)다음의 결과와 같이 정수를 입력하면 리스트 내포를 이용해
약수 리스트를 출력하는 코드를 작성하십시오.
'''
user_input = int(input())
print([i for i in range(1, user_input+1) if user_input % i == 0])

'''6282
list)[1, 3, 11, 15, 23, 28, 37, 52, 85, 100] 와 같은 리스트 객체가 주어졌을 때
다음의 결과를 출력하는 짝수만 항목으로 가지는 리스트 객체를 생성하는 코드를 작성하십시오.
'''
print([i for i in [1, 3, 11, 15, 23, 28, 37, 52, 85, 100] if i % 2 == 0])

'''6286
list)리스트 내포 가능을 이용해 피보나치 수열 10번째까지 출력하는 프로그램을 작성하십시오.
'''
result = [1, 1]
[result.append(result[i-1]+result[i-2]) for i in range(2, 10)]
print(result)

'''6288
list)리스트 내포 기능을 이용하여 1부터 20사이의 숫자 중 3의 배수가 아니거나
5의 배수가 아닌 숫자들의 제곱 값으로 구성된 리스트 객체를 출력하는 프로그램을 작성하십시오.
'''
print([i**2 for i in range(1, 21) if (i%3!=0)or(i%5!=0)])

'''6289
list)사용자가 숫자를 입력하면 숫자의 각 자릿수의 합을 구해서 반환하는 프로그램을 작성하십시오.
예를 들어 123을 입력하면 1 + 2 + 3 = 6의 결과를 반환합니다.
'''
user_input = input()
print(sum([i for i in list(map(int, user_input))]))

'''6290
list)입력 받은 문자열 리스트를 가나다 순으로 따로 묶으려고 합니다.
다음과 같은 리스트가 주어졌을 때 결과처럼 가나다순(사전순)으로
따로 묶은 리스트가 출력되도록 리스트 내포를 이용한 프로그램을 작성하십시오.
dicBase = (('가','깋'), ('나','닣'), ('다','딯'), ('라','맇'), ('마','밓'), ('바','빟'), ('사','싷'),
               ('아','잏'), ('자','짛'), ('차','칳'), ('카','킿'), ('타','팋'), ('파','핗'), ('하','힣'))
inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다',
                   '수출', '계시다', '다', '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그',
                   '자르다', '데리다', '마리', '개', '정도', '옳다', '놀이','뜨겁다']
'''
dicBase = (('가','깋'), ('나','닣'), ('다','딯'), ('라','맇'), ('마','밓'), ('바','빟'), ('사','싷'),
               ('아','잏'), ('자','짛'), ('차','칳'), ('카','킿'), ('타','팋'), ('파','핗'), ('하','힣'))
inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다',
                   '수출', '계시다', '다', '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그',
                   '자르다', '데리다', '마리', '개', '정도', '옳다', '놀이','뜨겁다']
print([[word for word in inputWord if ord(word[0]) in range(ord(dic[0]), ord(dic[1]))]
 for dic in dicBase])

'''6292
list)콤마(,)로 구분된 정수 값을 입력받아 리스트와 튜플 객체를 생성하는 코드를 작성하십시오.
'''
ui1, ui2, ui3, ui4 = list(map(int, input().split(', ')))
print([ui1, ui2, ui3, ui4])
print((ui1, ui2, ui3, ui4))

'''6293
list)다음의 결과와 같이 사용자로부터 콤마(,)로 구분해 여러 원의 반지름을 입력 받아
이들에 대한 원의 둘레를 계산해 출력하는 프로그램을 작성하십시오.
'''
import math
ui1, ui2, ui3, ui4 = list(map(int, input().split(', ')))
print('{:.2f}, {:.2f}, {:.2f}, {:.2f}'.format(ui1*2*math.pi, ui2*2*math.pi, ui3*2*math.pi, ui4*2*math.pi))

'''6295
list)다음과 같이 2차원 배열 구조를 만들기 위한 행, 열 정보를 콤마(,)로 구분해 입력하고,
이 리스트 객체의 항목의 값은 행과 열의 인덱스 곱으로 초기화해 출력하는 프로그램을 작성하십시오.
'''
rows, cols = list(map(int, input().split(', ')))
print([[row*col for col in range(cols)] for row in range(rows)])

'''6296
list)단어를 콤마(,)로 구분해 입력하면 그 단어들을 사전순으로 정렬해 출력하는 프로그램을 작성하시시오.
'''
uil = list(input().split(', '))
print(', '.join(sorted(uil)))

'''6297
list)콤마(,)로 구분해 숫자를 입력하고, 입력된 숫자 중 홀수를 콤마(,)로 구분해 출력하는
리스트 내포 기능을 이용한 프로그램을 작성하십시오.
'''
print(', '.join(list(filter(lambda x:int(x)%2!=0, input().split(', ')))))

'''6298
list)주어진 튜플 (1,2,3,4,5,6,7,8,9,10)의 앞 항목 절반과 뒤 항목 절반을 출력하는 프로그램을 작성하십시오.
'''
print(tuple(i for i in (1,2,3,4,5,6,7,8,9,10) if i <= 5))
print(tuple(i for i in (1,2,3,4,5,6,7,8,9,10) if i > 5))

'''6299
list)리스트 내포 기능을 이용해 [5, 6, 77, 45, 22, 12, 24]에서 짝수를 제거한 후 리스트를
출력하는 프로그램을 작성하십시오.
'''
print([i for i in [5, 6, 77, 45, 22, 12, 24] if i % 2 != 0])

'''6300
list)리스트 내포 기능을 이용해 [12, 24, 35, 70, 88, 120, 155]에서
홀수번째 항목을 제거한 후 리스트를 출력하는 프로그램을 작성하십시오.
'''
ui = [12, 24, 35, 70, 88, 120, 155]
print([i for i in ui if ui.index(i) % 2 != 0])

'''6301
list)항목 값으로는 0을 갖는 2*3*4 형태의 3차원 배열을 생성하는
리스트 내포 기능을 이용한 프로그램을 작성하십시오.
'''
print([[[0 for col in range(4)] for row in range(3)] for width in range(2)])

'''6302
list)리스트 내포 기능을 이용해 [12, 24, 35, 70, 88, 120, 155]에서
첫번째, 다섯번째, 여섯번째 항목을 제거한 후 리스트를 출력하는 프로그램을 작성하십시오.
'''
ui = [12, 24, 35, 70, 88, 120, 155]
print([i for i in ui if ui.index(i) not in [0, 4, 5]])

'''6303
list)두 개의 리스트 [1,3,6,78,35,55]와 [12,24,35,24,88,120,155]를 이용해
양쪽 리스트에 모두 있는 항목을 리스트로 반환하는 프로그램을 작성하십시오.
'''
print([i for i in [1,3,6,78,35,55] if i in [12,24,35,24,88,120,155]])

'''6305
list)리스트의 항목 중 중복이 되는 항목을 제거하는 함수를 정의하고 이 함수를 이용해
[12,24,35,24,88,120,155,88,120,155]에서 중복이 제거된 리스트를 출력하십시오.
'''
ui = [12,24,35,24,88,120,155,88,120,155]
result = []
[result.append(i) for i in [12,24,35,24,88,120,155,88,120,155] if i not in result]
print(result)

'''6254
dict)다음과 같이 등록된 학생의 이름을 출력하고, 이름을 입력하면 전화번호를 출력해주는
딕셔너리 객체를 이용한 전화번호부 프로그램을 작성하십시오.
[등록된 학생]
홍길동: 010-1111-1111
이순신: 010-1111-2222
강감찬: 010-1111-3333
[프로그램]
아래 학생들의 전화번호를 조회할 수 있습니다.
홍길동
이순신
강감찬
전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.
'''
dic = {"홍길동": "010-1111-1111",
        "이순신": "010-1111-2222",
        "강감찬": "010-1111-3333"}
print('아래 학생들의 전화번호를 조회할 수 있습니다.')
for k in dic.keys():
    print(k)
print('전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.')
user_input = input()
print('{}의 전화번호는 {}입니다.'.format(user_input, dic[user_input]))

'''6255
dict)아래의 상품 딕셔너리 데이터를 가격에 따라 내림차순으로 정렬하는 프로그램을 작성하십시오.
"TV": 2000000,
"냉장고": 1500000,
"책상": 350000,
"노트북": 1200000,
"가스레인지": 200000,
"세탁기": 1000000
'''
dic = {"TV": 2000000,
"냉장고": 1500000,
"책상": 350000,
"노트북": 1200000,
"가스레인지": 200000,
"세탁기": 1000000}
ordered_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
print('\n'.join(['{}: {}'.format(k, v) 
for k, v in ordered_dic]))

'''6256
dict)다음 두 딕셔너리 객체를 합쳐 중복된 메뉴가 없는 딕셔너리를 만들고
가격이 3000원 이상인 메뉴를 아래와 같이 출력하는 프로그렘을 작성하십시오.
중복된 메뉴의 가격이 다를 경우 딕셔너리 a의 가격을 사용하세요.
a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}
'''
a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
dic = {'헤이즐럿라떼': 2900, '카페모카': 3400, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}
dic.update(a)  # a가격 사용
result = dict(filter(lambda x: x[1] >= 3000, dic.items()))
print(set(zip(result.keys(), result.values())))

'''6257
dict)리스트의 원소를 키로 하고, 그 원소의 length를 값으로 갖는 딕셔너리 객체를 생성하는 코드를 작성해봅시다.
이 때 딕셔너리 내포 기능을 사용하며, 원소의 공백은 제거합니다.
리스트 fruit는 다음과 같습니다. fruit = ['   apple    ','banana','  melon']
'''
fruit = ['   apple    ','banana','  melon']
fruit_after = list(map(lambda x: x.strip(), fruit))
fruit_length = list(map(lambda x: len(x), fruit_after))
dic = {k:v for k, v in zip(fruit_after, fruit_length)}
print(dic)

'''6258
dict)다음과 같이 정수 N을 입력받아서 1부터 N까지의 정수를 키로 하고, 
그 정수의 제곱을 값으로 하는 딕셔너리 객체를 만드는 코드를 작성하십시오.
'''
N = int(input())
print({i:i**2 for i in range(1, N+1)})

'''6259
dict)다음과 같이 사용자가 입력한 문장에서 숫자와 문자를 구별해 각각의 개수를 출력하는 프로그램을 작성하십시오.
'''
user_input = input()
let_cnt = sum([1 for i in user_input if i.isalpha()])
dig_cnt = sum([1 for i in user_input if i.isdigit()])
dic = {'LETTERS':let_cnt, 'DIGITS':dig_cnt}
for k, v in dic.items():
    print(k, v)

'''6260
dict)다음과 같이 사용자가 입력한 문장에서 대소문를 구별해 각각의 갯수를 출력하는 프로그램을 작성하십시오.
'''
user_input = input()
up_cnt = sum([1 for i in user_input if 65 < ord(i) < 90])
lo_cnt = sum([1 for i in user_input if 97 < ord(i) < 122])
dic = {'UPPER CASE':up_cnt, 'LOWER CASE':lo_cnt}
for k, v in dic.items():
    print(k, v)

'''6261
dict)다음과 같은 기존의 맥주 가격을 5% 인상하려고 할 경우
딕셔너리 내포 기능을 이용한 코드를 작성하십시오.
beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
'''
beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
new_beer = {k:v*1.05 for k, v in beer.items()}
print(beer)
print(new_beer)

'''6262
dict)다음의 결과와 같이 입력된 문자열의 문자 빈도수를 구하는 프로그램을 작성하십시오.
'''
user_input = input()
dic = {k:0 for k in set(user_input)}
for i in user_input:
    dic[i] += 1
for k, v in sorted(dic.items(), key=lambda x:x[0]):
    print('{},{}'.format(k,v))

'''6232
string)다음의 결과와 같이 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.
'''
user_input = input()
idx = 0
result = ''
for s in user_input:
    if user_input[idx] != user_input[-(idx+1)]:
        break
    result += s
    idx += 1
if user_input == result:
    print(user_input)
    print('입력하신 단어는 회문(Palindrome)입니다.')

'''6239
string)다음과 같이 문장을 구성하는 단어를 역순으로 출력하는 프로그램을 작성하십시오.
'''
user_input = input()
print(' '.join(reversed(user_input.split())))

'''6241
string)다음의 결과와 같이 임의의 URL 주소를 입력받아 protocol, host, 나머지(path, querystring, ...)로
구분하는 프로그램을 작성하십시오.
'''
user_input = input()
result = list(filter(lambda x: x!='', map(lambda x: x.replace(':',''), user_input.split('/'))))
print("protocol: {}\nhost: {}\nothers: {}".format(result[0], result[1], result[2]))

'''6678
string)다음의 결과와 같이 여러 문장을 입력받아 대문자로 변환해 출력하는 프로그램을 작성합니다.
아무 것도 입력하지 않고 엔터만 입력하면 입력이 종료됩니다.
'''
while True:
    try:
        print(">> {}".format(input().upper()))
    except EOFError:
        break
# 문제가 이상한가?!

'''6243
string)사용자가 입력한 문장에서 공백을 이용해 단어들을 구분하고,
중복된 단어없이 단어를 콤마(,)로 구분해 사전순으로 출력하는 프로그램을 작성하십시오.
'''
user_input = input()
print(','.join(sorted(set(user_input.split()))))

'''6248
string)다음 결과와 같이 문자열을 입력하면 짝수 인덱스를 가진 문자들을 출력하는 프로그램을 작성하십시오.
'''
user_input = input()
print(''.join(list(filter(lambda x: user_input.index(x) % 2 == 0, user_input))))

'''6203
oop)다음의 결과와 같이 국어, 영어, 수학 점수를 입력받아 합계를 구하는 객체지향 코드를 작성하십시오.
이 때 학생 클래스의 객체는 객체 생성 시 국어, 영어, 수학 점수를 저장하며, 총점을 구하는 메서드를 제공합니다.
'''
class student:
    def __init__(self, ko, en, ma):
        self.korean = ko
        self.english = en
        self.math = ma
    
    def get_sum(self):
        print('국어, 영어, 수학의 총점: {}'.format(self.korean + self.english + self.math))

k, e, m = map(int, input().split(', '))
stu = student(k, e, m)
stu.get_sum()

'''
6208
국적을 출력하는 printNationality 정적 메서드를 갖는 Korean 클래스를 정의하고
메서드를 호출하는 코드를 작성해봅시다.
'''
class Korean:
    def __init__(self):
        self.nation = '대한민국'
    
    def printNationality(self):
        print(self.nation)
        print(self.nation)

k = Korean()
k.printNationality()

'''6217
name 프로퍼티를 가진 Student를 부모 클래스로 major 프로퍼티를 가진
GraduateStudent 자식 클래스를 정의하고 이 클래스의 객체를
다음과 같이 문자열로 출력하는 코드를 작성하십시오.
'''
class Student():
    def __init__(self, name):
        self.name = name

class GraduateStudent(Student):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

s = Student('홍길동')
gs = GraduateStudent('이순신', '컴퓨터')
print('이름: {}\n이름: {}, 전공: {}'.format(s.name, gs.name, gs.major))

'''6223
반지름 정보를 갖고, 원의 면적을 계산하는 메서드를 갖는 Circle 클래스를 정의하고,
생성한 객체의 원의 면적을 출력하는 프로그램을 작성하십시오.
'''
class Circle:
    def __init__(self, r):
        self.radius = r
    
    def get_area(self):
        print('원의 면적: {:.2f}'.format(3.14*self.radius**2))

c = Circle(2)
c.get_area()

'''6225
가로, 세로 정보을 갖고, 사각형의 면적을 계산하는 메서드를 갖는 Rectangle 클래스를 정의하고,
생성한 객체의 사각형의 면적을 출력하는 프로그램을 작성하십시오.
'''
class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h
    
    def get_area(self):
        print('사각형의 면적: {}'.format(self.width * self.height))

r = Rectangle(4, 5)
r.get_area()

'''6228
Shape를 부모 클래스로 Square 자식 클래스를 정의하는 코드를 작성하십시오.
Square 클래스는 length 필드를 가지며, 0을 반환하는 Shape 클래스의 area 메서드를
length * length 값을 반환하는 메서드로 오버라이딩합니다.
'''
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        self.length = l
    
    def area(self):
        # super().area()
        return self.length*self.length

s = Square(3)
print('정사각형의 면적: {}'.format(s.area()))

'''6229
Person를 부모 클래스로 Male, Female 자식 클래스를 정의하는 코드를 작성하십시오.
"Unknown"을 반환하는 Person 클래스의 getGender 메서드를 Male 클래스와 Female 클래스는
"Male", "Female" 값을 반환하는 메서드로 오버라이딩합니다.
'''
class Person:
    def getGender(self):
        return "Unknown"

class Male(Person):
    def getGender(self):
        return 'Male'

class Female(Person):
    def getGender(self):
        return 'Female'

m = Male()
f = Female()
print(m.getGender())
print(f.getGender())