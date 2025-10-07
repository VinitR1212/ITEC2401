# Assignment 2 Starter: ITEC 2401
# Mehdi Niknam (1234567)
#----------------------------------
# Returns a LIST of classmates with no duplicates
# that attend ANY classes with student stu
# The dictionary of class names / student rosters is also an input parameter
def get_classmates(stu, class_dict):
    classmates = []
    stu_courses = stu[3] #this grabs the course list which will be the keys for the dictionary
    for i in stu_courses: #using i as the keys for the dictionary and cycling through all the courses/keys the student is attending
        if i not in class_dict:
            continue
        for j in class_dict[i]: #using j to cycle between every student in the course
            if j not in classmates: #check to make sure the student is not already appended in classmates to prevent duplicate classmates
                classmates.append(j)
    if stu in classmates: #check to make sure the selected students name is not in the classmates list and if so remove them
        classmates.remove(stu)
    return classmates

# Create and return a dictionary consisting of students numbers (keys) paired with
# student information (values). Function takes a LIST of students stu_list as an input
# parameter


def get_student_numbers(s_list):
    id_list = []
    for i in range(len(s_list)):
        id_list.append(s_list[i][2])
    return id_list


# Returns the list of students that have not taken the class (class_name)
# The set of all students, the dictionary of class rosters for all classes, and the class name
# are all inputs.
def get_missing_students(s_list, class_name, class_dict):
    roster = class_dict.get(class_name, []) #bulletproofed by returning an empty list if there is no class name
    return [s for s in s_list if s not in roster] #returns the list of all students missing from the class

# Function print_student_list prints the contents of a list of students in a easier to
# read format.  The function does not return anything but you can have it return a string
def print_student_list(s_list):
    if not s_list:
        print("No students found\n")
        return None

    for i in range(len(s_list)):
        currstudent = list(s_list[i]) #turning the tuple of each student into list
        print("Name: " + currstudent[0] +" "+ currstudent[1])
        print("ID: " + str(currstudent[2]))
        print("Courses: " + ", ".join(currstudent[3])+"\n")
    print("------------------------------------")
    return None


# GIVEN DATA SET TO USE
# Tuple (), Lists [], dict/Sets {}
student1 = ("Mehdi", "Niknam", 123456, ["BIT1400", "BIT2400", "ITEC2100", "ITEC3204"])
student2 = ("Rose", "Niknam", 123321, ["BIT1401", "BIT2401", "ITEC2000"])
student3 = ("Ali", "Niknam", 654321, ["BIT1400", "BIT2401", "ITEC2100", "ITEC3204"])
student4 = ("Emily", "Angel", 111111, ["ITEC1401", "BIT2400", "ITEC2000"])
student5 = ("Joe", "Niknam", 1459385, ["BIT1401", "BIT2401", "ITEC2100", "ITEC2000"])
student6 = ("Jacky", "Niknam", 7260769, ["ITEC1401", "BIT2401", "ITEC2100", "ITEC2000"])
student7 = ("Jennifer", "Niknam", 8675309, ["PHYS1400"])


# Used to test function get_student_numbers.  The elements of the set should be the same as the list that
# function returns
set_student_ids = {123456, 123321, 654321, 111111, 1459385, 7260769, 8675309}

student_list = [student1, student2, student3, student4, student5, student6, student7]


class_ros_1400 = [student1, student3]
class_ros_1401 = [student2, student4, student5, student6]
class_ros_2401 = [student2, student3, student5, student6]
class_ros_2100 = [student1, student3, student5, student6]
class_ros_2400 = [student1, student4]
class_ros_3204 = [student1, student3]
class_ros_2000 = [student2, student4, student5, student6]
class_ros_phys = [student7]

# Intentionally broken with some students having BIT1401 instead of ITEC1401.  Do not fix.  Handle the potential error.
university_classes = {"BIT1400": class_ros_1400, "ITEC1401": class_ros_1401,
                      "BIT2400": class_ros_2400, "BIT2401": class_ros_2401,
                      "ITEC2100": class_ros_2100, "ITEC2000": class_ros_2000,
                      "ITEC3204": class_ros_3204, "PHYS1400": class_ros_phys }

miss_class = "ITEC2100"
missing_students = get_missing_students(student_list, miss_class, university_classes)
print("The students missing " + miss_class + " are\n" )
print_student_list(missing_students)

# Print the classmates
classmates = get_classmates(student1, university_classes)
print("The classmates of " + student1[0] + " " + student1[1] + " are\n" )
print_student_list(classmates)

classmates = get_classmates(student7, university_classes)
print("The classmates of " + student7[0] + " " + student7[1] + " are\n" )
print_student_list(classmates)

#Print all the student numbers
student_numbers = get_student_numbers(student_list)
print("Student numbers: [")
for num in student_numbers:
    print(str(num) + " ")
print("]\n")


# Finally confirming the student numbers found are legitimate numbers (in set_student_ids)
# TODO: test each id in student_numbers is also in set_student_ids
for id in student_numbers:
    assert(id in set_student_ids)
