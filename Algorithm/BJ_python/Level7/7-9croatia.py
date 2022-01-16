user_input = input()
croatia_alp = {'c=': 'c', 'c-': 'c', 'dz=': 'd', 'd-': 'n', 'lj': 'l',
               'nj': 'n', 's=': 's', 'z=': 'z'}
for keys, values in croatia_alp.items():
    if keys in user_input:
        user_input = user_input.replace(keys, values)
print(len(user_input))
