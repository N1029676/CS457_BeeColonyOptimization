from EliteBee import *
import threading
import Queue
import time
import random

scout_schedules = Queue.PriorityQueue()


class ScoutBee(threading.Thread):
    def __init__(self, iterations):
        threading.Thread.__init__(self)
        self.iterations = iterations

    def run(self):
        time.sleep(3)
        while True:
            designated_schedule = elite_schedules.get()
            if elite_schedules.empty():
                break
            new_schedule = Schedule(2016, 1)
            for course in designated_schedule:
                new_schedule.add_session(course.get_sessions()[0])

            new_schedule.sort()
            scout_schedules.put(new_schedule)
            scout_schedules.task_done()
            elite_schedules.task_done()

