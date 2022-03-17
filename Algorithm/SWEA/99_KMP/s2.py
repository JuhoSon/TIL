# 교재

def KMP(target: str, pattern: str):
    #1. 전처리 과정
    N = len(target)                                 # 타겟 문자열의 길이
    M = len(pattern)                                # 패턴 문자열의 길이
    lps = [0] * (M+1)                               # 패턴을 저장 할 배열

    j = 0                                           # preprocessing -> 일치한 개수 -> 패턴 내에서 비교할 인덱스 위치
    lps[0] = -1                                     # 시작 지점 초기화

    for i in range(1, M):
        lps[i] = j                                  # p[i]이전에 일치한 개수
        if p[i] == p[j]:                            # 일치하면
            j += 1                                  # j 증가 (다음 for에서 i 증가) 
        else:                                       # 일치하지 않으면
            j = 0                                   # j는 0으로 초기화
    lps[M] = j                                      

    #2. 패턴 문자 탐색 과정
    i = 0                                           # target text를 컨트롤 하는 인덱스
    j = 0                                           # pattern text를 컨트롤 하는 인덱스
    while i < N and j <= M:
        if j == -1 or target[i] == pattern[j]:       # pattern의 첫 글자이거나 글자가 일치한다면
            i += 1                                  # target & pattern을 체크하는 인덱스를 하나씩 올려가자
            j += 1
        else:                                       # 불일치하는 경우
            j = lps[j]                              # j가 0인 경우(처음 불일치가 일어난 경우) -> -1 (비교를 다시 시작해야 하는 부분의 인덱스로 갱신)

        if j == M:                                  # 패턴을 찾은 경우 (패턴이 일치한 경우 패턴의 전체 길이인 M의 길이와 같다.)
            print(i-M, end=' ')                     # 일치 했을 때의 위치(i)에서 패턴의 길이(M)를 빼면 패턴이 일치한 시작 위치를 가져올 수 있음
            j = lps[j]                              # (패턴이 중복되는 경우) 다음 패턴을 찾기 위해서 어디부터 시작하면 되는지를 체크하기 위함
    print()


t = 'AABAABAAAABAABDAABAABAC'
p = 'AABAABAC'
KMP(t, p)
# 15 -> 15번째 인덱스에서 패턴 일치 시작
print('#############################################')


t = 'zzzabcdabcdabcefabcd'
p = 'abcdabcef'
KMP(t, p)
# 7 -> 7번째 인덱스에서 패턴 일치 시작
print('#############################################')


t = 'AABAACAADAABAABA'
p = 'AABA'
KMP(t, p)
# 0 9 12 -> 0/9/12에서 인덱스에서 패턴 일치 시작(3개의 패턴 일치)
print('#############################################')


t = "AAAAABAAABA"
p = "AAAA"
KMP(t, p)
# 0 1 -> 0/1에서 인덱스에서 패턴 일치 시작(2개의 패턴 일치)
print('#############################################')

t = "AAAAABAAABA"
p = "AA"
# 0 1 2 3 6 7  -> 0/1/2/3/6/7에서 인덱스에서 패턴 일치 시작(6개의 패턴 일치)
KMP(t, p)
