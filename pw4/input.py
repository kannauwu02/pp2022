from datetime import datetime
class input:    
    def __init__(self, studentid, studentname, dobformat):
        self.stid = studentid
        self.stname = studentname
        self.stdob = dobformat
    
    def __str__(self):
        return f"Student ID: {self.stid} -- Student Name: {self.stname} -- Date of birth: {self.stdob}"
    
    def CountStudents():
        return int(input("How many students?: "))
        
    def DetailStudents():
        studentid = input("Input student's ID: ")
        studentname = input("Input student's name: ")
        while True:
            try:
                studentdob = input("Enter student's date of birth dd/mm/yyyy: ")
                dob = datetime.strptime(studentdob, "%d/%m/%Y")
            except ValueError:
                print("Wrong date of birth format!")
                continue
            break
        dobformat = f"{dob.day}/{dob.month}/{dob.year}"
        return studentid, studentname, dobformat
    
    def __init__(self, courseid, coursename):
        self.cid = courseid
        self.cname = coursename
    
    def __str__(self):
        return f"Course ID: {self.cid} -- Course Name: {self.cname}"
    
    def CountCourses():
        return int(input("How many courses?: "))
        
    def DetailCourses():
        courseid = input("Input course's ID: ")
        coursename = input("Input course's name: ")
        return courseid, coursename