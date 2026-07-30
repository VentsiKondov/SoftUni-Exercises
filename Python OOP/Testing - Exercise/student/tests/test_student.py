from project.student import Student
import unittest
class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Mitko", None)
        self.student1 = Student("Mitko", {"Math": ["A"]})

    def test_init(self):
        self.assertEqual(self.student.name, "Mitko")
        self.assertEqual(self.student.courses, {})
        self.assertEqual(self.student1.courses, {"Math": ["A"]})

    def test_enroll_method_with_existing_name(self):
        self.student.courses = {"Math": []}
        self.assertEqual(self.student.enroll("Math", "", ), "Course already added. Notes have been updated.")
        self.assertEqual(self.student.courses, {"Math": []} )

    def test_enroll_method_with_add_course_notes_string(self):
        self.student.courses = {}
        self.student.enroll("Math", "", "")
        self.assertEqual(self.student.courses, {"Math": ""} )
        self.assertEqual(self.student.enroll("Bio", "ABC", ""), "Course and course notes have been added.")


    def test_enroll_method_with_add_course_notes(self):
        self.student.courses = {}
        self.assertEqual(self.student.enroll("Math", "ABC", "Y"), "Course and course notes have been added.")
        self.assertEqual(self.student.enroll("Bio", "ABC", ""), "Course and course notes have been added.")
        self.assertEqual(self.student.courses, {"Bio": "ABC", "Math": "ABC"} )

    def test_enroll_method_with_no_add_and_not_in_dict(self):
        self.student.courses = {}
        self.assertEqual(self.student.enroll("Math", "ABC", "B"), "Course has been added.")
        self.student.enroll("Math", "ABC", "B")
        self.assertEqual(self.student.courses, {"Math": ["A", "B", "C"]} )

    def test_add_notes_method_exception(self):
        self.student.courses = {"Math": ["A", "B", "C"]}
        with self.assertRaises(Exception) as context:
            self.student.add_notes("Bio", "")
        self.assertEqual(str(context.exception), "Cannot add notes. Course not found.")

    def test_add_notes_method_without_exception(self):
        self.student.courses = {"Math": ["A", "B", "C"]}
        self.student.add_notes("Math", "C")
        self.assertEqual(self.student.courses, {"Math": ["A", "B", "C", "C"]})
        self.student.add_notes("Math", "CB")
        self.assertEqual(self.student.courses, {"Math": ["A", "B", "C", "C", "CB"]})

    def test_leave_course_method_exception(self):
        self.student.courses = {}
        with self.assertRaises(Exception) as context:
            self.student.leave_course("Math")
        self.assertEqual(str(context.exception), "Cannot remove course. Course not found.")

    def test_leave_course_method_without_exception(self):
        self.student.courses = {"Math": ["A", "B", "C"]}
        self.student.leave_course("Math")
        self.assertEqual(self.student.courses, {})

if __name__ == '__main__':
    unittest.main()