def solution(width, height, diagonals):
    min_path = width + height + 1
    answer = 0

    answer %= 10000019
    return answer


a = 12
s = solution(2, 2, [[1,1],[2,2]])
print(a, s)