import unittest
from schoolsearch import (
    find_student_class,
    find_student_bus,
    find_teacher_students,
    students_take_bus,
    students_at_grade,
    average_gpa_of_grade,
    find_gpa_high,
    find_gpa_low,
    student_info,
)

class TestSchoolSearch(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            ["SMITH", "JOHN", "3", "102", "22", "3.2", "BONITA", "AMY"],
            ["DOE", "JANE", "4", "203", "22", "3.5", "BROWN", "CHARLIE"],
            ["SMITH", "EMILY", "3", "102", "15", "3.9", "BONITA", "AMY"],
            ["KINGSTON", "MICHAEL", "4", "203", "17", "2.8", "BROWN", "CHARLIE"],
        ]

    def test_find_student_class(self):
        result = find_student_class("SMITH", self.test_data)
        self.assertEqual(result, [("SMITH", "JOHN", '3', '102', 'BONITA', 'AMY'), ("SMITH", "EMILY",'3', '102', 'BONITA', 'AMY')])

    def test_find_student_bus(self):
        result = find_student_bus("DOE", self.test_data)
        self.assertEqual(result, [('DOE', 'JANE', '22')])

    def test_find_teacher_students(self):
        result = find_teacher_students("BONITA", self.test_data)
        self.assertEqual(result, [("SMITH", "JOHN"),("SMITH", "EMILY")])

    def test_students_take_bus(self):
        result = students_take_bus("22", self.test_data)
        self.assertEqual(result, [('SMITH', 'JOHN', '3', '102'), ('DOE', 'JANE', '4', '203')])

    def test_students_at_grade(self):
        result = students_at_grade("3", self.test_data)
        self.assertEqual(result, [('SMITH', 'JOHN'), ('SMITH', 'EMILY')])

    def test_average_gpa_of_grade(self):
        result = average_gpa_of_grade("4", self.test_data)
        self.assertAlmostEqual(result, 3.15)

    def test_find_gpa_high(self):
        result = find_gpa_high("3", self.test_data)
        self.assertEqual(result, ['SMITH', 'EMILY', '3', '102', '15', '3.9', 'BONITA', 'AMY'])

    def test_find_gpa_low(self):
        result = find_gpa_low("4", self.test_data)
        self.assertEqual(result, ['KINGSTON', 'MICHAEL', '4', '203', '17', '2.8', 'BROWN', 'CHARLIE'])

    def test_student_info(self):
        result = student_info(self.test_data)
        self.assertEqual(result, [(0, 0), (1, 0), (2, 0), (3, 2), (4, 2), (5, 0), (6, 0)])

    def test_invalid_bus_route(self):
        # Testing a bus route that doesn't exist
        result = students_take_bus("67", self.test_data)
        self.assertEqual(result, [])

    def test_invalid_student_lastname(self):
        # Testing a student last name that doesn't exist
        result = find_student_class("Nobody", self.test_data)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()