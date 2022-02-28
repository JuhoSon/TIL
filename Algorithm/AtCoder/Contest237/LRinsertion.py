from collections import deque

N = int(input())
S = input()
S_num = [num for num in range(1, len(S)+1)]
A = [0]

for idx, direction in enumerate(S):
    pre_num_idx = A.index(S_num[idx]-1)
    
    if direction == 'L':
        if pre_num_idx == 0:
            STACK_RANGE = len(A)
        else:
            STACK_RANGE = len(A) - (pre_num_idx)
    else:
        STACK_RANGE = len(A) - (pre_num_idx + 1)
    
    stack = []
    for _ in range(STACK_RANGE):
        s = A.pop()
        stack.append(s)
    
    A.append(S_num[idx])

    for _ in range(STACK_RANGE):
        s = stack.pop()
        A.append(s)
    
print(*A)