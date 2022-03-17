import sys
sys.stdin = open('input.txt')


def enq(num):
    global heap_cnt

    # input
    heap_cnt += 1
    heap_tree[heap_cnt] = num


    # heapify
    p = heap_cnt // 2
    c = heap_cnt
    while p and heap_tree[p] > heap_tree[c]:
        heap_tree[p], heap_tree[c] = heap_tree[c], heap_tree[p]
        c = p
        p = c // 2


T = int(input())
for tc in range(1, T+1):
    V = int(input())
    nodes = map(int, input().split())
    heap_tree = [0 for _ in range(V + 1)]
    heap_cnt = 0

    for n in nodes:
        enq(n)

    last_node_idx = (len(heap_tree) - 1) // 2
    anc_sum = 0
    while last_node_idx:
        anc_sum += heap_tree[last_node_idx]
        last_node_idx //= 2

    print('#{} {}'.format(tc, anc_sum))

