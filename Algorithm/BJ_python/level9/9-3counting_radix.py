# result = [input() for cycle_time in int(input())]
#
# max_len = max(list(map(len, result)))
# for i in range(max_len):
#     n_list = []
#     que = []
#     for j in result:
#         n_list.append(j[i])
#     make_que_temp = list(n_list)
#     for k in range(len(n_list)):
#         que.append(min(make_que_temp))
#         make_que_temp.pop(min(make_que_temp))
#     # n의자리 기반으로 result 정렬.
#     for n_times in n_list:
#         for que_times in que:
#             if n_times == que_times:
# 
# i = [1, 2, 3]
# j = [1, 5, 6]
# for first in i:
#     for second in j:
#         if first == second:
#             print(i.index(second))


def list_to_buckets(a, base, iteration):
    buckets = [[] for x in range(base)]
    for x in a:
        digit = (x // (base ** iteration)) % base
        buckets[digit].append(x)
    return buckets


def buckets_to_list(buckets):
    a = []
    for bucket in buckets:
        for x in bucket:
            a.append(x)
    return a


def radix_sort(a, base=10):
    maxval = max(a)
    it = 0
    while base ** it <= maxval:
        a = buckets_to_list(list_to_buckets(a, base, it))
        it += 1
    return a
