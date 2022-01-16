'''4828 minmax
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
[입력]
첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
test_cnt = int(input())
for case in range(test_cnt):
    N = int(input())  # 다른 언어에서 리스트 크기 정할 때 사용
    test_list = list(map(int, input().split()))
    print('#{} {}'.format(case + 1, max(test_list) - min(test_list)))

'''4831 전기버스
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
[입력]
첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )
[출력]
#과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.
'''
# <기본 아이디어 낙서장>
# N을 루프도는동안 충전Flag=k로 지정해놓고 루프돌때마다 -1씩.
# 충전Flag 0보다 작아지면(음수가되면) break; return 0
# 현재위치 + 충전Flag에서 가장 멀리있는 charge_num에서 충전하기
T = int(input())  # 노선수
for line in range(T):
    K, N, M = map(int, input().split())  # 최대이동가능 수, 정류장 수, (충전기개수. 그저거들뿐)
    charge_num = list(map(int, input().split()))

    # 첫 정류소에서 충전해서 출발~ (카운트 포함X:문제조건)
    charge_cnt = 0
    charge_flag = K
    for n in range(N+1):  # 0부터 N번정류장까지
        # 어디서 충전할지 정하기 (현재위치 + 충전Flag고려해서 최대한 멀리 있는 충전소 선택)
        charge_idx = max(
            list(filter(lambda x: x[1]<=0, {k:k-(n + charge_flag) for k in charge_num}.items())),
            key=lambda x: x[1])[0]
        if n == charge_idx:
            if (N - (n + charge_flag) <= 0): # 충전할 때지만, 안하고 종점갈 수 있을 때
                pass
            else:
                charge_flag = K  # 충전~
                charge_cnt += 1
        
        # 다음 정류소로 출발~ 전! 전기가 없다!
        if charge_flag < 0:
            charge_cnt = 0
            break
        # 다음 정류소로 출발~
        charge_flag -= 1

    print('#{} {}'.format(line+1, charge_cnt))

'''4834 숫자 카드
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 ) 
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.
'''
# <기본생각> 카드 숫자 세아려서 key, value 출력하면 끝!
T = int(input())  # 테스트 케이스 수
for _ in range(T):
    N = int(input())  # 카드 장수 (필요없어!)
    num = input()
    # 카운트~
    dic = {int(k):0 for k in num}
    for k in num:
        dic[int(k)] += 1
    fir_sort = list(sorted(dic.items(), key = lambda x: x[1], reverse=True))  # value기준 정렬
    sec_sort = list(filter(lambda x: x[1]==fir_sort[0][1], fir_sort))  # value높은값만 남기고
    result = list(sorted(sec_sort, key = lambda x: x[0], reverse=True))[0]  # key 기준 정렬
    print('#{} {} {}'.format(_ + 1, result[0], result[1]))

'''4835 구간합
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
다음은 N=5, M=3이고 5개의 숫자 1 2 3 4 5가 배열 v에 들어있는 경우이다.
이웃한 M개의 합이 가장 작은 경우 1 + 2 + 3 = 6
이웃한 M개의 합이 가장 큰 경우 3 + 4 + 5 = 12
답은 12와 6의 차인 6을 출력한다.
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
# <기본 생각> brute force하게, 모든 M구간의 정수합을 모두 구해서 min, max 가져오기

T = int(input())  # 테스트 케이스 개수
for _ in range(T):
    N_cnt, M = map(int, input().split())  # (정수의 개수.안씀), 구간의 개수
    N = list(map(int, input().split()))

    minmax_list = []
    for i in range(len(N)-M+1):
        minmax_list.append(sum(N[i:i+M]))
    print('#{} {}'.format(_ + 1, max(minmax_list) - min(minmax_list)))

