# arr_list = [int(input()) for counts in range(int(input()))]
# arr_list.sort()
# for i in arr_list:
#     print(i)

x = [int(input()) for times in range(int(input()))]


# 버블정렬
def bubbleSort(x):
    for i in range(len(x)):
        for j in range(len(x)-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x


for i in bubbleSort(x):
    print(i)


# 삽입정렬
# def insertSort(x):
#     for i in range(len(x)):
#         j = i - 1
#         key = x[i]
#         while x[j] > key and j >= 0:
#             x[j+1] = x[j]
#             j -= 1
#         x[j+1] = key
#     return x
#
#
# for i in insertSort(x):
#     print(i)
