x = int(input())
x //= 10
if x >= 0:
    print(int(x))
elif not x * 10 % 10:
    print(int(x))
else:
    print(int(x) - 1)