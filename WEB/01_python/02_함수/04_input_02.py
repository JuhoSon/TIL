print('hi', 'hello', '안녕', 'Guten Morgen', 'Bon jour')

def add(*args):
    print(args, type(args))
    return sum(args)

add(1, 2, 3)
add(1)