from time import sleep
import random 

snow = '*'
while True:
    for _ in range(100):
        if random.randint(0, 1):
            snow += '*'
        else:
            snow += ' '
    print(snow)
    sleep(1.5)