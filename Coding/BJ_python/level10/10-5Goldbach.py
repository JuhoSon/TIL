cycle_num = int(input())
# make prime_list
finish_num = 10000
seive = [False, False] + [True] * (finish_num - 1)
for k in range(2, int(finish_num ** 0.5 + 1.5)):
    if seive[k]:
        seive[k*2::k] = [False] * ((finish_num - k) // k)
prime_list = [x for x in range(finish_num+1) if seive[x]
              and x <= finish_num]

for times in range(cycle_num):
    user_input = int(input())
    ave = user_input//2  # 소수리스트의 중간항부터 계산해야 소수두개의 차이가 가장적다
    f_count = ave
    s_count = ave
    while f_count > 0:
        if f_count in prime_list and s_count in prime_list:
            # f_count와 s_count가 소수일때
            if user_input == f_count + s_count:  # 그 두 소수의 합이 입력한 짝수이면 성립
                print(f_count, s_count)
                break
        f_count -= 1
        s_count += 1
