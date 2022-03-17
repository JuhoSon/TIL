import sys
from collections import deque
sys.stdin = open('input.txt')

T = 11
for tc in range(1, T+1):
    tc = int(input())
    pw = deque(map(int, input().split()))
    minus_arr = [1, 2, 3, 4, 5]
    idx = 0
    while True:
        num = pw.popleft()
        num -= minus_arr[idx]
        if num <= 0:
            pw.append(0)
            break
        pw.append(num)
        idx = (idx + 1) % 5


    print('#{}'.format(tc), end=' ')
    print(*pw, end=' ')
    print()

