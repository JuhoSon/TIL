import sys
sys.stdin = open('input.txt')


x2d = {  # hexadecimal to decimal
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def d2b(d):
    b = ''
    while d:
        b += str(d % 2)
        d //= 2
    return b[::-1].zfill(4)


T = int(input())
for tc in range(1, T + 1):
    length, inp = input().split()
    result = ''.join([d2b(x2d[_]) for _ in inp])
    print(f'#{tc} {result}')