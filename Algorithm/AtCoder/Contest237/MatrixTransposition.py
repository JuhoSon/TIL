row, col = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(row)]
for row in list(zip(*arr)):
    print(*row)