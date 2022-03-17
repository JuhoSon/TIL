# 1부터 사용자가 입력한 양의 정수까지의 총합 (while)
# 사용자 입력한 양의 정수를 저장.
user_input = int(input())
# 값 초기화 
n = 1
total = 0
# 반복문
while n <= user_input:
    # 하나씩 더하긴 해야하는데..
    total += n 
    n += 1
print(total)
