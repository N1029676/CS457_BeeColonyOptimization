# from EliteBee import *
from ScoutBee import *

threads = []

thread1 = EliteBee(50)
thread2 = EliteBee(90)
# thread3 = EliteBee(30)
thread4 = ScoutBee(0)

thread1.setDaemon(True)
thread2.setDaemon(True)
# thread3.setDaemon(True)
thread4.setDaemon(True)

thread1.start()
thread2.start()
# thread3.start()
thread4.start()

threads.append(thread1)
threads.append(thread2)
# threads.append(thread3)
threads.append(thread4)

print "Main thread waiting!"

for thread in threads:
    thread.join()


print "Exiting main thread!"
