import sys
sys.stdin = open('Tree_11279_최대힙.txt')


def hpush(x):
    global pointer
    pointer += 1
    heap[pointer] = x
    child_idx = pointer
    parent_idx = child_idx // 2

    while parent_idx and heap[parent_idx] < heap[child_idx]:
        heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]
        child_idx = parent_idx
        parent_idx = child_idx // 2


def hpop(num):
    global pointer
    if pointer == 0:
        return 0
    root = heap[1]
    heap[1] = heap[pointer]
    heap[pointer] = 0
    pointer -= 1

    parent_idx = 1
    child_idx = parent_idx * 2

    if child_idx + 1 <= pointer:
        if heap[child_idx] < heap[child_idx + 1]:
            child_idx = child_idx + 1

    while child_idx <= pointer and heap[parent_idx] < heap[child_idx]:
        heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]
        parent_idx = child_idx
        child_idx = parent_idx * 2

        if child_idx + 1 <= pointer:
            if heap[child_idx] < heap[child_idx + 1]:
                child_idx = child_idx + 1
    return root


N = int(input())
inp = [int(input()) for _ in range(N)]  # integer: push, 0: pop

# hard coding
heap = [0 for _ in range(N + 1)]  # zero padding, start with index 1
pointer = 0
for num in inp:
    if num == 0:
        print(hpop(num))
    else:
        hpush(num)