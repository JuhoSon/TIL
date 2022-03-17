import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pascal = []
    for n in range(N):
        pascal.append([])

        pascal[n].append(1)  # first 1
        for sum_idx in range(1, n):  # sum of n-1 row's values
            summation = pascal[n-1][sum_idx-1] + pascal[n-1][sum_idx]
            pascal[n].append(summation)
        if n != 0:
            pascal[n].append(1)  # end 1

    print('#{}'.format(tc))
    for row in pascal:
        print(*row)

