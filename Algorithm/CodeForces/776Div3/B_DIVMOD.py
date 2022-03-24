import sys
sys.stdin = open('B_DIVMOD.txt')


def func(x):
    rnd_num = x // divisor
    mod_num = x % divisor
    return rnd_num + mod_num


T = int(input())
for tc in range(1, T + 1):
    lower_bnd, upper_bnd, divisor = map(int, input().split())
    remainder = upper_bnd % divisor
    new_lower_bnd = (upper_bnd - remainder) - 1
    if new_lower_bnd > lower_bnd:
        # 하한을 높여주는 방법으로 연산을 최대 10억번에서 1번까지 줄일수있다.
        # 상한에 가까운 나누어 떨어지는 지점의 바로 1개 전 시점이 f의 값이 가장 높을때다.
        lower_bnd = new_lower_bnd
    nums = [func(num) for num in range(lower_bnd, upper_bnd + 1)]
    print(max(nums))