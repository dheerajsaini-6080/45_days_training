"""
Q3: Learner Class
"""


class Learner:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def summary(self):
        return f"{self.name} is enrolled in {self.course}"


student = Learner("Dheeraj", "AI & DS")

print(student.summary())