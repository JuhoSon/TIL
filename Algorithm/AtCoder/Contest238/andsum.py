T = int(input())

for t in range(T):
    a, s = map(int, input().split())
    pair = set()
    # sum pair (brute-force)
    for n in range(s+1):
        pair.add((n, s-n))
    # and pair
    result = set()
    for p in pair:
        x = p[0]
        y = p[1]
        if x & y == a:
            result.add((x,y))
    
    if len(result) > 0:
        print('Yes')
    else:
        print('No') 