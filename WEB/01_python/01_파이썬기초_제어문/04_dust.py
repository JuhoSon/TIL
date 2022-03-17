dust = 100 

# 150 초과 : 매우 나쁨
if dust > 150:
    print('매우 나쁨!')
# 80 초과 150이하 : 나쁨 
elif dust > 80:
    print('나쁨')
# 30 초과 : 보통 
elif dust > 30:
    print('보통')
# 나머지는 모두 좋음 
else:
    print('좋음')