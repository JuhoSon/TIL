directions = {
    True: {
        'R': 'D',
        'D': 'L',
        'L': 'U',
        'U': 'R',
    },
    False: {
        'L': 'D',
        'D': 'R',
        'R': 'U',
        'U': 'L',
    }
}
next = lambda dir, val: val + 1 if dir in 'RD' else val -1


def solution(n, clockwise):
    direction = directions[clockwise]  # next step direction
    answer = [[0 for _ in range(n)] for __ in range(n)]  # init
    init_cnt = n * n
    if clockwise:
        left_top = {'R': [0, 0]}
        right_top = {'D': [0, n-1]}
        left_bottom = {'U': [n-1, 0]}
        right_bottom = {'L': [n-1, n-1]}
    else:
        left_top = {'D': [0, 0]}
        right_top = {'L': [0, n-1]}
        left_bottom = {'R': [n-1, 0]}
        right_bottom = {'U': [n-1, n-1]}
    start_num = 1
    positions = [left_top, right_top, left_bottom, right_bottom]

    # fill matrix
    while init_cnt > 0:
        for idx, dir_position in enumerate(positions):
            dir, position = [(k, v) for k, v in dir_position.items()][0]
            # fill
            x = position[0]
            y = position[1]
            answer[x][y] = start_num
            init_cnt -= 1
            
            # update direction, position
            if dir == 'D':
                new_x = x + 1
                if new_x < n and answer[new_x][y] == 0:
                    new_dir = dir
                    new_position = [new_x, y]
                elif new_x < n and answer[new_x][y] != 0:
                    new_dir = direction[dir]
                    new_y = next(new_dir, y)
                    new_position = [x, new_y]
                positions[idx] = {new_dir: new_position}
                
            elif dir == 'R':
                new_y = y + 1
                if new_y < n and answer[x][new_y] == 0:
                    new_dir = dir
                    new_position = [x, new_y]
                elif new_y < n and answer[x][new_y] != 0:
                    new_dir = direction[dir]
                    new_x = next(new_dir, x)
                    new_position = [new_x, y]
                positions[idx] = {new_dir: new_position}

            elif dir == 'U':
                new_x = x - 1
                if new_x >= 0 and answer[new_x][y] == 0:
                    new_dir = dir
                    new_position = [new_x, y]
                elif new_x >= 0 and answer[new_x][y] != 0:
                    new_dir = direction[dir]
                    new_y = new_y = next(new_dir, y)
                    new_position = [x, new_y]
                positions[idx] = {new_dir: new_position}

            elif dir == 'L':
                new_y = y -1
                if new_y >= 0 and answer[x][new_y] == 0:
                    new_dir = dir
                    new_position = [x, new_y]
                elif new_y >= 0 and answer[x][new_y] != 0:
                    new_dir = direction[dir]
                    new_x = new_y = next(new_dir, x)
                    new_position = [new_x, y]
                positions[idx] = {new_dir: new_position}
        start_num += 1
    return answer

