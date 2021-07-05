print('%5d/ %8f/ %2s/' % (1, 2.123412341234, 3))
print("{2} {0} {1}".format(1, 2, 'a'))
s = 90
if s >= 90: grade = 'a'
elif s >= 80: grade = 'b'
else: grade='f'
print(grade)
def cal(a, b):
    return a+b
cal(1, 2)


def asterisk_test(a, b, *args):
    return a+b+sum(args)


asterisk_test(1, 2, 3, 4, 5)


def asterisk_test2(*args):
    return args


print(asterisk_test2(3, 4, 5))


def kwargs_test(*args, **kwargs):
    print(kwargs)
    return None


kwargs_test(1, 2, 3, 4, 5)

print("\n")

s = set([1, 2, 3])
s.add(4)
s.remove(1)
s.update([5, 6])
s.discard(3)
s

temp_dict = {1: 'juho', 2: 'sejeong', 3: 'sonju'}
temp_dict
temp_dict.items()
temp_dict.keys()
temp_dict.values()
temp_dict['juho'] = 1
temp_dict

f = lambda x, y: x+y
print(*(1,2,3,4,5))
