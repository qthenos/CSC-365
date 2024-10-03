# import unittest
# from schoolsearch_v2 import (
#     read_file,
#     find_student_class,
#     find_student_bus,
#     find_teacher_students,
#     students_take_bus,
#     students_at_grade,
#     average_gpa_of_grade,
#     find_gpa_high,
#     find_gpa_low,
#     student_info,
# )

# class TestSchoolSearch(unittest.TestCase):
#     def setUp(self):
#         self.test_data = read_file()

#     def test_TC1(self):
#         result = find_student_class("HAVIR", self.test_data)
#         self.assertEqual(result, [("HAVIR", "BOBBIE", '2', '108', 'HAMER', 'GAVIN\n')])
    
#     def test_TC2(self):
#         result = find_student_class("NEMO", self.test_data)
#         self.assertEqual(result, [])

#     #TC3 needs to be tested manually

#     def test_TC4(self):
#         result = find_student_bus("HAVIR", self.test_data)
#         self.assertEqual(result, [('HAVIR', 'BOBBIE', '0')])
    
#     #TC5 needs to be tested manually
        
#     def test_TC6(self):
#         result = find_teacher_students("HANTZ", self.test_data)
#         self.assertEqual(result, [
#             ("CORKER", "CARTER"),  ("IMMERMAN", "DEVIN"), ("RAPOSE","ALONZO"), ("OGAS","ERVIN"), ("MASSART","ELDON"), ("BEX","TAMESHA")
#             ])
        
#     def test_TC7(self):
#         result = find_teacher_students("nobody", self.test_data)
#         self.assertEqual(result, [])

#     def test_TC8(self):
#         result = students_at_grade("1", self.test_data)
#         self.assertEqual(result, [
#             ["SAELEE","DANILO","1","103","54","2.85","FALKER","ADOLPH\n"],
#             ["GARTH","JOHN","1","103","0","3.14","FALKER","ADOLPH\n"]
#         ])
    
#     def test_TC9(self):
#         result = students_at_grade("0", self.test_data)
#         self.assertEqual(result, [])
        
#     def test_TC10(self):
#         result = students_take_bus("0", self.test_data)
#         self.assertEqual(result, 
#                 [("SCHOENECKER","PHUONG","6","109")
#                 , ("FINCHMAN","MATHILDA","6","111")
#                 , ("BRODERSEN","HYE","3","110")
#                 , ("HAVIR","BOBBIE","2","108")
#                 , ("MASSART","ELDON","4","105")
#                 , ("GARTH","JOHN","1","103")
#                 , ("CREMEANS","RANDOLPH","6","109")
#                 , ("KREESE","CARRIE","6","109")])

#     def test_TC11(self):
#         result = students_take_bus(101, self.test_data)
#         self.assertEqual(result, [])

#     def test_TC12(self):
#         result = find_gpa_high("2", self.test_data)
#         self.assertEqual(result, [["WICINSKY","TERESE","2","108","53","3.22","HAMER","GAVIN\n"]])

#     def test_TC13(self):
#         result = find_gpa_high("0", self.test_data)
#         self.assertEqual(result, [])
        
#     def test_TC14(self):
#         result = find_gpa_low("1", self.test_data)
#         self.assertEqual(result, [["SAELEE","DANILO","1","103","54","2.85","FALKER","ADOLPH\n"]])

#     def test_TC15(self):
#         result = average_gpa_of_grade("2", self.test_data)
#         self.assertEqual(result, 2.95)

#     def test_TC16(self):
#         result = average_gpa_of_grade("0", self.test_data)
#         self.assertEqual(result, "")

#     def test_TC17(self):
#         result = student_info(self.test_data)
#         self.assertEqual(result, [(0, 0), (1, 2), (2, 13), (3, 9), (4, 15), (5, 0), (6, 21)])

#     #TC-18 has to be tested manually
#     #TC-19 has to be tested manually    

# if __name__ == "__main__":
#     unittest.main()