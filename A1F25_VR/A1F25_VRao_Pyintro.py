print('Hello A1!\n')
print('Made by Vinit Rao Fall 2025\n')
def get_first_name():
    while True: #loop to check if name is valid
        first_name = input("What is your first name? ")
        if len(first_name) < 1:
            print("Please enter a first name.")
            continue
        break
    return first_name

def get_last_name():
    last_name = input("What is your last name? ")
    if len(last_name) < 1: #if condition to input N/A if no last name is provided
        last_name = '(no last name given)'
    return last_name

def get_average():
    total_grades = 0 #used for calculating the average grade

    #checking how many grades will be used in the calculation
    while True:
        try:
            grade_count = int(input("How many grades do you have? "))
            if grade_count <= 0: #making sure int is a positive value
                print("Please enter a positive number.")
                continue
            break #exit while loop when condition is met
        except ValueError: #making sure int is an int :p
            print("Please enter a number.")

    #looping based off how many grades were requested
    for i in range(int(grade_count)):
        while True:
            try:
                current_grade = int(input("Please enter your grade: "))
                if current_grade < 0:  #making sure int is a positive value
                    print("Please enter a positive number.")
                    continue
                if current_grade > 100:
                    print("Please enter a number in range from 0 to 100.")
                    continue
                break #exit while loop when condition is met
            except ValueError: #making sure int is an int :p
                print("Please enter a number.")
        total_grades += current_grade #adding the current grade to the total every cycle
    return(total_grades // grade_count) #average grade calculated and returned as an int (no decimal value)

def is_pass_msg(grade):
    while True:
        try:
            if grade < 0 or grade > 100: #check to make sure grade falls in range of 0-100
                print("Please enter valid a number.")
                continue
            elif grade < 50: #check if below 50 to output a failed result
                print("You failed ITEC 2401. Sorry")
                return grade
            elif grade > 50: #check if above 50 to output a passed result
                print("You passed the course with an " + str(grade) + "%. Nice work")
                return grade
        except ValueError: #check to make sure is valid numeric value
            print("Please enter a valid number.")

def print_range(min,max):
    for i in range(min,max): #prints in the range from min to max
        print(i)

# get_first_name() and get_last_name Task:
print("get_first_name() & get_last_name() Task:\n")
first_name = get_first_name()
last_name = get_last_name()
print (first_name + " has " + str(len(first_name)) + " letters in their first name.")
print("Your full name is " + first_name +" "+ last_name + ".\n")

# get_average() & is_pass_msg() Task:
print("get_average() & is_pass_msg() Task:\n")
average_grade = get_average()
print("Average Grade: " + str(average_grade) + "%")
is_pass_msg(average_grade)

# print_range() Task:
print("\nprint_range() Task:\n")
min_num = int(input("Please enter your minimum grade: "))
max_num = int(input("Please enter your maximum grade: "))
print_range(min_num,max_num)
