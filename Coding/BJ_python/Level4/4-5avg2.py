C = int(input())
for i in range(C):
    score_list = list(map(int, input().split()))
    num_stu = score_list.pop(0)
    score_avg = sum(score_list) / len(score_list)
    num_avg_up = [i for i in score_list if i > score_avg]
    print('{:.3f}%'.format(len(num_avg_up) / num_stu * 100))
