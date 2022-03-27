import sys
sys.stdin = open('input.txt')


def get_b(inp_f):
    times = -1
    result = '0.'
    while inp_f:
        b = 2 ** (times)
        if b <= inp_f:
            inp_f -= b
            result += '1'
        else:
            result += '0'
        times -= 1

        if len(result) >= 15:
            return 'overflow'
    return result[2:]


T = int(input())
for tc in range(1, T + 1):
    inp_f = float(input())
    result = get_b(inp_f)
    print(f'#{tc} {result}')