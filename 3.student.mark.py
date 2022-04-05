from datetime import datetime
import numpy as np
import math

class Student:
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

numStudents = Student.CountStudents()
studentList = []
for i in range(numStudents):
    id, name, dob = Student.DetailStudents()
    studentList.append((id, name, dob))
    studentList.sort()

print ("\nAll students list:")
for s in studentList:
    print (f"Student ID: {s[0]} -- Student Name: {s[1]} -- Date of birth: {s[2]}")

class Course:
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

numCourses = Course.CountCourses()
courseList = []
for i in range(numCourses):
    id, name = Course.DetailCourses()
    courseList.append((id, name))
    courseList.sort() 
    
smlib = {}
while True:
    studentid = input("Input student's ID: ")
    courseid = input("Input course's ID: ")
    if studentid not in [student[0] for student in studentList]:
        print ("Invalid student's ID")
        continue 
    if courseid not in [course[0] for course in courseList]:
        print ("Invalid course's ID")
        continue
    break

mark = float(input("Input mark: "))
                
if courseid in smlib:
    smlib[courseid].append((studentid, mark))
else:
    smlib[courseid] = [(studentid, mark)]
    
print("\nAll courses list:")
for c in courseList:
    print(f"Course ID: {c[0]} -- Course Name: {c[1]}")

while True:
    cidmark = input("\nWhich course do you want to see all student marks for? ")
    if cidmark in smlib:
        for l in smlib[cidmark]:
            print(f"Student {l[0]} got {l[1]} marks")
    else:
        print("No course like that lmao")
        continue
    break

class GPA:
    def __init__(self, name):
        self.name = name
  
    def GPAcalc(self, name, cre):
        gpalist = []
        for i in range(len(studentList)):
            if name == studentList[i]:
                print(courseList[i])
                gpalist.append(courseList[i])
                grade = np.array([list(g.values()) for g in gpalist])
                cre = np.array(cre)
                gpa = grade.dot(cre) / sum(cre)
                return tuple((name, gpa))