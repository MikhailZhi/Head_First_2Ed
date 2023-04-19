import datetime
import random
import time


odds = []

for o in range(1,60,2):
    odds.append(o)



for i in range(4):
    min_now = datetime.datetime.now().minute
    print (datetime.datetime.now())
    if min_now in odds:
        print (min_now, "- this minute seems a little odd")
    else:
        print (min_now, "- not an odd minute")
    wait_time = random.randint(1,45)
    print ("Let's wait", wait_time, "sec\n")
    time.sleep(wait_time) 

print("That's all!")
