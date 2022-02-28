def my_cnt(digit):
    num_cnt = len(str(digit)) - 1
    min_num = 10 ** num_cnt
    if num_cnt == 0:
        return digit - (min_num - 1)
    else:
        return digit - min_num + 1  # including min_num


# N = int(input())
N = 999999999999999999
# 10의 8승(1억번)까지 1초만에 수행
# 10의 18승은 .... 
# Modulo 연산으로 해야하는데 아깝다 ...
# Time error,,, 
total_sum = 0
for n in range(N+1):
    total_sum += my_cnt(n)
print(total_sum)