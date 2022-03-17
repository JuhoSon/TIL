import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    inp = input()
    stack = ['nobody']
    for s in inp:
        if stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
    print('#{} {}'.format(tc, len(stack)-1))

