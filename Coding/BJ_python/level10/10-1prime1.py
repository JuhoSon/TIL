userless = int(input())
input_list = list(map(int, input().split()))
input_set = set(input_list)
result_set = set()
for i in input_list:
    div_num = 2
    while div_num < i:
        if i % div_num == 0:
            result_set.add(i)
            break
        div_num += 1
print(len(input_set-result_set-{1}))
