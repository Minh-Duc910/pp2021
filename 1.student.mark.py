

def no_of_student():
   no = int(input("No of student: "))
   return no

def st_info():
    id = input("Student ID: ")
    name = input("Student's name: ")
    dob = input("Date of birth (dd/mm/yy): ")
    info = {"ID ":id ,"Name ":name ,"DoB ":dob}
    return info

st = []
number = no_of_student()
for i in range(number):
    info = st_info()
    st += [info]
print(st)

def no_of_courses():
    noc = int(input("Number of course: "))
    return noc

def c_info():
    c_id = int(input("Course ID: "))
    c = input("Course: ")
    info_of_c = {"Course ID":c_id ,"Course":c}
    return info_of_c
