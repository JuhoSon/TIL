import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    laser_pol = input().replace('()', 'R')
    pol_stack = 0
    pol_cut = 0

    for idx, p in enumerate(laser_pol):
        if p == '(':
            pol_stack += 1
        elif p == 'R':  # cutting of whole pol
            for stack in range(pol_stack):
                pol_cut += 1
        elif p == ')':  # end of just one pol
            pol_stack -= 1
            pol_cut += 1
    print('#{} {}'.format(tc, pol_cut))
