inpstr = list(input())
ath, bth = map(lambda x: int(x)-1, input().split())
inpstr[ath], inpstr[bth] = inpstr[bth], inpstr[ath]
print(''.join(inpstr))