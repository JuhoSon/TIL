import sys
sys.stdin = open('input.txt')


def calculate(x, y, string):
    if string == '*':
        return x * y
    elif string == '/':
        return x / y
    elif string == '-':
        return x - y
    elif string == '+':
        return x + y


def post_cal(node):
    if node:
        x = post_cal(tree[node][1])
        y = post_cal(tree[node][2])
        val = tree[node][0]
        if type(val) == int:
            return val
        result = calculate(x, y, val)
        return result


T = 10
for tc in range(1, T+1):
    V = int(input())
    tree = [[0, 0, 0] for _ in range(V + 1)]  # zero padding, format : [num, left child index, right child index]
    for _ in range(V):
        inp = input().split()
        P_IDX = int(inp[0])
        inp = inp[1:]
        if len(inp) == 3:  # calculator
            cal = inp[0]
            LC_IDX = int(inp[1])  # left child index
            RC_IDX = int(inp[2])  # right child index
            tree[P_IDX] = [cal, LC_IDX, RC_IDX]
        else:  # leaf num
            num = int(inp[0])
            tree[P_IDX][0] = num

    r = int(post_cal(1))


    print('#{} {}'.format(tc, r))

