# https://www.cs.miami.edu/home/burt/learning/Csc517.091/workbook/countingsort.html
def counting_sort(arr: list, N: int):
    #1.
    # 카운팅하기 위한 배열 초기화
    counter = [0] * (max(arr)+1) # 최댓값 +1 (인덱스)
    result = [0] * N             # 배열 크기

    #2.
    # arr 안에 들어있는 숫자의 개수 카운팅
    for i in arr:
        counter[i] += 1

    #3.
    # 누적값 카운팅
    for i in range(1, len(counter)):
        counter[i] += counter[i-1]

    #4.
    # 기존 배열의 가장 뒤에 있는 원소(len(arr)-1)부터 시작해서
    # 정렬될 결과를 저장할 배열(result)에 쌓아가자
    for i in range(len(arr)-1, -1, -1):
        result[counter[arr[i]]-1] = arr[i]  # 위치 찾기
        counter[arr[i]] -= 1                # 같은 숫자가 왔을 때 더 하나 더 작은 위치에 놓이게 하기 위함!

    return result

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    N = len(numbers)
    print(numbers)
    sorted_numbers = counting_sort(numbers, N)
    print(sorted_numbers)