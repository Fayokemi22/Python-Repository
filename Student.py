class Student:
    def __init__(self, student_name, student_grade):
        self.student_name = student_name
        self.student_grade = student_grade
        self.score = 100

    def introduce(self):
        return f"Student name is {self.student_name} and grade is {self.student_grade}"

    def promote(self):
        self.student_grade += 1
        return f"Student grade has been promoted to {self.student_grade}"

    def has_passed(self):
        if self.score <= 100:
            return False
        else:
            return True

    def update_name(self,new_name):
        self.student_name = new_name
        return f"Student name has been updated to {self.student_name}"


    def is_graduating(self):
        if self.student_grade == 12:
            return True
        else:
            return False
