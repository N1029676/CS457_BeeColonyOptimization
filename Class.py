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
        session.add_code(self)

    def session(self, session):
        self.add_session(session)

    def get_sessions(self):
        return self.sessions

    def get_prereqs(self):
        return self.prereq_codes


class Session:
    def __init__(self, quarter, professor):
        self.quarter = quarter
        self.professor = professor
        self.course = None

    def __str__(self):
        return repr(self.course.code) + " " + repr(self.quarter) + " " + str(self.professor)

    def add_code(self, code):
        self.course = code

    def get_professor(self):
        return self.professor

    def get_quarter(self):
        return self.quarter


cs110 = Course(110, 4, None, True, 0)
cs110.session(Session(1, ))
cs110.session(Session(1, ))
cs110.session(Session(2, ))
cs110.session(Session(3, ))
cs110.session(Session(4, ))
cs110.session(Session(4, ))
cs110.session(Session(5, ))
cs110.session(Session(6, ))
cs110.session(Session(7, ))
cs110.session(Session(7, ))
cs110.session(Session(8, ))
cs110.session(Session(9, ))

cs111 = Course(111, 4, [cs110], True, 0)
cs111.session(Session(2, ))
cs111.session(Session(2, ))
cs111.session(Session(3, ))
cs111.session(Session(5, ))
cs111.session(Session(5, ))
cs111.session(Session(6, ))
cs111.session(Session(8, ))
cs111.session(Session(8, ))
cs111.session(Session(9, ))

cs112 = Course(112, 4, None, False, 0)
cs112.session(Session(1, ))
cs112.session(Session(3, ))
cs112.session(Session(4, ))
cs112.session(Session(6, ))
cs112.session(Session(7, ))
cs112.session(Session(9, ))

cs301 = Course(301, 4, [cs111], True, 0)
cs301.session(Session(1, ))
cs301.session(Session(1, ))
cs301.session(Session(4, ))
cs301.session(Session(4, ))
cs301.session(Session(7, ))
cs301.session(Session(7, ))

cs302 = Course(302, 4, [cs301], True, 0)
cs302.session(Session(2, ))
cs302.session(Session(2, ))
cs302.session(Session(5, ))
cs302.session(Session(5, ))
cs302.session(Session(8, ))
cs302.session(Session(8, ))

cs311 = Course(311, 4, [cs110], True, 0)
cs311.session(Session(1, ))
cs311.session(Session(1, ))
cs311.session(Session(3, ))
cs311.session(Session(3, ))
cs311.session(Session(4, ))
cs311.session(Session(4, ))
cs311.session(Session(6, ))
cs311.session(Session(6, ))
cs311.session(Session(7, ))
cs311.session(Session(7, ))
cs311.session(Session(9, ))
cs311.session(Session(9, ))

cs312 = Course(312, 4, [cs301, cs311], True, 0)
cs312.session(Session(1, ))
cs312.session(Session(2, ))
cs312.session(Session(2, ))
cs312.session(Session(4, ))
cs312.session(Session(5, ))
cs312.session(Session(5, ))
cs312.session(Session(7, ))
cs312.session(Session(8, ))
cs312.session(Session(8, ))

cs325 = Course(325, 3, [cs301], True, 0)
cs325.session(Session(2, ))
cs325.session(Session(3, ))
cs325.session(Session(5, ))
cs325.session(Session(6, ))
cs325.session(Session(8, ))
cs325.session(Session(9, ))

cs361 = Course(361, 4, [cs302], True, 0)
cs361.session(Session(1, ))
cs361.session(Session(1, ))
cs361.session(Session(4, ))
cs361.session(Session(4, ))
cs361.session(Session(7, ))
cs361.session(Session(7, ))

cs362 = Course(362, 4, [cs361], True, 0)
cs362.session(Session(2, ))
cs362.session(Session(2, ))
cs362.session(Session(5, ))
cs362.session(Session(5, ))
cs362.session(Session(8, ))
cs362.session(Session(8, ))

cs380 = Course(380, 4, [cs302], True, 0)
cs380.session(Session(1, ))  # This is made up, I can't find it anywhere on the schedules
cs380.session(Session(1, ))  # This is made up, I can't find it anywhere on the schedules
cs380.session(Session(1, ))  # This is made up, I can't find it anywhere on the schedules
cs380.session(Session(1, ))  # This is made up, I can't find it anywhere on the schedules
cs380.session(Session(1, ))  # This is made up, I can't find it anywhere on the schedules
cs380.session(Session(1, ))  # This is made up, I can't find it anywhere on the schedules

cs392 = Course(392, 1, None, True, 0)
cs392.session(Session(1, ))
cs392.session(Session(2, ))
cs392.session(Session(3, ))
cs392.session(Session(4, ))
cs392.session(Session(5, ))
cs392.session(Session(6, ))
cs392.session(Session(7, ))
cs392.session(Session(8, ))
cs392.session(Session(9, ))

cs427 = Course(427, 4, [cs302, cs325], True, 0)
cs427.session(Session(1, ))
cs427.session(Session(1, ))
cs427.session(Session(4, ))
cs427.session(Session(4, ))
cs427.session(Session(7, ))
cs427.session(Session(7, ))

cs420 = Course(420, 4, [cs302, cs325], False, 0)
cs420.session(Session(3, ))
cs420.session(Session(6, ))
cs420.session(Session(9, ))

# cs446 = Course(446, 4, [cs302], False, 0)

cs470 = Course(470, 4, [cs302, cs312, cs325], True, 0)
cs470.session(Session(2, ))
cs470.session(Session(5, ))
cs470.session(Session(8, ))

cs480 = Course(480, 4, [cs325, cs380, cs420], True, 0) #  This actually lists cs420 -OR- cs446, not sure how to represent...
cs480.session(Session(1, ))
cs480.session(Session(1, ))
cs480.session(Session(4, ))
cs480.session(Session(4, ))
cs480.session(Session(7, ))
cs480.session(Session(7, ))

cs481 = Course(481, 4, [cs480], True, 0)
cs481.session(Session(2, ))
cs481.session(Session(5, ))
cs481.session(Session(8, ))

cs489 = Course(489, 1, [cs325], True, 0)
cs489.session(Session(2, ))
cs489.session(Session(3, ))
cs489.session(Session(5, ))
cs489.session(Session(6, ))
cs489.session(Session(8, ))
cs489.session(Session(9, ))

cs492 = Course(492, 2, None, True, 0)
cs492.session(Session(1, ))
cs492.session(Session(2, ))
cs492.session(Session(3, ))
cs492.session(Session(4, ))
cs492.session(Session(5, ))
cs492.session(Session(6, ))
cs492.session(Session(7, ))
cs492.session(Session(8, ))
cs492.session(Session(9, ))


# Typical Elective Courses
cs105 = Course(105, 4, None, False, 0)

cs250 = Course(250, 4, None, False, 0)
cs250.session(Session(1, ))
cs250.session(Session(4, ))
cs250.session(Session(7, ))

# cs255 = Course(255, 4, [cs111], False, 0)

cs351 = Course(351, 4, [cs250], False, 0)
cs351.session(Session(2, ))
cs351.session(Session(5, ))
cs351.session(Session(8, ))

cs352 = Course(352, 4, [cs351], False, 0)
cs351.session(Session(3, ))
cs351.session(Session(6, ))
cs351.session(Session(9, ))

cs367 = Course(367, 4, [cs105], False, 0)
cs367.session(Session(3, ))
cs367.session(Session(6, ))
cs367.session(Session(9, ))

# cs370 = Course(370, 4, None, False, 0)

# cs375 = Course(375, 4, [cs301], False, 0)

cs440 = Course(440, 4, [cs302], False, 0)
cs440.session(Session(4, ))

cs441 = Course(441, 4, [cs440], False, 0)
cs441.session(Session(2, ))
cs441.session(Session(8, ))

cs442 = Course(442, 4, [cs302], False, 0)
cs442.session(Session(3, ))
cs442.session(Session(9, ))

cs450 = Course(450, 4, [cs301], False, 0)
cs450.session(Session(4, ))

cs455 = Course(455, 4, [cs302], False, 0)
cs455.session(Session(1, ))
cs455.session(Session(7, ))

# cs460 = Course(460, 4, [cs301], False, 0)

cs473 = Course(473, 4, [cs361, cs427], False, 0)
cs473.session(Session(5, ))

# cs456 = Course(456, 4, [cs420], False, 0)

# cs457 = Course(457, 4, [cs302, cs362], False, 0)

# cs445 = Course(445, 4, [cs440], False, 0)

# cs430 = Course(430, 4, None, False, 0)

# cs475 = Course(475, 4, None, False, 0)

# cs476 = Course(476, 4, [cs302], False, 0)
