import datetime
import random
import time


odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]



for i in range(4):
    min_now = datetime.datetime.now().minute
    print (datetime.datetime.now())
    if min_now in odds:
        print (min_now, "- this minute seems a little odd")
    else:
        print (min_now, "- not an odd minute")
    time.sleep(random.randint(1,45)) 

print("That's all!")
