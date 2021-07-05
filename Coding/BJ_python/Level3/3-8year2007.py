month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_list = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
date = 0
user_month, user_date = map(int, input().split())

for i in range(user_month-1):
    date += month_list[i]
date = (date + user_date) % 7
print(day_list[date])
