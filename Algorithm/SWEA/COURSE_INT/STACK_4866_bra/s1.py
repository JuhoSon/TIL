import sys
sys.stdin = open('input.txt')


def braket_checker(inp):
    stack = []
    for s in inp:
        if s in braket.keys():  # global reference : braket
            stack.append(s)
        else:  # elif ord(s) in braket.values():
            if len(stack) != 0:
                recent_open = stack.pop()
                if braket[recent_open] != s:
                    return 0
            else:
                return 0
    if len(stack) == 0:
        return 1
    else:
        return 0


T = int(input())
braket = {40:41, 91:93, 123:125}  # ( ) [ ] { }
for tc in range(1, T+1):
    inp = [ord(s) for s in input() if ord(s) in braket.keys() or ord(s) in braket.values()]
    print('#{} {}'.format(tc, braket_checker(inp)))

