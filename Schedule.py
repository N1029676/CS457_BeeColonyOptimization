from Class import *

REQUIRED_CREDITS = 106

class Schedule:
    def __init__(self, startYear, startQuarter):
        self.startYear = startYear
        self.startQuarter = startQuarter
        self.maxCreditsPerQuarter = 22
        self.maxQuarters = 9
        self.fitness = 0
        self.schedule = list()

    def check_fitness(self, weightProfessor, weightCourse, weightCompletion, weightCredit):
        """Check the fitness of the current configuration

        Args:
            weightProfessor (int): How important is the professor rating
            weightCourse (int): How important is the class's rating
            weightCompletion (int): How important is finishing faster
            weightCredit (int): How important is having a low credit load

        Returns:
            int: returns an int with higher numbers representing a higher satisfaction
            based on the provided weights.
        """
        return 0

    def check_prereqs(self, course):
        if course.prereq_codes is None:
            return 0
        prereqs_unmet = len(course.prereq_codes)
        for prereq in course.prereq_codes:
            for session in self.schedule:
                if session.course == prereq:
                    prereqs_unmet -= 1
                    break
        return prereqs_unmet

    def add_session(self, session):
        self.schedule.append(session)

    def drop_session(self, session):
        self.schedule.remove(session)

    def get_sessions(self, quarter=None):
        output = list()
        if quarter is not None:
            for session in self.schedule:
                if session.get_quarter() == quarter:
                    output.append(session)
        else:
            output = self.schedule
        return output

    def sort(self):
        self.schedule.sort(key=lambda x: x.quarter, reverse=False)

    def swap_course(self, course_one, course_two):
        return 0

