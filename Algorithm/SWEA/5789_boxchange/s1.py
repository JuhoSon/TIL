import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    lr = {i+1:tuple(map(lambda x: int(x) - 1, input().split())) for i in range(Q)}
    box = [0 for _ in range(N)]
    for i, (l, r) in lr.items():
        for idx in range(l, r+1):
            box[idx] = i

    print('#{}'.format(tc), *box)

