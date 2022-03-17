import sys
sys.stdin = open('input.txt')


male = lambda s, n: [_ if (idx+1) % n != 0 else int(not _) for idx, _ in enumerate(s)]


def fema(s, n):
    n -= 1
    slice = 0
    while (n-slice >= 0) and (n+slice <= len(s)-1) and (s[n-slice] == s[n+slice]):
        slice += 1
    slice -= 1
    for idx in range(n-slice, n+slice + 1):
        s[idx] = int(not s[idx])
    return s


switch = {1:male, 2:fema}

T = 1
for tc in range(1, T+1):
    size = int(input())
    status = list(map(int, input().split()))
    student_num = int(input())
    students = [list(map(int, input().split())) for _ in range(student_num)]

    for gender, num in students:
        status = switch[gender](status, num)

    # for print
    if len(status) <= 20:
        print(*status)
    else:
        row = []
        for s in status:
            row.append(s)
            if len(row) == 20:
                print(*row)
                row = []
        if len(row) > 0:
            print(*row)