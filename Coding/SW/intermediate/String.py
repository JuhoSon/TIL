'''4864 문자열 비교
두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.
예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.
ABC
ZZZZZABCZZZZZ
두번째 문자열에 첫번째 문자열과 일치하는 부분이 있으므로 1을 출력.
ABC
ZZZZAZBCZZZZZ
문자열이 일치하지 않으므로 0을 출력.
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  (1≤T≤50)
다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어집니다. (5≤N≤100, 10≤M≤1000, N≤M)
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
# <기본생각> 보이어무어 알고리즘 사용
T = int(input())
for _ in range(T):
    need = input()
    total = input()
    if total.find(need)>=1:
        print('#{} {}'.format(_+1, 1))
    else:
        print('#{} {}'.format(_+1, 0))

'''4861 회문
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다. 
예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
# <기본생각> reversed로 검사 
T = int(input())  # 테스트 케이스 수
for _ in range(T):
    N, M = map(int, input().split())  # N*N 행렬, 회문길이는 M
    matrix = [input() for _ in range(N)]  # 가로 확인
    matrix2 = [''.join(col) for col in zip(*matrix)]  # 세로 확인
    row_result = [row[i:i+M] for row in matrix 
                    for i in range(len(row)-(M-1)) 
                    if row[i:i+M]==''.join(list(reversed(row[i:i+M])))]
    col_result = [col[i:i+M] for col in matrix2 
                    for i in range(len(col)-(M-1))
                    if col[i:i+M]==''.join(list(reversed(col[i:i+M])))]
    if len(row_result) == 1:
        print('#{} {}'.format(_+1, row_result[0]))
    elif len(col_result) == 1:
        print('#{} {}'.format(_+1, col_result[0]))

'''4865 글자 수
두 개의 문자열 str1과 str2가 주어진다. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.
예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우, str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.
파이썬의 경우 딕셔너리를 이용할 수 있다.
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어진다. 5≤N≤100, 10≤M≤1000, N≤M
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
# <기본생각> 그냥 세자!
T = int(input())  # 테스트 케이스 수
for _ in range(T):
    str1 = input()  # 길이 N
    str2 = input()  # 길이 M
    # 글자 수 카운트
    dic = {s:0 for s in str1}
    for s in str2:
        try:
            dic[s] += 1
        except:
            pass
    # value 높은거 출력
    max_s = list(sorted(dic.items(), key = lambda x: x[1], reverse=True))[0]  # 제일 높은거
    print('#{} {}'.format(_+1, max_s[1]))

