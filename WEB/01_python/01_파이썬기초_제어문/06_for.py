chars = 'happy'

# 1. 단순히 순회 (for)
for char in chars:
  print(char)

# 2. 인덱스로 접근 => 0 ~ 길이-1 (반복) 
for idx in range(len(chars)):
  print(idx, chars[idx])

for idx, value in enumerate(chars):
  # idx, value = (0, 'h')
  print(idx, value)