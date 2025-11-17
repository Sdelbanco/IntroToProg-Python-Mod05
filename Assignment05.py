# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Serena del Banco,11/12/25, Created Script
# ------------------------------------------------------------------------------------------ #

# Import json and _io
import json # import code from Python's JSON module
from json import JSONDecodeError
import _io # import _io.TextIOWrapper

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data (TODO: Change this to a Dictionary)
students: list = []  # a table of student data
file = _io.TextIOWrapper  # Holds a reference to an opened file. (TODO: Change this to use _io.TextIOWrapper instead of None)
menu_choice: str  # Hold the choice made by the user.

# try command for error handling
try:
# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
    file = open(FILE_NAME, "r")
    students=json.load(file)
    file.close()
except FileNotFoundError as e:
    print(f"File {FILE_NAME} not found")
    print(e,e.__doc__, type(e), sep='\n')
    print("Creating file since it doesn't exist")
    file=open(FILE_NAME, 'w')
except JSONDecodeError as e:
    print(e, e.__doc__, type(e), sep='\n')
    print("Data in file not valid. Resetting it.")
    file = open(FILE_NAME, 'w')
    json.dump(students, file)
except Exception as e:
    print("Unhandled exception")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if not file.closed:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError('First name must be alphabetic')
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError('Last name must be alphabetic')
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name, "LastName": student_last_name,"CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            continue
        except ValueError as e:
            print(e, e.__doc__, type(e), sep='\n')

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student['CourseName']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            for student in students:
                print(f"Registration info for {student["FirstName"]} {student["LastName"]} has been saved to {FILE_NAME}")
            continue
        except TypeError as e:
            print("Check that data is in valid JSON format")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("Unhandled exception")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if not file.closed:
                file.close()

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
