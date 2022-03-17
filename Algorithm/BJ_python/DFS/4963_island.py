import sys
sys.stdin = open('4963_island.txt')


dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [1, 1, 1, 0, -1, -1, -1, 0]


while True:
    # BJ input
    inp = input()
    if inp == '0 0':
        break
    w, h = map(int, inp.split())
    maps_arr = [list(map(int, input().split())) for _ in range(h)]
    maps = {(x, y):island for x, row in enumerate(maps_arr) for y, island in enumerate(row)}
    visited = {(x, y): False for x in range(h) for y in range(w)}

    # maps loop
    island_cnt = 0  # result
    for x in range(h):
        for y in range(w):
            island = maps[(x, y)]

            # delta loop
            stack = []
            if island:
                stack.append((x, y))
                maps[(x, y)] = 0  # update
                visited[(x, y)] = True
                island_cnt += 1
            while stack:
                pop_x, pop_y = stack.pop()
                for delta_idx in range(8):
                    delta_x = dx[delta_idx]
                    delta_y = dy[delta_idx]
                    new_x = pop_x + delta_x
                    new_y = pop_y + delta_y
                    if 0 <= new_x < h and 0 <= new_y < w and maps[(new_x, new_y)] and not visited[(new_x, new_y)]:
                    # index를 벗어나지 않고, 섬이 있으며, 방문하지 않은 곳
                        stack.append((new_x, new_y))
                        maps[(new_x, new_y)] = 0
                        visited[(new_x, new_y)] = True
    print(island_cnt)