from datetime import datetime

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
    
def CountCourses():
    return int(input("How many courses?: "))
    
def DetailCourses():
    courseid = input("Input course's ID: ")
    coursename = input("Input course's name: ")
    return courseid, coursename
    
numStudents = CountStudents()
studentList = []
for i in range(numStudents):
    id, name, dob = DetailStudents()
    studentList.append((id, name, dob))
    studentList.sort() 

print ("\nAll students list:")
for s in studentList:
    print (f"Student ID: {s[0]} -- Student Name: {s[1]} -- Date of birth: {s[2]}")

numCourses = CountCourses()
courseList = []
for i in range(numCourses):
    id, name = DetailCourses()
    courseList.append ((id, name))
    courseList.sort() 
    
smlib = {}
while True:
    numCmark = int(input("How many student's course marks do you want to enter? "))
    if numCmark < 0 or numCmark > numStudents * numCourses:
        print("Student's course marks is not available, re-enter please!")
        continue
    break 
for i in range(numCmark):
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