user_input = input().lower()

result_dict = dict()
index = 0
for i in user_input:
    try:
        result_dict[i] += 1
    except:
        result_dict[i] = 1

target_value = max(result_dict.values())
target_list = []
for keys, values in result_dict.items():
    if values == target_value:
        target_list.append(keys)
if len(target_list) == 1:
    print(''.join(target_list).upper())
else:
    print('?')
