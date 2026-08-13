# Q. Attendance System


from tabulate import tabulate
import os


class Student:
    def __init__(self, student_name, student_roll):
        self.student_name = student_name
        try:
            self.student_roll = int(student_roll)
        except ValueError:
            print("Input roll as int.")
            return
        
    def __repr__(self):
        return f"Name: {self.student_name}\nRoll: {self.student_roll}"


class CourseRecords:
    def __init__(self, course_name, course_records_file=None):
        if course_records_file == None:
            try:
                course_records_file = open(f"course_{course_name}.json", "x")
                course_records_file.close()
            except FileExistsError:
                print("File already exists!")

        self.base_path = os.path.dirname(os.path.abspath(__file__))
        course_records_file = os.path.join(self.base_path, course_records_file)

        #here I want to enroll all students with attended_sessions as 0



class AttendanceManager: 
    def __init__(self):
        self.courses_list = []
        self.students_list = []
    
    def add_student(self, name, roll):
        student = Student(name, roll)  
        self.students_list.append(student)
        
    def mark_attendance(self, roll):
        pass

    def find_student_attendance(self, roll):
        pass

    def add_course(self, course_name, total_sessions=0):
        new_course = CourseRecords()

    def show_groups_table(self):
        print("Students Categorized:")
        categorized_table = [()]
        print(tabulate(categorized_table, headers=["Group 1", "Group 2", "Group 3", "Group 4"], tablefmt="grid"))


#Main
manager = AttendanceManager()
def main():
    while True:    

        while True:     #if error occurs during input of task_number

            task_number = input("Enter option number for the task you want to perform:\n1. Mark Attendance\n2. Show catogorized table of students\n3. Find Attendance of a student\n4. Add New Student to course\n5. Add a New Course\n6. Exit System.")
            
            if task_number == '6' or task_number == 'q':
                return
            try:
                if int(task_number) > 0:
                    break
            except ValueError:
                print("Invalid Input. Enter valid option number from the following:\n")
        

        if task_number == "1":
            roll = input("Enter Roll Number: ")
            try:
                if int(roll) > 0:
                    manager.mark_attendance(roll)
            except ValueError:
                print("Invalid Input.\n")

        if task_number == "2":
            manager.show_groups_table()

        if task_number == "3":
            manager.find_student_attendance(roll)

        if task_number == "4":
            name = input("New Student name: ")
            roll = input("New Student Roll Number: ")
            try:
                if int(roll) > 0:
                    manager.add_student(name, roll)
            except ValueError:
                print("Invalid Input.\n")

        if task_number == "5":
            course_name = input("Enter New Course Name: ")
            course_code = input("Enter New Course Code: ")
            sessions = input("Enter total number of sessions (0 if not decided): ")
            try:
                if int(sessions) >= 0:
                    manager.add_course(course_name, course_code, sessions)
            except ValueError:
                print("Invalid Input.\n")



        # break   ##Remove this

    # manager.student.student_name




if __name__ == "__main__":
    main()

    