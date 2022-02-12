N = int(input())
cards = map(int, input().split())  # size of 4N-1
# 4로 나누었을 때 나머지가 3인 것이 삭제된 카드
card_cnt = dict()
for num in cards:
    if num not in card_cnt:
        card_cnt[num] = 0
    card_cnt[num] += 1

for num, cnt in card_cnt.items():
    if cnt % 4 == 3:
        result = num
print(result)