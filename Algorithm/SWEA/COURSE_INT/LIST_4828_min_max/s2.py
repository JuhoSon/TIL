import sys
sys.stdin = open('input.txt')
T = int(input())

#2. 정렬
def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    bubble_sort(numbers)
    ans = numbers[N-1] - numbers[0]
    print('#{} {}'.format(tc, ans))