#free diddy
# Paul Nassar & Andy Duong
#Reference:     StLastName, StFirstName, Grade, Classroom, Bus, GPA, TLastName, TFirstName

#TODO
"""
• Given a student’s last name, find the student’s grade, classroom and teacher (if there is more than one student with the same last name, find this information for all students);
• Given a student’s last name, find the bus route the student takes (if there is more than one student with the same last name, find this information for all matching students);
• Given a teacher, find the list of students in his/her class;
• Given a bus route, find all students who take it;
• Find all students at a specified grade level. 
• For a given grade level find the average GPA of students in that grade.
• In a given grade level find the student with the highest (lowest) GPA.
"""



#function for reading in the data
def read_file():
    file = open("students.txt", "r")
    data = []
    for line in file:
        current_line = line.split(",")
        data.append(current_line)
    return data

def find_student_class(lastname: str, data: list):
    students = []
    for line in data:
        if line[0] == lastname:
            class_data = [line[2], line[3], line[6], line[7]]
            students.append(class_data)
    return students

def find_student_bus(lastname: str, data: list):
    busses = []
    for line in data:
        if line[0] == lastname:
            busses.append(line[4])
    return busses

def find_teacher_students(lastname: str, data: list):
    students = []
    for line in data:
        if line[6] == lastname:
            students.append(line)
    return students

def students_take_bus(bus_route: int, data : list):
    students = []
    for student in data:
        if student[4] == bus_route:
            students.append(student)
    return students

def students_at_grade(grade: int, data: list):
    students = []
    for line in data:
        if line[2] == grade:
            students.append(line)
    return students

def average_gpa_of_grade(grade: int, data: list):
    gpa_sum = 0
    count = 0
    for line in data:
        if line[2] == grade:
            gpa_sum += line[5]
            count += 1
    return gpa_sum / count

def find_gpa_high(grade: int, data: list):
    high = data[0]
    for line in data:
        if line[2] == grade:
            if line[5] > high[5]:
                high = line
    return high

def find_gpa_low(grade: int, data: list):
    low = data[0]
    for line in data:
        if line[2] == grade:
            if line[5] < low[5]:
                low = line
    return low

if __name__ == "__main__":
    print("hello")
    print(read_file())
    print("goodbye")