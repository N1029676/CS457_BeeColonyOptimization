from EliteBee import *
import threading
import Queue
from collections import deque
import time
import random

scout_schedules = Queue.PriorityQueue()
MAX_SCOUT_ATTEMPTS = 3000


class ScoutBee(threading.Thread):
    def __init__(self, iterations):
        threading.Thread.__init__(self)
        self.iterations = iterations

    def run(self):
        time.sleep(0.5)
        while True:
            if elite_schedules.empty():
                break
            designated_schedule = deque(elite_schedules.get())
            new_schedule = Schedule(2016, 1)
            attempts = 0
            while (attempts < MAX_SCOUT_ATTEMPTS) & (len(designated_schedule) > 0):
                course_to_evaluate = designated_schedule.pop()
                if new_schedule.check_prereqs(course_to_evaluate) == 0:
                    new_schedule.add_session(course_to_evaluate.get_sessions()[0])
                else:
                    designated_schedule.appendleft(course_to_evaluate)
                attempts += 1

            new_schedule.sort()
            scout_schedules.put(new_schedule)

