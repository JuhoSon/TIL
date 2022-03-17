# 1~30까지 숫자 중에 (반복)
# 홀수만 (조건)

# 1-1. 빈통
numbers = []
for i in range(1, 31):
  if i % 2 == 1:
    numbers.append(i)
print(numbers)

numbers_2 = [ i for i in range(1, 31) if i % 2 == 1]
print(numbers_2)