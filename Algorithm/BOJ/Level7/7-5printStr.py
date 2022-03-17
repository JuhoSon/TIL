N = int(input())
count = 0
for times in range(N):
    user_input = input()
    check_list = []
    i = 0
    j = 1
    while True:
        if len(user_input) == 1 or j >= len(user_input):
            count += 1
            break
        pre = user_input[i]
        aft = user_input[j]
        check_list.append(pre)
        if pre != aft:
            if aft in check_list:
                break
        i += 1
        j += 1
print(count)
