# Paul Nassar & Andy Duong
#list.txt:          StLastName, StFirstName, Grade, Classroom, Bus, GPA
#teachers.txt:      LastName, TFirstName, Classroom

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

#R4
def find_student_class(lastname: str, stud_data: list, teach_data : list): #part2 done
    students = []
    for line in stud_data:
        if line[0] == lastname.upper():
            teacher = find_teacher(line[3], teach_data)
            class_data = (line[0], line[1], line[2], line[3], teacher[0], teacher[1])
            students.append(class_data)
    return students

#R5
def find_student_bus(lastname: str, stud_data: list): #part2 done
    busses = []
    for line in stud_data:
        if line[0] == lastname.upper():
            busses.append((line[0], line[1], line[4]))
    return busses

#R6
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

#R7
def students_at_grade(grade: str, stud_data: list, teach_data): #part2 done
    students = []
    for line in stud_data:
        if line[2] == grade:
            teacher = find_teacher(line[3], teach_data)
            gpa = line[5].strip()
            students.append([line[0], line[1], line[2], line[3], line[4], gpa, teacher[0], teacher[1]])
    return students

#R8
def students_take_bus(bus_route: str, stud_data : list): #part 2 done
    students = []
    for line in stud_data:
        if line[4] == bus_route:
            students.append((line[0], line[1], line[2], line[3]))
    return students

#R9 (a)
def find_gpa_high(grade: str, stud_data: list, teach_data : list):#part 2 done
    students = students_at_grade(grade, stud_data, teach_data)
    if not students:
        return []
    
    high = students[0]
    for line in students:
        if line[2] == grade:
            if line[5] > high[5]:
                high = line
    
    return [high]

#R9 (b)
def find_gpa_low(grade: str, stud_data: list, teach_data : list): #part 2 done
    students = students_at_grade(grade, stud_data, teach_data)
    if not students:
        return []
    
    low = students[0]
    for line in students:
        if line[2] == grade:
            if line[5] < low[5]:
                low = line
    return [low]

#R10
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

#R11
def student_info(stud_data: list): #pt2 done
    results = []
    for i in range(7):
        counter = 0
        for line in stud_data:
            if int(line[2]) == i:
                counter += 1
        results.append((i, counter))
    return results

#NR1
def students_in_class(class_num: str, stud_data: list, teach_data: list):
    students = []
    for line in stud_data:
        if line[2] == class_num:
            teacher = find_teacher(line[3], teach_data)
            students.append([line[0], line[1], line[2], line[3], line[4], line[5], teacher[0], teacher[1]])
    return students

#NR2
def teachers_in_class(class_num: str, teach_data: list):
    teachers = []
    for line in teach_data:
        if line[2] == class_num:
            teachers.append(line)
    return teachers

#NR3
def teachers_in_grade(grade_num: str, stud_data: list, teach_data: list):
    classrooms = []
    teachers = []
    for line in stud_data:
        if line[2] == grade_num and line[3] not in classrooms:
            classrooms.append(line[3])
    for line in teach_data:
        if line[2] in classrooms:
            teachers.append(line)
    return teachers

#Dictionary Sorting Helper
def sort_dict(myDict: dict):
    keys = list(myDict.keys())
    keys.sort()
    return {i: myDict[i] for i in keys}


#NR4
def enrollments_report(stud_data: list):
    classes = {}
    for line in stud_data:
        if line[3] not in classes.keys():
            classes[line[3]] = 1
        else:
            classes[line[3]] += 1
    sorted_classes = sort_dict(classes)
    print("Enrollment Report: ")
    for key in sorted_classes:
        print(f"Class {key}:  {sorted_classes[key]} Student{"s" if sorted_classes[key] > 1 else ""}")

#NR5 (a)
def grade_analytics(stud_data: list):
    grades = {}
    for line in stud_data:
        if line[2] not in grades.keys():
            grades[line[2]] = average_gpa_of_grade(line[2], stud_data)
    sorted_grades = sort_dict(grades)
    for key in sorted_grades:
        print(f"Grade {key}:  {sorted_grades[key]} GPA")

#NR5 (b)
def teacher_analytics(stud_data: list, teach_data: list):
    teachers = {}
    teachers_counts = {}
    classes_to_teachers = {}
    for line in teach_data:
        if float(line[2]) not in classes_to_teachers.keys():
            classes_to_teachers[float(line[2])] = [f"{line[0], line[1]}"]
        else:
            classes_to_teachers[float(line[2])].append(f"{line[0], line[1]}")
        teachers[f"{line[0], line[1]}"] = 0
        teachers_counts[f"{line[0], line[1]}"] = 0
    for line in stud_data:
        for teacher in classes_to_teachers[float(line[3])]:
            teachers[teacher] += float(line[5])
            teachers_counts[teacher] += 1
    for teacher in teachers:
        teachers[teacher] = round(teachers[teacher] / teachers_counts[teacher], 2)
    sorted_teachers = sort_dict(teachers)
    for key in sorted_teachers:
        print(f"Teacher {key}:  {sorted_teachers[key]} GPA")

#NR5 (c)
def bus_analytics(stud_data: list):
    busses = {}
    busses_counts = {}
    for line in stud_data:
        if line[4] not in busses.keys():
            busses[line[4]] = float(line[5])
            busses_counts[line[4]] = 1
        else:
            busses[line[4]] += float(line[5])
            busses_counts[line[4]] += 1
    for bus in busses:
        busses[bus] = round(busses[bus] / busses_counts[bus], 2)
    sorted_busses = sort_dict(busses)
    for key in sorted_busses:
        print(f"Bus {key}:  {sorted_busses[key]} GPA")

#NR5
def getAnalytics(stud_data: list, teach_data: list, selection: str):
    if selection == "g":
        grade_analytics(stud_data)
    elif selection == "t":
        teacher_analytics(stud_data, teach_data)
    elif selection == "b":
        bus_analytics(stud_data)
    else:
        print("Invalid Analytics Selection")

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