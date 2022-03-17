import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    # 1.
    # round -> 두 번째 인자 생략되면 소수 첫째 자리 반올림
    """
    nums = list(map(int, input().split()))
    result = round(sum(nums) / len(nums))
    """

    # 2.
    my_sum = 0
    my_len = 0
    nums = list(map(int, input().split()))

    my_len = 0
    for num in nums:
        my_sum += num
        my_len += 1

    ans = round(my_sum / my_len)
    print('#{} {}'.format(tc, ans))