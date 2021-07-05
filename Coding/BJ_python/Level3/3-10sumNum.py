user_input1 = int(input())
user_input2 = int(input())
sums = 0
for i in range(user_input1+1):
    sums += user_input2 % 10
    user_input2 //= 10
print(sums)
