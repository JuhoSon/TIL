'''6216
basic)20% 농도의 소금물 100g과 물 200g을 혼합한 소금물의 농도(%)를
소수점 두 번째 자리까지 구하는 프로그램을 작성하십시오.
'''
salt = 20
salt_water = 100 + 200
concentration = salt/salt_water * 100
print('혼합된 소금물의 농도: {:.2f}%'.format(concentration))

'''6218
if)다음의 결과와 같이 임의의 양의 정수를 입력받아
그 정수의 모든 약수를 구하십시오
'''
user_input = int(input())
divisor = [num for num in range(1, user_input+1) if user_input % num == 0]
for d in divisor:
    print('{}(은)는 {}의 약수입니다.'.format(d, user_input))

'''6219
if)다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오
(단, 약수가 2개일 경우 소수임을 나타내십시오)
'''
user_input = int(input())
divisor = [num for num in range(1, user_input+1) if user_input % num == 0]
for d in divisor:
    print('{}(은)는 {}의 약수입니다.'.format(d, user_input))
if len(divisor)==2:
print('{}(은)는 {}과 {}로만 나눌 수 있는 소수입니다.'.format(
        user_input, divisor[0], divisor[1]))

'''6220
if)다음의 결과와 같이 입력된 영어 알파벳 문자에 대해 대소문자를 구분하는 코드를 작성하십시오.
'''
user_input = input()
small = 'abcdefghijklmnopqrstuvwxyz'
if user_input in small:
    print('{} 는 소문자 입니다.'.format(user_input))

'''6221
if)다음의 결과와 같이 가상의 두 사람이 가위 바위 보 중 하나를 내서 승패를 가르는 가위 바위 보 게임을 작성하십시오.
이 때 ["가위", "바위", "보"] 리스트를 활용합니다.
'''
man1 = input()
man2 = input()
rcp_list = ['가위', '바위', '보']
if man1 == man2:
    print('Result : Draw')
elif (man1==rcp_list[0] and man2==rcp_list[1]) or (man1==rcp_list[1] and man2==rcp_list[2]) or (man1==rcp_list[2] and man2==rcp_list[0]):
    print('Result : Man2 Win!')
else:
    print('Result : Man1 Win!')

'''6222
if)다음의 결과와 같이 입력된 문자가 대문자일 경우 소문자로, 소문자일 경우 대문자로 변경하고,
알파벳이 아닐 경우엔 그냥 출력하는 코드를 작성하십시오.
출력 시 아스키코드를 함께 출력합니다.
'''
user_input = input()
if ord(user_input) in range(97, 123):
    print('{}(ASCII: {}) => {}(ASCII: {})'.format(user_input, ord(user_input),
                                        user_input.upper(), ord(user_input.upper())))
elif ord(user_input) in range(65, 91):
    print('{}(ASCII: {}) => {}(ASCII: {})'.format(user_input, ord(user_input),
                                        user_input.lower(), ord(user_input.lower())))
else:
    print(user_input)

'''6226
if)1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 모든 숫자들을 찾아
콤마(,)로 구분된 문자열을 구성해 출력하는 프로그램을 작성하십시오.
'''
print(','.join([str(i) for i in range(1, 201) if ((i % 7 == 0)and(i % 5 != 0))]))

'''6227
if)100~300 사이의 숫자에서 각각의 자리 숫자가 짝수인 숫자를 찾아 콤마(,)로 구분해 출력하는 프로그램을 작성하십시오.
'''
print(','.join([str(i) for i in range(100, 301) if (
    ((i//100) % 2 ==0) and
    (((i%100)//10) % 2 == 0) and
    ((i%10) % 2 == 0)
)]))

'''6230
roop)다음의 결과와 같이 5명의 학생의 점수에 대해 60 이상일 때 합격 메시지를 출력하고,
60미만일 때 불합격 메시지를 출력하는 프로그램을 만드십시오.
'''
score_list = [88, 30, 61, 55, 95]
for i in range(len(score_list)):
    if score_list[i] >= 60:
        flag = '합격'
    else:
        flag = '불합격'
    print("{}번 학생은 {}점으로 {}입니다.".format(i+1, score_list[i], flag))

'''6231
roop)1부터 100까지의 숫자를 for 문과 range 함수를 이용해 출력하십시오.
'''
print('\n'.join([str(i) for i in range(1, 101)]))

'''6234
roop)1부터 100사이의 숫자 중 짝수를 for 문을 이용해 다음과 같이 출력하십시오.
'''
print(' '.join([str(i) for i in range(1, 101) if i % 2 == 0]))

'''6238
roop)1부터 100사이의 숫자 중 홀수를 for 문을 이용해 다음과 같이 출력하십시오.
'''
print(', '.join([str(i) for i in range(1, 101) if i % 2 != 0]))

'''6240
roop)1부터 100사이의 숫자 중 3의 배수의 총합을 for 문을 이용해 출력하십시오.
'''
print('1부터 100사이의 숫자 중 3의 배수의 총합:', sum([i for i in range(1, 101) if i % 3 == 0]))

'''6242
roop)다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.
'''
stu_ABO = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
A_cnt = 0
B_cnt = 0
O_cnt = 0
AB_cnt = 0
for abo in stu_ABO:
    if abo == 'A':
        A_cnt += 1
    elif abo == 'B':
        B_cnt += 1
    elif abo == 'AB':
        AB_cnt += 1
    elif abo == 'O':
        O_cnt += 1
# print("{'A': {0}, 'O': {1}, 'B': {2}, 'AB': {3}}".format(A_cnt, O_cnt, B_cnt, AB_cnt))
print("{'A': %d, 'O': %d, 'B': %d, 'AB': %d}"%(A_cnt, O_cnt, B_cnt, AB_cnt))

'''6244
roop)다음은 학생의 점수를 나타내는 리스트입니다.
[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.
'''
stu_score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
idx = len(stu_score)-1
sum_score = 0
while idx >= 0:
    if stu_score[idx] >= 80:
        sum_score += stu_score.pop(idx)
    idx -= 1
print(sum_score)

'''6246
roop)while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
'''
cnt = 5
while cnt > 0:
    print('*'*cnt)
    cnt -= 1
'''6247
roop)while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
'''
cnt = 4
while cnt > 0:
    print(' '*(4-cnt) + '*'*(cnt*2-1))
    cnt -= 1

'''6249
roop)다음의 결과와 같이 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.
'''
user_input = input()
cnt_09 = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
for i in user_input:
    cnt_09[int(i)] += 1
print(' '.join(list(map(str, cnt_09.keys()))))
print(' '.join(list(map(str, cnt_09.values()))))

'''6251
roop)for문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
'''
result = [' '*(5-cnt)+'*'*cnt for cnt in range(1, 6)]
for i in result:
    print(i)

'''6253
roop)다음의 결과와 같이 10진수를 2진수로 변환하는 프로그램을 작성하십시오.
'''
user_input = int(input())
result = ''
while True:
    result += str(user_input % 2)
    user_input //= 2
    if user_input <= 1:
        result += str(user_input)
        break
print(''.join(list(reversed(result))))

'''6319
func)다음의 결과와 같이 반목문을 이용해 단어의 순서를 거꾸로 해 반환하는 함수를 작성하고
그 함수를 이용해 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.
'''
def palin(user_input):
    if ''.join(list(reversed(user_input))) == user_input:
        print(user_input)
        print('입력하신 단어는 회문(Palindrome)입니다.')
user_input = input()
palin(user_input)

'''6320
func)다음과 같이 사용자 2명으로부터 가위, 바위, 보를 입력 받아
가위, 바위, 보 규칙이 정의된 함수를 이용해 승패를 결정하는 코드를 작성하십시오.
'''
name1 = input()
name2 = input()
n1_what = input()
n2_what = input()
def winlose(what1, what2):
    if (what1 == '바위' and what2 == '가위') or (what1 == '가위' and what2 == '보') or (what1 == '보' and what2 == '바위'):
        if what1 == '바위':
            print('바위가 이겼습니다!')
    elif (what1 == '가위' and what2 == '바위') or (what1 == '바위' and what2 == '보') or (what1 == '보' and what2 == '가위'):
        if what2 == '바위':
            print('바위가 이겼습니다!')
winlose(n1_what, n2_what)

'''6321
func)소수를 검사하는 함수를 정의하고, 다음의 결과와 같이 사용자가 입력한 숫자가
소수인지를 판단하는 프로그램을 작성하십시오.
소수일 경우 "소수입니다." 출력, 아닐 경우 "소수가 아닙니다." 출력
'''
def prime(num):
    if len([i for i in range(1, num+1) if (num % i == 0)])==2:
        print('소수입니다.')
user_input = int(input())
prime(user_input)

'''6323
func)다음의 결과와 같이 피보나치 수열의 결과를 생성하는 프로그램을 작성하십시오.
'''
def fibo(num):
    fibo_l = []
    for i in range(num):
        if i in [0, 1]:
            fibo_l.append(1)
        else:
            fibo_l.append(fibo_l[i-2]+fibo_l[i-1])
    print(fibo_l)
user_input = int(input())
fibo(user_input)

'''6324
func)리스트의 항목 중 유일한 값으로만 구성된 리스트를 반환하는 함수를 정의하고
이 함수를 이용해 리스트의 중복 항목을 제거하는 프로그램을 작성하십시오.
'''
ori = [1, 2, 3, 4, 3, 2, 1]
def remov_repli(li):
    result = []
    for i in ori:
        if i not in result:
            result.append(i)
    print(li)
    print(result)
remov_repli(ori)

'''6325
func)정렬된 숫자를 가진 리스트에서 특정 숫자를 찾는 함수를 정의하고,
이 함수를 이용해 임의의 숫자의 포함 여부를 출력하는 프로그램을 작성하십시오.
'''
ori = [2, 4, 6, 8, 10]
def find_li(li, num):
    if num in li:
        print('{} => True'.format(num))
    else:
        print('{} => False'.format(num))
print(ori)
find_li(ori, 5)
find_li(ori, 10)

'''6326
func)다음과 같이 팩토리얼을 구하는 함수를 정의해 입력된 숫자에 대한
팩토리얼 값을 구하는 프로그램을 작성하십시오.
'''
def fac(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    print(result)
user_input = int(input())
fac(user_input)

'''6327
func)숫자에 대해 제곱을 구하는 함수를 정의히고, 다음과 같이 숫자를 콤마(,)로 구분해 입력하면
정의한 함수를 이용해 제곱 값을 출력하는 프로그램을 작성하십시오.
'''
user_input = input()
def sq(num):
    return num**2
for i in map(int, user_input.split(', ')):
    print('square({}) => {}'.format(i, sq(i)))

'''6328
func)인자로 전달된 두 개의 문자열 중 길이가 더 긴 문자열을 출력하는 함수를 정의하고
결과를 출력하는 프로그램을 작성하십시오.
'''
user_input = input()
def which_long(user_input):
    fir = user_input.split(', ')[0]
    sec = user_input.split(', ')[1]
    if len(fir) > len(sec):
        print(fir)
    elif len(fir) < len(sec):
        print(sec)
which_long(user_input)

'''6329
func)인자로 전달된 숫자를 이용해 카운트다운하는 함수 countdown을 정의하고,
이 함수를 이용하여 countdown(0), countdown(10)을 순서대로 실행하십시오.
0보다 작거나 같은 인자가 전달되었을 경우 "카운트다운을 하려면 0보다 큰 입력이 필요합니다."를 출력하십시오.
'''
def countdown(num):
    if num <= 0:
        print('카운트다운을 하려면 0보다 큰 입력이 필요합니다.')
    else:
        for i in list(reversed(range(1, 11))):
            print(i)
countdown(0)
countdown(10)

'''6308
innerfunc)다음의 결과와 같이 이름과 나이를 입력 받아
올해를 기준으로 100세가 되는 해를 표시하는 코드를 작성하십시오.
'''
name = input()
age = int(input())
print('{}(은)는 {}년에 100세가 될 것입니다.'.format(name, 2019+(100-age)))

'''6311
innerfunc)"ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"와
같은 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때 문자열에 사용된
알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오.
'''
user_input = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
score = {'A':4, 'B':3, 'C':2, 'D':1}
print(sum(list(map(lambda x:score[x], user_input))))

'''6312
innerfunc)가변형 인자로 정수들을 입력받아 곱을 반환하는 함수를 정의하고,
단, 1, 2, '4', 3와 같이 제대로 입력되지 않은 경우 예외를 처리하는 프로그램을 작성하십시오.
'''
def multi(*args):
    result = 1
    if True in [type(i)==type('str') for i in args]:
        print('에러발생')
    else:
        for i in args:
            result *= i
        print(result)
multi(1, 2, '4', 3)

'''6313
innerfunc)ASCII 코드 값를 입력받아 문자를 확인하는 코드를 작성하십시오.
'''
user_input = int(input())
print('ASCII {} => {}'.format(user_input, chr(user_input)))

'''6314
innerfunc)1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해
짝수만을 선택해 리스트를 반환하는 프로그램을 작성하십시오.
'''
ori = list(range(1, 11))
print(list(filter(lambda x:x%2==0, ori)))

'''6315
innerfunc)1~10까지의 정수를 항목으로 갖는 리스트 객체에서 map 함수와 람다식을 이용해
항목의 제곱 값을 갖는 리스트를 반환하는 프로그램을 작성하십시오.
'''
ori = list(range(1, 11))
print(list(map(lambda x:x**2, ori)))

'''6316
innerfunc)1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해
짝수만을 선택한 후, map 함수와 람다식을 이용해 항목의 제곱 값을 갖는 리스트를 반환하는
프로그램을 작성하십시오.
'''
ori = list(range(1, 11))
print(list(map(lambda x: x**2, filter(lambda x:x%2==0, ori))))

'''6317
innerfunc)가변형 인자를 전달 받아 가장 큰 값을 반환하는 함수를 정의하고,
다음과 같은 결과를 출력하는 프로그램을 작성하십시오.
'''
def maximum(*args):
    print('max{} => {}'.format(args, max(args)))
maximum(3, 5, 4, 1, 8, 10, 2)

'''6318
innerfunc)다음의 결과와 같이 'abcdef' 문자열의 각각의 문자를 키로 하고 0~5 사이의 정수를
값으로 하는 딕셔너리 객체를 생성하고, 이 딕셔너리 객체의 키와 값 정보를 출력하는
프로그램을 작성하십시오.
'''
dic = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f':5}
for k, v in dic.items():
    print("{}: {}".format(k, v))