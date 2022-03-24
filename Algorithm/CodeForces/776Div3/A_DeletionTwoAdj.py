import sys
sys.stdin = open('A_DeletionTwoAdj.txt')


def del_adj(s):
    while len(s) > 1:
        if s[0] == c:
            return 'YES'
        else:
            s = s[2:]
    if s == c:
        return 'YES'
    else:
        return 'NO'

T = int(input())
for tc in range(1, T + 1):
    s = input()  # odd length
    c = input()

    print(del_adj(s))