grades = {'kim': 80, 'lee': 100}

# 1. 딕셔너리 순회 => key!!!
for key in grades:
  print(key, grades[key])
print('======================')
# 2. keys
for key in grades.keys():
  print(key, grades[key])
print('======================')
# 3. values 
for value in grades.values():
  print(value) 
print('======================')
# 4. items 
for key, value in grades.items():
  # key, value = ('kim', 80)   // x, y = 1, 2 
  print(key, value)

print(grades.items()) 
