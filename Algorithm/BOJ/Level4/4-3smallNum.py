seq, num = map(int, input().split())
seq_list = input().split()
result = []
for i in seq_list:
    if int(i) < num:
        result.append(i)
print(' '.join(result))
