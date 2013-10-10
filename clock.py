#clock.py

import time

s = input('time: ')

ring_time = time.localtime()
now = time.strptime(s,"%H:%M")

ring_time.tm_hour=now.tm_hour
ring_time.tm_min=now.tm_min

#set a timer
#if ring_time == now
# play sound
