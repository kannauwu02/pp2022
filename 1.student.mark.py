from datetime import datetime

def getStudentCount ():
    return int (input ("Enter student's number: "))
    
def getStudentDetails ():
    studentid = input ("Enter student id: ")
    studentname = input ("Enter student name: ")
    while True:
        try:
            sdob = input ("Enter student's date of birth dd/mm/yyyy: ")
            dob = datetime.strptime(sdob, "%d/%m/%Y")
        except ValueError:
            print("Wrong date of birth format!")
            continue
        break
    dobs = str(dob.day) + "/" + str(dob.month) + "/" + str(dob.year)
    return studentid, studentname, dobs
    
def getCourseCount ():
    return int (input ("Enter number of courses: "))
    
def getCourseDetails ():
    courseid = input ("Enter course id: ")
    coursename = input ("Enter course name: ")
    return courseid, coursename
    
numStudents = getStudentCount ()
studentList = []
for i in range (numStudents):
    id, name, dob = getStudentDetails ()
    studentList.append ((id, name, dob))
    studentList.sort() 

print ("\nListing all students now..")
for s in studentList:
    print (f"Student id: {s[0]} -- Name: {s[1]} -- Date of birth: {s[2]}")

numCourses = getCourseCount ()
courseList = []
for i in range (numCourses):
    cid, cname = getCourseDetails ()
    courseList.append ((cid, cname))
    courseList.sort() 
    
lib = {}
while True:
    n = int (input ("Enter how many student-course marks do you want to enter? "))
    if n < 0 or n > numStudents * numCourses:
        print("student-course marks is not available, re-enter please")
        continue
    break 
for i in range (n):
    while True:
        sid = input ("Enter student id: ")
        cid = input ("Enter course id: ")
        if sid not in [student [0] for student in studentList]:
            print ("Invalid student id")
            continue 
        if cid not in [course [0] for course in courseList]:
            print ("Invalid course id")
            continue 
        break

    marks = float (input ("Enter marks: "))
            
    if cid in lib:
        lib [cid].append ((sid, marks))
    else:
        lib [cid] = [(sid, marks)]

print ("\nListing all courses now..")
for c in courseList:
    print (f"Course id: {c[0]} Name: {c[1]}")

while True:
    cid = input ("\nWhich course do you want to see all student marks for? ")
    if cid in lib:
        for l in lib [cid]:
            print (f"Student {l[0]} got {l[1]} marks")
    else:
        print("No course like that lmao")
        continue
    break