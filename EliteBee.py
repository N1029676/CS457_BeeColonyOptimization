from Schedule import *
import threading
import random
import Queue

elite_schedules = Queue.Queue()

class EliteBee(threading.Thread):
    def __init__(self, iterations):
        threading.Thread.__init__(self)
        self.iterations = iterations

    def run(self):
        while self.iterations > 0:
            selected_courses = list(Course.requiredCourses)
            electives_available = list(Course.electiveCourses)
            credit_count = 0

            for course in selected_courses:
                credit_count += course.credits

            while credit_count < REQUIRED_CREDITS:
                random.shuffle(electives_available)
                selected_elective_course = electives_available.pop()
                credit_count += selected_elective_course.credits
                selected_courses.append(selected_elective_course)

            elite_schedules.put(selected_courses)
            self.iterations -= 1
