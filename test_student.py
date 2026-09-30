from unittest import TestCase
from Student import Student

class TestStudent(TestCase):
    def test_that_student_can_be_introduced(self):
        student = Student("Beatrice", 6)
        self.assertEqual(student.introduce(),"Student name is Beatrice and grade is 6")

    def test_that_student_can_be_promoted(self):
        student = Student("Beatrice", 6)
        self.assertEqual(student.promote(),f"Student grade has been promoted to 7")

    def test_that_student_has_passed(self):
        student = Student("Beatrice", 6)
        student.score = 120
        self.assertTrue(student.has_passed(),100)

    def test_that_student_name_can_be_updated(self):
        student = Student("Beatrice", 6)
        student.update_name("Lea")
        self.assertEqual(student.update_name("Lea"), f"Student name has been updated to Lea")

    def test_that_student_is_graduating(self):
        student = Student("Beatrice", 12)
        self.assertTrue( student.is_graduating())


