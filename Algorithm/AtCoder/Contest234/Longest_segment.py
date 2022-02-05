'''
Time Limit: 2 sec / Memory Limit: 1024 MB

Score : 200 points

Problem Statement
There are N points in a two-dimensional plane. The coordinates of the i-th point are (x_i, y_i).
Find the maximum length of a segment connecting two of these points.

Example
3
0 0
0 1
1 1
->
1.4142135624
'''

N = int(input())
inp_arr = [tuple(map(int, input().split(' '))) for _ in range(N)]

dist = lambda xy1, xy2: ((xy2[0]-xy1[0])**2 + (xy2[1]-xy1[1])**2)**0.5
def solution(inp_arr):
    result = dict()
    for fir_idx in range(len(inp_arr)):
        for sec_idx in range(fir_idx+1, len(inp_arr)):
            result[(fir_idx, sec_idx)] = dist(inp_arr[fir_idx], inp_arr[sec_idx])
    return sorted(result.items(), key=lambda x: x[1])[-1][1]  # largest pair's distance

print(solution(inp_arr))