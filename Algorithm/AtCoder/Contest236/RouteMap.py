local_size, express_size = map(int, input().split())
locals = input().split()
expresses = {station:True for station in input().split()}

for station in locals:
    if expresses.get(station, False):
        print('Yes')
    else:
        print('No')