import math

s = ['  *   ', ' * *  ', '***** ']


def makeStar(shift):
    c = len(s)
    for i in range(c):
        s.append(s[i] + s[i])  # 현 단계 삼각형을 뒤에 붙이고
        s[i] = ('   ' * shift + s[i] + '   ' * shift)


N = int(input())
k = int(math.log(int(N/3), 2))
for i in range(k):
    makeStar(int(pow(2, i)))
for i in range(N):
    print(s[i])
