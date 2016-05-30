from Professor import *


class Course:
    instances = list()
    requiredCourses = list()
    electiveCourses = list()

    def __init__(self, code, credit_count, prereq_codes, required, rating):
        self.code = code
        self.credits = credit_count
        self.prereq_codes = prereq_codes
        self.required = required
        self.rating = rating
        self.sessions = list()
        self.instances.append(self)
        if self.required:
            self.requiredCourses.append(self)
        else:
            self.electiveCourses.append(self)
        # TODO: Write better code for prereq detection. Expand ALL prereqs, not just what is listed.

    def __str__(self):
        return self.code + " " + str(self.credits)

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
    def __init__(self, quarter, professor=unknown):
        self.quarter = quarter
        self.professor = professor
        self.course = None

    def __str__(self):
        return str(self.course.code) + " " + repr(self.quarter) + " " + str(self.professor)

    def add_code(self, code):
        self.course = code

    def get_professor(self):
        return self.professor

    def get_quarter(self):
        return self.quarter


math172 = Course('ma172', 5, None, True, 0)
math172.session(Session(1))
math172.session(Session(2))
math172.session(Session(3))
math172.session(Session(4))
math172.session(Session(5))
math172.session(Session(6))
math172.session(Session(7))
math172.session(Session(8))
math172.session(Session(9))

math260 = Course('ma260', 5, [math172], True, 0)
math260.session(Session(1))
math260.session(Session(2))
math260.session(Session(3))
math260.session(Session(4))
math260.session(Session(5))
math260.session(Session(6))
math260.session(Session(7))
math260.session(Session(8))
math260.session(Session(9))

math330 = Course('ma330', 5, [math260], True, 0)
math330.session(Session(1))
math330.session(Session(2))
math330.session(Session(3))
math330.session(Session(4))
math330.session(Session(5))
math330.session(Session(6))
math330.session(Session(7))
math330.session(Session(8))
math330.session(Session(9))

cs110 = Course('cs110', 4, None, True, 0)
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

cs111 = Course('cs111', 4, [cs110], True, 0)
cs111.session(Session(2, ))
cs111.session(Session(2, ))
cs111.session(Session(3, ))
cs111.session(Session(5, ))
cs111.session(Session(5, ))
cs111.session(Session(6, ))
cs111.session(Session(8, ))
cs111.session(Session(8, ))
cs111.session(Session(9, ))

cs112 = Course('cs112', 4, None, False, 0)
cs112.session(Session(1, ))
cs112.session(Session(3, ))
cs112.session(Session(4, ))
cs112.session(Session(6, ))
cs112.session(Session(7, ))
cs112.session(Session(9, ))

cs301 = Course('cs301', 4, [cs111], True, 0)
cs301.session(Session(1, ))
cs301.session(Session(1, ))
cs301.session(Session(4, ))
cs301.session(Session(4, ))
cs301.session(Session(7, ))
cs301.session(Session(7, ))

cs302 = Course('cs302', 4, [cs301], True, 0)
cs302.session(Session(2, ))
cs302.session(Session(2, ))
cs302.session(Session(5, ))
cs302.session(Session(5, ))
cs302.session(Session(8, ))
cs302.session(Session(8, ))

cs311 = Course('cs311', 4, [cs110], True, 0)
cs311.session(Session(1, davendra))
cs311.session(Session(1, davendra))
cs311.session(Session(3, davendra))
cs311.session(Session(3, davendra))
cs311.session(Session(4, ))
cs311.session(Session(4, ))
cs311.session(Session(6, ))
cs311.session(Session(6, ))
cs311.session(Session(7, ))
cs311.session(Session(7, ))
cs311.session(Session(9, ))
cs311.session(Session(9, ))

cs312 = Course('cs312', 4, [cs301, cs311], True, 0)
cs312.session(Session(1, ))
cs312.session(Session(2, davendra))
cs312.session(Session(2, davendra))
cs312.session(Session(4, ))
cs312.session(Session(5, ))
cs312.session(Session(5, ))
cs312.session(Session(7, ))
cs312.session(Session(8, ))
cs312.session(Session(8, ))

cs325 = Course('cs325', 3, [cs301], True, 0)
cs325.session(Session(2, ))
cs325.session(Session(3, ))
cs325.session(Session(5, ))
cs325.session(Session(6, ))
cs325.session(Session(8, ))
cs325.session(Session(9, ))

cs361 = Course('cs361', 4, [cs302], True, 0)
cs361.session(Session(1, ))
cs361.session(Session(1, ))
cs361.session(Session(4, ))
cs361.session(Session(4, ))
cs361.session(Session(7, ))
cs361.session(Session(7, ))

cs362 = Course('cs362', 4, [cs361], True, 0)
cs362.session(Session(2, ))
cs362.session(Session(2, ))
cs362.session(Session(5, ))
cs362.session(Session(5, ))
cs362.session(Session(8, ))
cs362.session(Session(8, ))

cs380 = Course('cs380', 4, [cs302], True, 0)
cs380.session(Session(1, ))  # This is made up, I can't find it anywhere on the schedules
cs380.session(Session(1, ))  # This is made up, I can't find it anywhere on the schedules
cs380.session(Session(1, ))  # This is made up, I can't find it anywhere on the schedules
cs380.session(Session(1, ))  # This is made up, I can't find it anywhere on the schedules
cs380.session(Session(1, ))  # This is made up, I can't find it anywhere on the schedules
cs380.session(Session(1, ))  # This is made up, I can't find it anywhere on the schedules

cs392 = Course('cs392', 1, None, True, 0)
cs392.session(Session(1, unknown))
cs392.session(Session(2, unknown))
cs392.session(Session(3, unknown))
cs392.session(Session(4, unknown))
cs392.session(Session(5, unknown))
cs392.session(Session(6, unknown))
cs392.session(Session(7, unknown))
cs392.session(Session(8, unknown))
cs392.session(Session(9, unknown))

cs427 = Course('cs427', 4, [cs302, cs325], True, 0)
cs427.session(Session(1, kovalerchuk))
cs427.session(Session(1, ))
cs427.session(Session(4, ))
cs427.session(Session(4, ))
cs427.session(Session(7, ))
cs427.session(Session(7, ))

cs420 = Course('cs420', 4, [cs302, cs325], False, 0)
cs420.session(Session(3, ))
cs420.session(Session(6, ))
cs420.session(Session(9, ))

# cs446 = Course('cs446', 4, [cs302], False, 0)

cs470 = Course('cs470', 4, [cs302, cs312, cs325], True, 0)
cs470.session(Session(2, vajda))
cs470.session(Session(5, ))
cs470.session(Session(8, ))

cs480 = Course('cs480', 4, [cs325, cs380, cs420], True, 0)  # This actually lists cs420 -OR- cs446
cs480.session(Session(1, vajda))
cs480.session(Session(1, vajda))
cs480.session(Session(4, ))
cs480.session(Session(4, ))
cs480.session(Session(7, ))
cs480.session(Session(7, ))

cs481 = Course('cs481', 4, [cs480], True, 0)
cs481.session(Session(2, davendra))
cs481.session(Session(5, vajda))
cs481.session(Session(8, ))

cs489 = Course('cs489', 1, [cs325], True, 0)
cs489.session(Session(2, ))
cs489.session(Session(3, ))
cs489.session(Session(5, ))
cs489.session(Session(6, ))
cs489.session(Session(8, ))
cs489.session(Session(9, ))

cs492 = Course('cs492', 2, None, True, 0)
cs492.session(Session(1, unknown))
cs492.session(Session(2, unknown))
cs492.session(Session(3, unknown))
cs492.session(Session(4, unknown))
cs492.session(Session(5, unknown))
cs492.session(Session(6, unknown))
cs492.session(Session(7, unknown))
cs492.session(Session(8, unknown))
cs492.session(Session(9, unknown))


# Typical Elective Courses
cs105 = Course('cs105', 4, None, False, 0)
cs105.session(Session(1))
cs105.session(Session(2))
cs105.session(Session(3))
cs105.session(Session(4))
cs105.session(Session(5))
cs105.session(Session(6))
cs105.session(Session(7))
cs105.session(Session(8))
cs105.session(Session(9))

cs250 = Course('cs250', 4, None, False, 0)
cs250.session(Session(1, ))
cs250.session(Session(4, ))
cs250.session(Session(7, ))

# cs255 = Course('cs255', 4, [cs111], False, 0)

cs351 = Course('cs351', 4, [cs250], False, 0)
cs351.session(Session(2, ))
cs351.session(Session(5, ))
cs351.session(Session(8, ))

cs352 = Course('cs352', 4, [cs351], False, 0)
cs352.session(Session(3, ))
cs352.session(Session(6, ))
cs352.session(Session(9, ))

cs367 = Course('cs367', 4, [cs105], False, 0)
cs367.session(Session(3, ))
cs367.session(Session(6, ))
cs367.session(Session(9, ))

# cs370 = Course('cs370', 4, None, False, 0)

# cs375 = Course('cs375', 4, [cs301], False, 0)

cs440 = Course('cs440', 4, [cs302], False, 0)
cs440.session(Session(4, kovalerchuk))

cs441 = Course('cs441', 4, [cs440], False, 0)
cs441.session(Session(2, ))
cs441.session(Session(8, ))

cs442 = Course('cs442', 4, [cs302], False, 0)
cs442.session(Session(3, ))
cs442.session(Session(9, ))

cs450 = Course('cs450', 4, [cs301], False, 0)
cs450.session(Session(4, ))

cs455 = Course('cs455', 4, [cs302], False, 0)
cs455.session(Session(1, kovalerchuk))
cs455.session(Session(7, kovalerchuk))

# cs460 = Course('cs460', 4, [cs301], False, 0)

cs473 = Course('cs473', 4, [cs361, cs427], False, 0)
cs473.session(Session(5, ))

# cs456 = Course('cs456', 4, [cs420], False, 0)

# cs457 = Course('cs457', 4, [cs302, cs362], False, 0)

# cs445 = Course('cs445', 4, [cs440], False, 0)

# cs430 = Course('cs430', 4, None, False, 0)

cs471 = Course('cs471', 4, None, False, 0)
cs471.session(Session(1, davendra))

# cs475 = Course('cs475', 4, None, False, 0)

# cs476 = Course('cs476', 4, [cs302], False, 0)
