user_input = input()
count = len(user_input) // 10
for i in range(count+1):
    print(user_input[:10])
    user_input = user_input[10:]
