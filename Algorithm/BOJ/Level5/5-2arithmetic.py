def f_sub_seq(chiper_list):
    test_set = set()
    for i in range(len(chiper_list)-1):
        test_set.add(chiper_list[i] - chiper_list[i+1])
    if len(chiper_list) == 1:
        return True
    elif len(test_set) == 1:
        return True


def f_chiper_list(do_num):
    chiper_list = []
    for i in range(len(str(do_num))):
        chiper_list.append(do_num % 10)
        do_num //= 10
    return chiper_list


user_input = int(input())
do_list = list(range(1, user_input+1))
result_list = []
for i in do_list:
    chiper_list = f_chiper_list(i)
    if f_sub_seq(chiper_list) is True:
        result_list.append(i)
print(len(result_list))
