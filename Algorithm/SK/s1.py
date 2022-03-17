def solution(money, costs):
    PEN = [500, 100, 50, 10, 5, 1]
    COSTS = costs[::-1]
    COST = {P:C for P, C in zip(PEN, COSTS)}
    
    answer = 0
    for idx, p in enumerate(PEN):
        remain_p = PEN[idx+1:]
        p_cost = COST[p]
        FLAG = False
        for rp in remain_p:
            MULTI_NUM = p // rp  # 500 // 10 = 50 (50 times)
            rp_cost = COST[rp]
            if p_cost > rp_cost * MULTI_NUM:
                FLAG = True
        if FLAG:
            continue
    
        p_cnt = money // p
        money %= p * p_cnt
        answer += p_cnt * p_cost

    return answer


print(solution(4578, [1, 4, 99, 35, 50, 1000]))
print(solution(1999, [2, 11, 20, 100, 200, 600]))