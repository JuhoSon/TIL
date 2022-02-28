inp = int(input())

lower_bnd = -2**31
upper_bnd = 2**31 - 1

if lower_bnd <= inp <= upper_bnd:
    print('Yes')
else:
    print('No')