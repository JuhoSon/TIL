N = int(input())
As = map(int, input().split())

'''
360=0이라 보기,  잘리는지점만 저장
[0] -> [0, 0+90]=[0,90] -> [0, 0+180, 90+180]=[0,180,270] -> [0, 0+45, 180+45, 270+45]=[0,45,225,315] 
-> [0, 0+195, 45+195, 225+195, 315+195]=[0, 195, 240, 420=60, 510=150]
'''

result_range = [0]  # initial cutting

for rotation_degree in As:
    new_range = [0]  # cutting
    for r in result_range:  # rotation
        new_degree = (r + rotation_degree) % 360
        new_range.append(new_degree)
    result_range = list(new_range)
result_range.append(360)

# find max degree section
degree = []
result_range = sorted(result_range)
end_degree = result_range.pop()
while len(result_range):
    start_degree = result_range.pop()
    
    degree.append(end_degree - start_degree)

    end_degree = start_degree    
print(max(degree))