goal = int(input())
five = goal // 5
goal %= 5
three = 0
while five >= 0:
    if goal % 3 == 0:
        three = goal // 3
        goal %= 3
        break
    five -= 1
    goal += 5
print(five + three)
