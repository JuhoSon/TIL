def check_pattern(pattern: list, M: int, PI: list):
    """
    Pattern 문자열 전처리
    -> PI 배열에 pattern을 기록하기 위한 함수
    """
    i, j = 0, -1                                    # 인덱스 초기화 (-1인 이유는 밑에서 0으로 설정하기 위함)
    PI[0] = -1                                      # 0으로 초기화하면 무한루프
    while i < M:                                    # M(패턴의 길이)이 i보다 큰 동안
        while j > -1 and pattern[i] != pattern[j]:
            j = PI[j]
        i += 1
        j += 1
        PI[i] = j

def KMP(target: list, N: int, pattern: list, M: int, PI: list):
    i, j = 0, 0
    pos = -1
    while i < N:
        while j >= 0 and target[i] != pattern[j]:
            j = PI[j]
        i += 1
        j += 1
        if j == M:
            pos = i - j
            break
    return pos

import sys
sys.stdin = open('input.txt')
target = input()                        # target 문자열
pattern = input()                       # pattern 문자열
N = len(target)
M = len(pattern)
PI = [0] * (M+1)                        # pattern 문자열의 길이만큼 패턴을 체크 할 배열 생성

check_pattern(pattern, M, PI)
print(PI)
ans = KMP(target, N, pattern, M, PI)
print(ans)

# http://whocouldthat.be/visualizing-string-matching/