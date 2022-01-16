user_input = int(input())
count = 0
new_num = user_input
while True:
    right_num_raw = new_num % 10
    right_num_sum = (new_num // 10 + new_num % 10) % 10
    new_num = int(str(right_num_raw)+str(right_num_sum))
    count += 1
    if new_num == user_input:
        break
print(count)
