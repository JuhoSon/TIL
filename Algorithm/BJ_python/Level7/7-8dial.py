user_input = input()
result_list = []
tel_dict = {2: '', 3: 'ABC', 4: 'DEF', 5: 'GHI', 6: 'JKL', 7: 'MNO',
            8: 'PQRS', 9: 'TUV', 10: 'WXYZ', 11: ''}
for tel_num in user_input:
    for keys, values in tel_dict.items():
        if tel_num in values:
            result_list.append(keys)
print(sum(result_list))
