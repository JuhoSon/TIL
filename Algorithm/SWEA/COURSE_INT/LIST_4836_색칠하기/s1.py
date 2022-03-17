import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    boxes = [[0] * 10 for _ in range(10)]
    n = int(input())
    cnt = 0
    for k in range(n):          # 색칠
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                boxes[i][j] += color

    for i in range(10):         # 겹쳐진 칸수 카운팅 -> 3이면 겹쳐진 영역
        for j in range(10):
            if boxes[i][j] == 3:
                cnt += 1

    print('#{} {}'.format(tc, cnt))