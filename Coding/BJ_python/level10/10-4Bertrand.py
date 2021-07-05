while True:
    user_input = int(input())
    if user_input == 0:
        break
    start_num, finish_num = user_input+1, user_input*2
    seive = [False, False] + [True] * (finish_num - 1)
    for k in range(2, int(finish_num ** 0.5 + 1.5)):
        if seive[k]:
            seive[k*2::k] = [False] * ((finish_num - k) // k)
    prime_list = [x for x in range(finish_num+1) if seive[x]
                  and x >= start_num and x <= finish_num]
    print(len(prime_list))
