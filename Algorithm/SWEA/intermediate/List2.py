'''4836 색칠하기
그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.
N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.
주어진 정보에서 같은 색인 영역은 겹치지 않는다.
예를 들어 2개의 색칠 영역을 갖는 위 그림에 대한 색칠 정보이다.
2
2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )
3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )
다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )
color = 1 (빨강), color = 2 (파랑)
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
# <기본생각> 0으로 채워진 보드에 1, 2, 3의 색 칠하기.
T = int(input())  # 테스트 케이스 개수
for _ in range(T):
    board = [["0" for _ in range(10)] for __ in range(10)]  # 보드 초기화
    N = int(input())  # 색 개수 초기화
    common_flag = '0'  # 공통영역 초기화
    for __ in range(N):
        row_start, col_start, row_end, col_end, color = list(map(int, input().split()))
        for r in range(row_start, row_end+1):  # 보드 업데이트
            for c in range(col_start, col_end+1):
                if str(color) not in board[r][c]:  # 같은 색인 영역은 겹치지 않는다.
                    board[r][c] += str(color)
        if str(color) not in common_flag:  # 공통영역 업데이트
            common_flag += str(color)
    common_cnt = sum([sum([1 for c in range(10) if board[r][c] == common_flag]) for r in range(10)])
    print('#{} {}'.format(_+1, common_cnt))
# 왜안돼 ㅠ

T = int(input())  # 테스트 케이스 개수
for _ in range(T):
    board = [[0 for _ in range(10)] for __ in range(10)]  # 보드 초기화
    N = int(input())  # 색 개수 초기화
    for __ in range(N):
        row_start, col_start, row_end, col_end, color = list(map(int, input().split()))
        for r in range(row_start, row_end+1):  # 보드 업데이트
            for c in range(col_start, col_end+1):
                board[r][c] += color
    common_cnt = sum([sum([1 for c in range(10) if board[r][c] == 3]) for r in range(10)])
    print('#{} {}'.format(_+1, common_cnt))
# 같은색 겹치는거, ...

'''4837 부분집합의 합
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
# <기본생각> 부분집합 다 만들고 K맞는거 찾기
# 아~ 멱집합 만드는게 어렵구나 ㅎ ; 
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
A_power = [[A[i] for i in range(len(A)) if switch&(1<<i)] for switch in range(1<<12)]  # 1<<12 = 2**12

T = int(input())  # 테스트 케이스 수
for _ in range(T):
    N, K = map(int, input().split())  # 원소의 수, 부분집합의 합
    A_power_nk = [i for i in A_power if len(i)==N and sum(i)==K]
    print('#{} {}'.format(_ + 1, len(A_power_nk)))
    
'''4839 이진탐색
코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.
짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.
예를 들어 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 중간 페이지 c= int((l+r)/2)로 계산한다.
찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.
A는 300, B는 50 쪽을 찾아야 하는 경우, 다음처럼 중간 페이지를 기준으로 왼쪽 또는 오른 쪽 영역의 중간 페이지를 다시 찾아가면 된다.
책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때, 이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하시오. 비긴 경우는 0을 출력한다.
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
테스트 케이스 별로 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1<= P, Pa, Pb <=1000
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, A, B, 0 중 하나를 출력한다.
'''
# <기본생각> A, B의 카운트를 세아려 낮은 쪽이 승리
def cnt(left, right, page):
    l, r = left, right
    c = int((l+r)/2)
    cnt = 1
    while True:
        if page > c:
            l = c
            c = int((l+r)/2)
        elif page < c:
            r = c
            c = int((l+r)/2)
        else:
            break
        cnt += 1
    return cnt

T = int(input())  # 테스트 케이스 수
for _ in range(T):
    P, Pa, Pb = map(int, input().split())  # 전체 쪽수, A가 찾을 쪽수, B가 찾을 쪽수
    Acnt, Bcnt = cnt(1, P, Pa), cnt(1, P, Pb)
    if Acnt < Bcnt:
        print('#{} {}'.format(_ + 1, 'A'))
    elif Acnt > Bcnt:
        print('#{} {}'.format(_ + 1, 'B'))
    else:
        print('#{} {}'.format(_ + 1, 0))

'''4843 특별한 정렬
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
10 1 9 2 8 3 7 4 6 5
주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다.
'''
# <기본생각> 
T = int(input())  # test case num
for _ in range(T):
    N = int(input())  # int num 안쓸듯
    ai = list(map(int, input().split()))  # 정수들
    result = []
    for __ in range(int(len(ai)/2)+1):
        try:  # 홀수인 경우 고려
            result.append(ai.pop(ai.index(max(ai))))
            result.append(ai.pop(ai.index(min(ai))))
        except:  # 짝수인 경우 인덱스에러 (이미 정렬은 끝난 상황)
            pass
    print('#{} {}'.format(_ + 1, ' '.join(map(str, result[:10]))))