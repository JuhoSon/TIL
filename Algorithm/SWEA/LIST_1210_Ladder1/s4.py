import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    dr = [0, 0, -1]
    dc = [1, -1, 0]                              # 우 좌 상

    r, c = 99, data[99].index(2)                 # 도착 지점 부터 출발
    while r > 0:                                 # 가장 위로 올라왔을 때 종료
        data[r][c] = 0                           # 방문 표시
        for i in range(3):                       # 좌우부터 이동가능 확인 이후 위로 이동
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nc < 100 and 0 <= nr < 100:  # 이동 가능 확인
                if data[nr][nc]:                 # 방문 여부 확인
                    r, c = nr, nc
                    break
    print("#{} {}".format(tc, c))