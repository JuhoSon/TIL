import sys
sys.stdin = open('input_sample.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # init
    max_price = max(arr)
    max_date = arr.index(max_price)
    bulk = []
    money = 0

    for date, price in enumerate(arr):
        if date == max_date:  # sell
            for sell_price in bulk:
                money += (max_price - sell_price)
            bulk = []
            for init_date in range(date+1):
                arr[init_date] = 0
            if date < len(arr):  # update max
                max_price = max(arr)
                max_date = arr.index(max_price)
        elif date < max_date:
            bulk.append(price)
    print('#{} {}'.format(tc, money))
