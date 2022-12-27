from datetime import datetime
from random import randint
import time

odds = []
for i in range(60):
	if (i % 2 == 1):
		odds.append(i)
	

for i in range(5):
  right_this_minute = datetime.today().minute

  if right_this_minute in odds:
    print("This minute seems a little odd")
  else:
    print("Not an odd minute")
  
  nprint("This minute is {minute}".format(minute=right_this_minute))
  wait_time = randint(0, 60)
  time.sleep(wait_time)
