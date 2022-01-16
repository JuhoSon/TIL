import sys

user_list = [int(sys.stdin.readline()) for i in range(int(sys.stdin.readline()))]
# 최빈값 함수

sys.stdout.write(int(sum(user_list)/len(user_list)))  # 산술평균
sys.stdout.write(sorted(user_list)[int(len(user_list)/2)])  # 중간값


count_list = []
for i in user_list:
    count_list.append(user_list.count(i))
if count_list.count(max(count_list)) == 1:
    freq_index = count_list.index(max(count_list))
    sys.stdout.write(user_list[freq_index])
elif count_list.count(max(count_list)) >= 2:
    # 최솟값의 인덱스 구하기
    min_index = []
    for i in count_list:
        if i == max(count_list):
            min_index.append(count_list.index(i))
            count_list[count_list.index(i)] = -1
    # 두 번째로 작은 값 구하기
    user_list_temp = [user_list[i] for i in min_index]
    user_list_temp = list(set(user_list_temp))
    user_list_temp.remove(min(user_list_temp))
    sys.stdout.write(min(user_list_temp))
sys.stdout.write(max(user_list)-min(user_list))  # 최댓값-최솟값
