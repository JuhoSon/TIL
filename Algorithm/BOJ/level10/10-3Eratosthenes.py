start_num, finish_num = map(int, input().split())

# # Bad coding
# input_list = list(range(start_num, finish_num+1))
# input_set = set(input_list)
# result_set = set()
# for i in input_list:
#     # div_num = 2
#     # while div_num < i:
#     #     if i % div_num == 0:
#     #         result_set.add(i)
#     #         break
#     #     div_num += 1
#     if i != 1:
#         for div_num in range(2, i):
#             if i % div_num == 0:
#                 result_set.add(i)
# decimal_set = input_set - result_set - {1}
# for ele in decimal_set:
#     print(ele)

seive = [False, False] + [True] * (finish_num - 1)
for k in range(2, int(finish_num ** 0.5 + 1.5)):
    if seive[k]:
        seive[k*2::k] = [False] * ((finish_num - k) // k)
prime_list = [x for x in range(finish_num+1) if seive[x]
              and x >= start_num and x <= finish_num]
for i in prime_list:
    print(i)
