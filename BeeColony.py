# from EliteBee import *
from ScoutBee import *
import time

threads = []

thread1 = EliteBee(50)
thread2 = ScoutBee(0)
# thread3 = ScoutBee(0)
# thread4 = ScoutBee(0)
# thread5 = ScoutBee(0)
# thread6 = ScoutBee(0)
# thread7 = ScoutBee(0)

thread1.setDaemon(True)
thread2.setDaemon(True)
# thread3.setDaemon(True)
# thread4.setDaemon(True)
# thread5.setDaemon(True)
# thread6.setDaemon(True)
# thread7.setDaemon(True)

thread1.start()
thread2.start()
# thread3.start()
# thread4.start()
# thread5.start()
# thread6.start()
# thread7.start()

threads.append(thread1)
threads.append(thread2)
# threads.append(thread3)
# threads.append(thread4)
# threads.append(thread5)
# threads.append(thread6)
# threads.append(thread7)

print "Main thread waiting!", time.ctime()

for thread in threads:
    thread.join()

# while True:
#     print scout_schedules.qsize()
#     if scout_schedules.qsize() == 0:
#         break
#     output_schedule = scout_schedules.get()
#     for session in output_schedule.get_sessions():
#         print session
#     print "\n\n"


print "Exiting main thread!", time.ctime()
