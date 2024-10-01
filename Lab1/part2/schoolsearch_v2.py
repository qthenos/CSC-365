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
def read_file(file_name):
    f_stud = open(file_name, "r")
    data = []
    for line in f_stud:
        current_line = line.split(",")
        data.append(current_line)
    return data

def find_teacher(classNum, teach_data:list):
    for line in teach_data:
        if classNum == line[2].strip():
            return [line[0], line[1]]
    return None

def find_student_class(lastname: str, stud_data: list, teach_data : list): #part2 done
    students = []
    for line in stud_data:
        if line[0] == lastname.upper():
            teacher = find_teacher(line[3], teach_data)
            class_data = (line[0], line[1], line[2], line[3], teacher[0], teacher[1])
            students.append(class_data)
    return students

def find_student_bus(lastname: str, stud_data: list): #part2 done
    busses = []
    for line in stud_data:
        if line[0] == lastname.upper():
            busses.append((line[0], line[1], line[4]))
    return busses

def find_teacher_students(lastname: str, stud_data: list, teach_data : list): #part2 done
    students = []
    classNum = 0
    for line in teach_data:
        if line[0] == lastname.upper():
            classNum = line[2].strip()
            break
    
    for line in stud_data:
        if line[3] == classNum:
            students.append((line[0], line[1]))
    return students

def students_take_bus(bus_route: str, stud_data : list): #part 2 done
    students = []
    for line in stud_data:
        if line[4] == bus_route:
            students.append((line[0], line[1], line[2], line[3]))
    return students

def students_at_grade(grade: str, stud_data: list, teach_data): #part2 done
    students = []
    for line in stud_data:
        if line[2] == grade:
            teacher = find_teacher(line[3], teach_data)
            students.append([line[0], line[1], line[2], line[3], line[4], line[5], teacher[0], teacher[1]])
    return students

def average_gpa_of_grade(grade: str, stud_data: list): #part 2 done
    gpa_sum = 0
    count = 0
    for line in stud_data:
        if line[2] == grade:
            gpa_sum += float(line[5])
            count += 1
    if count == 0:
        return ""
    else:
        return round(gpa_sum / count, 2)

def find_gpa_high(grade: str, stud_data: list, teach_data : list):#part 2 done
    students = students_at_grade(grade, stud_data, teach_data)
    if not students:
        return []
    
    high = students[0]
    for line in stud_data:
        if line[2] == grade:
            if line[5] > high[5]:
                high = line

    high[5] = high[5].strip()
    teacher = find_teacher(high[3], teach_data)
    high.append(teacher[0])
    high.append(teacher[1])
    return [high]

def find_gpa_low(grade: str, stud_data: list, teach_data : list): #part 2 done
    students = students_at_grade(grade, stud_data, teach_data)
    if not students:
        return []
    
    low = students[0]
    for line in stud_data:
        if line[2] == grade:
            if line[5] < low[5]:
                low = line
    low[5] = low[5].strip()
    teacher = find_teacher(low[3], teach_data)
    low.append(teacher[0])
    low.append(teacher[1])
    return [low]

def student_info(stud_data: list): #pt2 done
    results = []
    for i in range(7):
        counter = 0
        for line in stud_data:
            if int(line[2]) == i:
                counter += 1
        results.append((i, counter))
    return results

def print_studs(studs: list):
    for stud in studs:
        print(",".join(stud)) if stud else print("")

def main():
    stud_data = read_file("list.txt")
    teach_data = read_file("teachers.txt")
    
    if not stud_data or not teach_data:
        print("list.txt or teacher.txt has the wrong format")
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
                stud = find_student_class(data[2], stud_data ,teach_data)
                print_studs(stud)
            else:
                if data[3] == "b":
                    stud = find_student_bus(data[2], stud_data)
                    print_studs(stud)
                else:
                    print("Unknown command. Please try again.")

        elif command == "t":
            stud = find_teacher_students(data[2], stud_data, teach_data)
            print_studs(stud)

        elif command == "g":
            if len(data) < 4:
                stud = [(line[0], line[1]) for line in students_at_grade(data[2], stud_data, teach_data)]
                print_studs(stud)
            else:
                if data[3].lower() == "h":
                    stud = find_gpa_high(data[2], stud_data, teach_data)
                    print_studs(stud)
                elif data[3].lower() == "l":
                    stud = find_gpa_low(data[2], stud_data, teach_data)
                    print_studs(stud)

        elif command == "b":
            stud = students_take_bus(data[2], stud_data)
            print_studs(stud)
        elif command == "a":
            print(average_gpa_of_grade(data[2], stud_data))
        elif command == "i":
            info = [f'{line[0]}:{line[1]}' for line in student_info(stud_data)]
            print(", ".join(info))
        elif command == "q":
            print("Quitting...!")
            break
        else:
            print("Unknown command. Please try again.")

    

if __name__ == "__main__":
    main()