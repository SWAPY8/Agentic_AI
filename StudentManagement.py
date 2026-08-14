# 1. Create a Student Management System using Class and Object in Python. What to Do 
# 1. Create a class named Student.  
# 2. Create a constructor __init__() to initialize:  o Student name  o Roll number  o Age  o Marks of 3 subjects  
# 3. Create a display_details() method to display all student information.  
# 4. Create a calculate_total() method to calculate the total marks.  
# 5. Create a calculate_percentage() method to calculate the percentage.  
# 6. Create a check_result() method:  o Student passes if marks in every subject are 35 or above.  o Otherwise, display FAIL.  
# 7. Create an update_marks() method to update the marks of a selected subject. 


class Student:
    
    all_students = {}
    def __init__ (self, Student_Name, Roll_Number, Age, Marks):
        self.Student_Name = Student_Name
        self.Roll_Number = Roll_Number
        self.Age = Age
        self.Marks = Marks
        
    def Action_Bar(self):
        print(f"""        Enter 1 to ADD new Student.
        Enter 2 to Display Students Details.
        Enter 3 to Chech Result.
        Enter 4 to Update student.
        Enter 5 to Exit""")
        
    
    def Add_Student(self):
        name = input("Enter ur name.: ")
        roll_no = int(input("Enter ur roll_no.: "))
        age = int(input(("Enter ur ah age.: ")))
        marks = []
        for i in range(3):
            mark = int(input(f" Enter ur sub{i+1} marks: "))
            marks.append(mark)
        stud_details = Student(name, roll_no, age, marks)
        Student.all_students[roll_no] = stud_details 
        print("Student Added successfully")
        return stud_details
            
        
    
    def display_details(self):
        if not Student.all_students:
            print("No Students Available.")
            return
        
        for roll_no, student in Student.all_students.items():
            print(f"Name = {student.Student_Name}, Roll_No = {student.Roll_Number}, Age = {student.Age}, Marks = {student.Marks}")
    
    
    def calculate_total(self):
        total = sum(self.Marks)
        print("Total = ", total)
        return total    
    
    def percentage(self):
        total = sum(self.Marks)
        percent = total / 3
        print(f"percentage = {percent}%")
        return percent
    
    def check_result(self):
        roll_no = int(input("Enter roll no to check result.: "))
        if roll_no not in Student.all_students:
            print("Student not found.")
            return
        stud1 = Student.all_students[roll_no]
        
        if all(mark >= 35 for mark in stud1.Marks) :
            print("Your result is : Pass")
            self.calculate_total()
            self.percentage()
        else:
            print("Fail")
    
    def update_info(self):
        
        marks = []
        # return stud_details
        
        roll_no = int(input("Change ur roll_no.: "))
        if roll_no not in Student.all_students:
            print("student not available.")
            
        curr_student = Student.all_students[roll_no]
        name = input("Change ur name.: ")
        age = input(("Change ur ah age.: "))
        for i in range(3):
            mark = int(input(f"Enter ur sub{i+1} marks: "))
            marks.append(mark)
        curr_student.Student_Name = name
        curr_student.Age = age
        curr_student.Marks = marks
        
        print("student has updated successfully!")
        
        
    def menu(self):
        print()
        while True:
            
            self.Action_Bar()
            Action = int(input("Enter your Choice : "))
    
            match Action:
                case 1:
                    self.Add_Student()
                
                case 2:
                    self.display_details()
                    
                case 3: 
                    self.check_result()
                    print("""
                                                  
                    """)
                case 4:
                    self.update_info()
                    print("""
                                                  
                    """)
                case 5:
                    print("Exit")
                    break
        

        

obj1 = Student("Swapnil", 101, 67, [78,67,89])
Student.all_students[obj1.Roll_Number] = obj1
obj1.menu()




