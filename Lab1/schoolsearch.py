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
        if len(current_line) < 8:
            return []
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
            busses.append(line[0], line[1], line[4])
    return busses

def find_teacher_students(lastname: str, data: list):
    students = []
    for line in data:
        if line[6] == lastname:
            students.append(line)
    return students

def students_take_bus(bus_route: int, data : list):
    students = []
    for line in data:
        if line[4] == bus_route:
            students.append((line[0], line[1], line[2], line[3]))
    return students

def students_at_grade(grade: int, data: list, type=0):
    students = []
    for line in data:
        if line[2] == grade:
            students.append((line[0], line[1]))
    return students

def average_gpa_of_grade(grade: int, data: list):
    gpa_sum = 0
    count = 0
    for line in data:
        if line[2] == grade:
            gpa_sum += float(line[5])
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

def student_info(data: list):
    results = []
    for i in range(7):
        counter = 0
        for line in data:
            if int(line[2]) == i:
                counter += 1
        results.append((i, counter))
    return results



if __name__ == "__main__":
    userIn = ""
    table_data = read_file()
    if table_data:
        while True:
            userIn = input("Your wish is my command!\n")
            data = userIn.split()

            if data[0].lower() == "s":
                if len(data) < 3:
                    print(find_student_class(data[1], table_data))
                else:
                    print(find_student_bus(data[1], table_data))

            elif data[0].lower() == "t":
                print(find_teacher_students(data[1], table_data))

            elif data[0].lower() == "g":
                if len(data) < 3:
                    print(students_at_grade(data[1], table_data))
                else:
                    if data[2].lower() == "h":
                        print(find_gpa_high(data[1], table_data))
                    elif data[2].lower() == "l":
                        print(find_gpa_low(data[1], table_data))

            elif data[0].lower() == "b":
                print(students_take_bus(data[1]), table_data)
            elif data[0].lower() == "a":
                print(average_gpa_of_grade(data[1], table_data))
            elif data[0].lower() == "i":
                print(student_info(table_data))
            elif data[0].lower() == "q":
                print("Quitting...!")
                break
    else:
        print("students.txt has the wrong format")