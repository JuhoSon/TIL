for repeat in range(int(input())):
    user_input = input().upper()
    score = 0
    sums = 0
    for i in user_input:
        if i == 'O':
            score += 1
        else:
            score = 0
        sums += score
    print(sums)
