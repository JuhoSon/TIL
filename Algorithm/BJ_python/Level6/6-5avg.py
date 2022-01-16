score_list = []
for i in range(5):
    temp_score = int(input())
    if temp_score >= 40:
        score_list.append(temp_score)
    else:
        score_list.append(40)
print(int(sum(score_list) / len(score_list)))
