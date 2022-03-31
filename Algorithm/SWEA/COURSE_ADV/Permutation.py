"""
연습문제 1. 순열
1-1) 단순하게 순열 생성하기
[1, 2, 3]을 포함하는 모든 순열을 반복문을 활용하여 구현하시오.
"""

nums = [1, 2, 3]

for i in nums:
    for j in nums:
        if i != j:
            for k in nums:
                if j != k and i != k:
                    print(i, j, k)


"""
1-2) 재귀로 순열 생성하기
[1, 2, 3]을 포함하는 모든 순열을 재귀 함수를 활용하여 구현하시오.
** 각 자리를 어떻게 확정 시킬 것인가에 초점을 맞춰 구현해보세요.
** swap하는 방식과 방문 처리를 하는 방식으로 모두 구현해보세요.
    n = 0                            |1|2|3|
                            /           |             \
    n = 1           |1|2|3|          |2|1|3|        |3|2|1|
                    /    \           /     \        /     \
    n = 2       |1|2|3| |1|3|2|  |2|1|3| |2|3|1| |3|2|1| |3|1|2|

                          자리가 확정되면 출력(n == k)
"""
# 1. swap
def perm_swap(n, k):
    if n == k:
        print(*nums)
    else:
        for i in range(n, k):
            nums[n], nums[i] = nums[i], nums[n]
            perm_swap(n+1, k)
            nums[n], nums[i] = nums[i], nums[n]
nums = [1, 2, 3]
perm_swap(0, len(nums))
print('---------------------------------------')


# 2. visited
def perm_visited(k):
    if n == k:
        print(*sel)
    else:
        for i in range(n):
            if visited[i]: continue
            visited[i] = 1
            sel[k] = nums[i]
            perm_visited(k+1)
            visited[i] = 0
nums = [1, 2, 3]
n = len(nums)
visited = [0] * n
sel = [0] * n
perm_visited(0)


"""
1-3) 5개의 숫자 중 3자리의 순열 생성하기
[1, 2, 3, 4, 5]에서 3자리의 순열을 재귀 함수를 활용하여 구현하시오.
"""
def perm(n, k, m):
    if n == k:
        for i in range(k):
            print(nums[i], end=' ')
        print()
    else:

        for i in range(n, m):
            nums[n], nums[i] = nums[i], nums[n]
            perm(n+1, k, m)
            nums[n], nums[i] = nums[i], nums[n]
nums = [1, 2, 3, 4, 5]
perm(0, 3, len(nums))
print('#########################')

# visited 버전
def perm(i, n, k):
    if i == k:
        print(*p)
    else:
        for j in range(n):
            if not u[j]:
                u[j] = 1
                p[i] = nums[j]
                perm(i+1, n, k)
                u[j] = 0

nums = [1, 2, 3, 4, 5]
N = len(nums)
K = 3
u = [0] * N
p = [0] * K
perm(0, N, K)


"""
연습문제 2. 부분 집합 구현
2-1) {-1, 3, -9, 6, 7, -6, 1, 5, 4, -2} 의 모든 부분 집합 구하기
"""

def print_set(n):
    global cnt_subset
    cnt_subset += 1
    print('{}: '.format(cnt_subset), end='')

    for i in range(n):
        if check[i] == 1:
            print(nums[i], end=' ')
    print()

def powerset(n, k):
    if n == k:
        print_set(n)
    else:
        check[n] = 1
        powerset(n+1, k)
        check[n] = 0
        powerset(n+1, k)


cnt_subset = 0
nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums)
check = [0 for _ in range(N)]
powerset(0, N)


"""
연습문제 2. 부분 집합의 합 구현
2-2) {-1, 3, -9, 6, 7, -6, 1, 5, 4, -2}의 모든 부분 집합 중 원소의 합이 0이 되는 부분집합 구하기
** 비트 연산
- 원소 수에 해당하는 N개의 비트열을 활용
- n번째 비트값이 1이면 n번째 원소가 '포함'되었음을 의미
0   0 0 0 0   {A, B, C, D}
1   0 0 0 1   {A}
2   0 0 1 0   {B}
3   0 0 1 1   {B, A}
...........
14  1 1 1 0   {D, C, B}
15  1 1 1 1   {D, C, B, A}
"""


# 1. 재귀 활용
def print_set(n):
    global cnt_subset
    sum_of_subset = 0
    for i in range(n):
        if check[i] == 1:
            sum_of_subset += nums[i]

    if sum_of_subset == 0:
        cnt_subset += 1
        print('{}: '.format(cnt_subset), end='')

        for i in range(n):
            if check[i] == 1:
                print('{} '.format(nums[i]), end='')
        print()


def powerset(n, k):
    if n == k:
        print_set(n)
    else:
        check[n] = 1
        powerset(n + 1, k)
        check[n] = 0
        powerset(n + 1, k)


cnt_subset = 0
nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums)
check = [0 for _ in range(N)]
powerset(0, N)
print('------------------------------------------------')

# 2-1. 비트 연산 활용
nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums)

for i in range(1 << N):
    my_sum = []
    for j in range(N):
        if i & (1 << j):
            my_sum.append(nums[j])
    if sum(my_sum) == 0:
        print(*my_sum)
print('------------------------------------')

# 2-2. 비트 연산 활용
nums2 = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums2)

for i in range(1 << N):
    my_sum = 0
    for j in range(N):
        if i & (1 << j):
            my_sum += nums2[j]
    if my_sum == 0:
        for j in range(10):
            if i & (1 << j):
                print(nums2[j], end=' ')
        print()
