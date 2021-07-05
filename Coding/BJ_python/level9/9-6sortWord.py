sort_set = set()
for times in range(int(input())):
    sort_set.add(input())
sort_list = list(sort_set)
result = sorted(sort_list, key=lambda x: (len(x), x))
for i in result:
    print(i)
