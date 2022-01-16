def d(a):
    sums = a
    for i in range(len(str(a))):
        sums += a % 10
        a //= 10
    return sums


num_list = list(range(1, 10001))
generate_list = []
check_list = []
for i in num_list:
    generate_list.append(d(i))
    if i not in generate_list:
        check_list.append(i)

for j in check_list:
    print(j)
