import unittest
from schoolsearch_v2 import (
    read_file,
    find_student_class,
    find_student_bus,
    find_teacher_students,
    students_take_bus,
    students_at_grade,
    average_gpa_of_grade,
    find_gpa_high,
    find_gpa_low,
    student_info,
    students_in_class,
    teachers_in_class,
    teachers_in_grade,
    enrollments_report,
    grade_analytics,
    teacher_analytics,
    bus_analytics
)

class TestSchoolSearch(unittest.TestCase):
    def setUp(self):
        self.stud_data = read_file("list.txt")
        self.teacher_data = read_file("teachers.txt")

    def test_TC1(self):
        result = find_student_class("HAVIR", self.stud_data, self.teacher_data)
        self.assertEqual(result, [("HAVIR", "BOBBIE", '2', '108', 'HAMER', 'GAVIN')])
    
    def test_TC2(self):
        result = find_student_class("NEMO", self.stud_data, self.teacher_data)
        self.assertEqual(result, [])

    #TC3 needs to be tested manually

    def test_TC4(self):
        result = find_student_bus("HAVIR", self.stud_data)
        self.assertEqual(result, [('HAVIR', 'BOBBIE', '0')])
    
    #TC5 needs to be tested manually
        
    def test_TC6(self):
        result = find_teacher_students("HANTZ", self.stud_data, self.teacher_data)
        self.assertEqual(result, [
            ("CORKER", "CARTER"),  ("IMMERMAN", "DEVIN"), ("RAPOSE","ALONZO"), ("OGAS","ERVIN"), ("MASSART","ELDON"), ("BEX","TAMESHA")
            ])
        
    def test_TC7(self):
        result = find_teacher_students("nobody", self.stud_data, self.teacher_data)
        self.assertEqual(result, [])

    def test_TC8(self):
        result = students_at_grade("1", self.stud_data, self.teacher_data)
        self.assertEqual(result, [
            ["SAELEE","DANILO","1","103","54","2.85","FALKER","ADOLPH"],
            ["GARTH","JOHN","1","103","0","3.14","FALKER","ADOLPH"]
        ])
    
    def test_TC9(self):
        result = students_at_grade("0", self.stud_data, self.teacher_data)
        self.assertEqual(result, [])
        
    def test_TC10(self):
        result = students_take_bus("0", self.stud_data)
        self.assertEqual(result, 
                [("SCHOENECKER","PHUONG","6","109")
                , ("FINCHMAN","MATHILDA","6","111")
                , ("BRODERSEN","HYE","3","110")
                , ("HAVIR","BOBBIE","2","108")
                , ("MASSART","ELDON","4","105")
                , ("GARTH","JOHN","1","103")
                , ("CREMEANS","RANDOLPH","6","109")
                , ("KREESE","CARRIE","6","109")])

    def test_TC11(self):
        result = students_take_bus(101, self.stud_data)
        self.assertEqual(result, [])

    def test_TC12(self):
        result = find_gpa_high("2", self.stud_data, self.teacher_data)
        self.assertEqual(result, [["WICINSKY","TERESE","2","108","53","3.22","HAMER","GAVIN"]])

    def test_TC13(self):
        result = find_gpa_high("0", self.stud_data, self.teacher_data)
        self.assertEqual(result, [])
        
    def test_TC14(self):
        result = find_gpa_low("1", self.stud_data, self.teacher_data)
        self.assertEqual(result, [["SAELEE","DANILO","1","103","54","2.85","FALKER","ADOLPH"]])

    def test_TC15(self):
        result = average_gpa_of_grade("2", self.stud_data)
        self.assertEqual(result, 2.95)

    def test_TC16(self):
        result = average_gpa_of_grade("0", self.stud_data)
        self.assertEqual(result, "")

    def test_TC17(self):
        result = student_info(self.stud_data)
        self.assertEqual(result, [(0, 0), (1, 2), (2, 13), (3, 9), (4, 15), (5, 0), (6, 21)])

    #TC-18 has to be tested manually
    #TC-19 has to be tested manually    

    def test_TC20(self):
        result = students_in_class("105", self.stud_data, self.teacher_data)
        self.assertEqual(result, [['CORKER', 'CARTER', '4', '105', '53', '3.12', 'HANTZ', 'JED'], 
                                  ['IMMERMAN', 'DEVIN', '4', '105', '52', '2.78', 'HANTZ', 'JED'], 
                                  ['RAPOSE', 'ALONZO', '4', '105', '51', '3.12', 'HANTZ', 'JED'], 
                                  ['OGAS', 'ERVIN', '4', '105', '54', '2.84', 'HANTZ', 'JED'], 
                                  ['MASSART', 'ELDON', '4', '105', '0', '2.8', 'HANTZ', 'JED'], 
                                  ['BEX', 'TAMESHA', '4', '105', '55', '2.82', 'HANTZ', 'JED']])
    def test_TC21(self):
        result = students_in_class("115", self.stud_data, self.teacher_data)
        self.assertEqual(result, [])

    def test_TC22(self):
        result = teachers_in_class("105", self.teacher_data)
        self.assertEqual(result, [('HANTZ', 'JED')])
    def test_TC23(self):
        result = teachers_in_class("115", self.teacher_data)
        self.assertEqual(result, [])
    def test_TC24(self):
        result = teachers_in_grade("3", self.stud_data, self.teacher_data)
        self.assertEqual(result, [('FAFARD', 'ROCIO', '107'), ('ALPERT', 'JONATHAN', '110')])
    def test_TC25(self):
        result = teachers_in_grade("7", self.stud_data, self.teacher_data)
        self.assertEqual(result, [])
    def test_TC26(self):
        result = enrollments_report(self.stud_data)
        self.assertEqual(result, {'101': 1, '102': 5, '103': 2, '104': 2, '105': 6, '106': 2, '107': 7, '108': 11, '109': 5, '110': 2, '111': 9, '112': 8})
    def test_TC27(self):
        result = grade_analytics(self.stud_data)
        self.assertEqual(result, {'1': 3.0, '2': 2.95, '3': 3.05, '4': 2.95, '6': 2.98})
    def test_TC28(self):
        result = teacher_analytics(self.stud_data, self.teacher_data)
        self.assertEqual(result, {"('ALPERT', 'JONATHAN')": 3.17, "('BODZIONY', 'LUZ')": 3.09, 
                                  "('CHIONCHIO', 'PERLA')": 2.98, "('COOL', 'REUBEN')": 2.91, 
                                  "('FAFARD', 'ROCIO')": 3.01, "('FALKER', 'ADOLPH')": 3.0, 
                                  "('GAMBREL', 'JAE')": 2.96, "('HAMER', 'GAVIN')": 2.95, 
                                  "('HANTZ', 'JED')": 2.91, "('KERBS', 'BENITO')": 2.98, 
                                  "('NISTENDIRK', 'NANCY')": 2.96, "('STEIB', 'GALE')": 2.9})
    def test_TC29(self):
        result = bus_analytics(self.stud_data)
        self.assertEqual(result, {'0': 2.95, '51': 3.02, '52': 2.88, '53': 3.06, '54': 2.94, '55': 3.04, '56': 2.92})


if __name__ == "__main__":
    unittest.main()