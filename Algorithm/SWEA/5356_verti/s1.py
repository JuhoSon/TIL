import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    raw_inp = [list(input()) for _ in range(5)]
    max_len = max(map(len, raw_inp))
    pad_inp = [line + [''] * (max_len - len(line)) for line in raw_inp]

    pad_inp_T = list(zip(*pad_inp))
    result = ''.join([''.join(line) for line in pad_inp_T])
    print('#{} {}'.format(tc, result))

