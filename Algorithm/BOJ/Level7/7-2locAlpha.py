S = input()
alpha_list = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
result = []
for i in alpha_list:
    if i in S:
        result.append(str(S.index(i)))
    else:
        result.append(str(-1))
print(' '.join(result))
