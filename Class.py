from Professor import *


class Course:
    instances = list()

    def __init__(self, code, credit_count, prereq_codes, required, rating):
        self.code = code
        self.credits = credit_count
        self.prereq_codes = prereq_codes
        self.required = required
        self.rating = rating
        self.sessions = list()
        self.instances.append(self)

    def add_session(self, session):
        self.sessions.append(session)

    def get_sessions(self):
        return self.sessions

    def get_prereqs(self):
        return self.prereq_codes


class Session:
    def __init__(self, quarter, professor):
        self.quarter = quarter
        self.professor = professor

    def __str__(self):
        return repr(self.quarter) + " " + str(self.professor)

    def get_professor(self):
        return self.professor

    def get_quarter(self):
        return self.quarter


