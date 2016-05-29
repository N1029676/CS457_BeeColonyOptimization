from Schedule import *
import thread
import threading
import time
import random


class EliteBee (threading.Thread):
    def __init__(self, threadid, name, iterations):
        threading.Thread.__init__(self)
        self.threadID = threadid
        self.name = name
        self.iterations = iterations

    def run(self):
        while self.iterations > 0:
            eliteScheduleLock.acquire()

            eliteScheduleLock.release()
            self.iterations -= 1


threads = []

eliteSchedules = list()
eliteScheduleLock = threading.Lock()




thread1 = EliteBee(1, "Bee1", 30)
thread2 = EliteBee(2, "Bee2", 60)
thread3 = EliteBee(3, "Bee3", 40)
thread4 = EliteBee(4, "Bee4", 30)

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
print "Exiting main thread!"


