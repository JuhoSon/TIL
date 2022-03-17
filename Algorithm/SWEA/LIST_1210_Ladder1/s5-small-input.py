def solve(r, c):
    while r > 0:                                 # 가장 위로 올라왔을 때 종료
        data[r][c] = 0                           # 방문 표시
        for i in range(3):                       # 좌우부터 이동가능 확인 이후 위로 이동
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nc < 10 and 0 <= nr < 10:    # 이동 가능 확인
                if data[nr][nc]:                 # 방문 여부 확인
                    r, c = nr, nc
                    break
    return c

import sys
sys.stdin = open('small_input.txt')
for _ in range(1):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(10)]
    dr = [0, 0, -1]                              # 우 좌 상 -> 왼쪽 오른쪽 살피고 위로 올라가자!
    dc = [1, -1, 0]

    r, c = 9, data[9].index(2)                   # 도착 지점 부터 출발
    ans = solve(r, c)
    print('hello world')
    print('hello world')
    print('hello world')
    print("#{} {}".format(tc, ans))