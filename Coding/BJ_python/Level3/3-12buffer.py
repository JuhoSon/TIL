import sys
input_count = int(input())
for i in range(1, input_count+1):
    user_input = sys.stdin.readline()
    a, b = map(int, user_input.split())
    print(a+b)
