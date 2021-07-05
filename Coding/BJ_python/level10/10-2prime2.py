start_num = int(input())
finish_num = int(input())
input_list = list(range(start_num, finish_num+1))
input_set = set(input_list)
result_set = set()
for i in input_list:
    div_num = 2
    while div_num < i:
        if i % div_num == 0:
            result_set.add(i)
            break
        div_num += 1
decimal_set = input_set - result_set - {1}
if len(decimal_set) == 0:
    print(-1)
else:
    print(sum(decimal_set))
    print(min(decimal_set))
