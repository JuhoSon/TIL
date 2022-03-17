def bubble_sort(arr):
    # len(arr)이 아닌 len(arr)-1인 이유는 j+1에서 index error를 막기 위함
    for i in range(len(arr)-1, 0, -1): # 정렬 구간의 끝
        for j in range(i):             # 비교 할 왼쪽 원소
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 정렬 -> 최대 - 최소
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(numbers)
    bubble_sort(numbers)
    print(numbers)