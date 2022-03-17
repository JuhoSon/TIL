x = [int(input()) for i in range(int(input()))]


def mergeSort(x, start=0, finish=len(x)-1):
    if start < finish:
        middle = int((start+finish)/2)
        mergeSort(x, start, middle)
        mergeSort(x, middle+1, finish)
        merge(x, start, middle, finish)
    return x


def merge(x, start=0, middle=int((0+len(x)-1)/2), finish=len(x)-1):
    s = start
    m = middle+1
    count = 0
    tmp = [0]*len(x)
    while (s <= middle and m <= finish):
        if x[s] <= x[m]:
            tmp[count] = x[s]
            count += 1
            s += 1
        else:
            tmp[count] = x[m]
            count += 1
            m += 1
    while s <= middle:
        tmp[count] = x[s]
        count += 1
        s += 1
    while m <= finish:
        tmp[count] = x[m]
        count += 1
        m += 1
    s = start
    count = 0
    while s <= finish:
        x[s] = tmp[count]
        s += 1
        count += 1
    return x


mergeSort(x)
