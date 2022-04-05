class output:
    print ("\nAll students list:")
    for s in studentList:
        print (f"Student ID: {s[0]} -- Student Name: {s[1]} -- Date of birth: {s[2]}")
    print("\nAll courses list:")
    for c in courseList:
        print(f"Course ID: {c[0]} -- Course Name: {c[1]}")