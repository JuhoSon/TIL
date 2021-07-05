sub_num = int(input())
score_list = list(map(int, input().split()))
M = max(score_list)
new_list = [i/M*100 for i in score_list]
print(sum(new_list) / len(new_list))
