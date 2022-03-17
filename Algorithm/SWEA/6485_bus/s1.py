import sys
sys.stdin = open('input.txt')

T = int(input())  # 1
for tc in range(1, T+1):
    N = int(input())  # 2
    ab_dic = dict()
    for i in range(N):
        ab_dic[i] = tuple(map(lambda x: int(x) - 1, input().split()))  # 1 3, 2 5
    bus = {idx: set() for idx in range(5000)}  # 5
    P = int(input())
    C = [int(input())-1 for _ in range(P)]  # 1 2 3 4 5
    for i, (a, b) in ab_dic.items():
        for idx in range(a, b+1):
            bus[idx].add(i)

    result = list(map(len, [bus[c_idx] for c_idx in C]))
    print('#{}'.format(tc), end=' ')
    print(*result)
