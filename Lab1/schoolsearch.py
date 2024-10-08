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
        if line[0] == lastname.upper():
            class_data = (line[0], line[1], line[2], line[3], line[6], line[7])
            students.append(class_data)
    return students

def find_student_bus(lastname: str, data: list):
    busses = []
    for line in data:
        if line[0] == lastname.upper():
            busses.append((line[0], line[1], line[4]))
    return busses

def find_teacher_students(lastname: str, data: list):
    students = []
    for line in data:
        if line[6] == lastname.upper():
            students.append((line[0], line[1]))
    return students

def students_take_bus(bus_route: str, data : list):
    students = []
    for line in data:
        if line[4] == bus_route:
            students.append((line[0], line[1], line[2], line[3]))
    return students

def students_at_grade(grade: str, data: list):
    students = []
    for line in data:
        if line[2] == grade:
            students.append(line)
    return students

def average_gpa_of_grade(grade: str, data: list):
    gpa_sum = 0
    count = 0
    for line in data:
        if line[2] == grade:
            gpa_sum += float(line[5])
            count += 1
    if count == 0:
        return ""
    else:
        return round(gpa_sum / count, 2)

def find_gpa_high(grade: str, data: list):
    if students_at_grade(grade, data) == []:
        return []
    else:
        high = students_at_grade(grade, data)[0]
        for line in data:
            if line[2] == grade:
                if line[5] > high[5]:
                    high = line
        return [high]

def find_gpa_low(grade: str, data: list):
    if students_at_grade(grade, data) == []:
        return []
    else:
        low = students_at_grade(grade, data)[0]
        for line in data:
            if line[2] == grade:
                if line[5] < low[5]:
                    low = line
        return [low]

def student_info(data: list):
    results = []
    for i in range(7):
        counter = 0
        for line in data:
            if int(line[2]) == i:
                counter += 1
        results.append((i, counter))
    return results

def print_studs(studs: list):
    for stud in studs:
        print(",".join(stud)) if stud else print("")

def main():
    table_data = read_file()
    
    if not table_data:
        print("students.txt has the wrong format")
        return

    while True:
        userIn = input("Your wish is my command!\n").strip().lower()
        data = userIn.split()

        if not data:
            print("Unknown command, please try again.")
            continue
        
        command = data[0]

        if command == "s":
            if len(data) < 4:
                stud = find_student_class(data[2], table_data)
                print_studs(stud)
            else:
                if data[3] == "b":
                    stud = find_student_bus(data[2], table_data)
                    print_studs(stud)
                else:
                    print("Unknown command. Please try again.")

        elif command == "t":
            stud = find_teacher_students(data[2], table_data)
            print_studs(stud)

        elif command == "g":
            if len(data) < 4:
                stud = [(line[0], line[1]) for line in students_at_grade(data[2], table_data)]
                print_studs(stud)
            else:
                if data[3].lower() == "h":
                    stud = find_gpa_high(data[2], table_data)
                    print_studs(stud)
                elif data[3].lower() == "l":
                    stud = find_gpa_low(data[2], table_data)
                    print_studs(stud)

        elif command == "b":
            stud = students_take_bus(data[2], table_data)
            print_studs(stud)
        elif command == "a":
            print(average_gpa_of_grade(data[2], table_data))
        elif command == "i":
            info = [f'{line[0]}:{line[1]}' for line in student_info(table_data)]
            print(", ".join(info))
        elif command == "q":
            print("Quitting...!")
            break
        else:
            print("Unknown command. Please try again.")

    

if __name__ == "__main__":
    main()