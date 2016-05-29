from Schedule import *
import thread
import threading
import time
import random

class EliteBee (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting " + self.name
        randomInt = random.randint(1, 20)
        while self.counter > 0:
            threadLock.acquire()
            time.sleep(2.0 / randomInt)
            print_time(self.name, 1, self.counter)
            threadLock.release()
            self.counter -= 1


def print_time(threadName, delay, counter):
    print "%s: %s - %s" % (threadName, counter, time.ctime(time.time()))


threadLock = threading.Lock()
threads = []

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


