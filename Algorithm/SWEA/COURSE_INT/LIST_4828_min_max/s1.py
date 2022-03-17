import sys
sys.stdin = open('input.txt')
T = int(input())

#1-1. 반복문
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    # max_num = min_num = nums[0]
    max_num = nums[0]     # 초깃값 설정
    min_num = nums[0]

    for num in nums:      # 최대 & 최소 연산
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    ans = max_num - min_num
    print('#{} {}'.format(tc, ans))

#1-2. 반복문2
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    min_value = 987654321           # 최대 & 최소 초기화
    max_value = 0

    for i in range(N):              # 길이만큼 반복하면 최대 & 최소
        if max_value < numbers[i]:
            max_value = numbers[i]

        if min_value > numbers[i]:
            min_value = numbers[i]
    ans = max_value - min_value
    print('#{} {}'.format(tc, ans))