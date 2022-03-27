import sys
sys.stdin = open('input.txt')


def oven(q):
    pointer = 0
    baking = q[:N]  # length N of circular queue
    q = q[N:]  # N <= M
    P_IDX = 0  # pizza index
    C_IDX = 1  # cheeze amount
    while q or sum([1 for c in baking if c[C_IDX] > 0]) > 1:
        # cheeze 0 -> new pizza input
        if not baking[pointer][C_IDX] and q:
            baking[pointer] = q.pop(0)
        # next round calculate
        baking[pointer][C_IDX] //= 2
        # pointer update
        pointer = (pointer + 1) % N

    last = max(baking, key=lambda x: x[C_IDX])[P_IDX]
    return last


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # size N, pizza cnt M
    q = list(map(list, enumerate(map(int, input().split()), start=1)))  # cheeze amount, length M
    result = oven(q)
    print('#{} {}'.format(tc, result))