from EliteBee import *

threads = []

thread1 = EliteBee(30)
thread2 = EliteBee(30)
thread3 = EliteBee(30)
thread4 = EliteBee(30)

thread1.start()
thread2.start()
thread3.start()
thread4.start()

threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
threads.append(thread4)

for thread in threads:
    thread.join()

for schedule in elite_schedules:
    for course in schedule:
        print course,
    print "\n"

print len(elite_schedules)

print "Exiting main thread!"
