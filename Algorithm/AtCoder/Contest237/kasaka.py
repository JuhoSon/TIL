inp = input()


def pal(inpstr):
    if inpstr == inpstr[::-1]:
        return True
    else:
        return False


FLAG = 'No'
for acnt in range(len(inp)):
    inpstr = 'a'*acnt + inp
    if pal(inpstr):
        FLAG = 'Yes'
print(FLAG)