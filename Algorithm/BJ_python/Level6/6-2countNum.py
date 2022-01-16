a = int(input())
b = int(input())
c = int(input())
result = str(a*b*c)
num_dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0,
            '6': 0, '7': 0, '8': 0, '9': 0}
for i in result:
    num_dict[i] += 1
for j in num_dict.values():
    print(j)
