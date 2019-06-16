print("-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-MARKSHEET-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-")
student_name = str(input ("STUDENT NAME: "))
father_name = str(input ("FATHER NAME: "))
rollno = str(input ("ROLL NO: "))
department = str(input ("DEPARTMENT: "))
semester = str(input ("SEMESTER: "))
english = int(input ("ENGLISH: "))
discret_math = int(input ("DISCREET MATH: "))
data_structure= int(input ("DATA STRUCTURE: "))
intro_SE = int(input ("INTRODUCTION TO S.E: "))
digital_logical_disgn = int(input ("DIGITAL LOGICAL DISGN: "))
print("-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-")
print("STUDENT NAME: ",student_name)
print("FATHER NAME: ",father_name)
print("ROLL NO: ",rollno)
print("DEPARTMENT: ",department)
print("SEMESTER: ",semester)
print ("SUBJECT                      TOTAL MARKS                         OBTAINED MARKS")
print("-----------------------------------------------------------------------------------")
print("ENGLISH                           100                                ",english)
print("DISCREET MATH                     100                                ",discret_math)
print("DATA STRUCTURE                    100                                ",data_structure)
print("INTRODUCTION TO S.E               100                                ",intro_SE)
print("DIGITAL LOGICAL DISGN             100                                ",digital_logical_disgn)
total_obtain_marks = english + discret_math + data_structure + intro_SE + digital_logical_disgn
percentage = (total_obtain_marks*100)/500 
print("TOTAL OBTAINED MARKS",total_obtain_marks)
print("PERCENTAGE",percentage)
if 90 <= percentage <=100:
    print("GRADE: A1+")
elif 80 <= percentage <90:
    print("GRADE: A1")
elif 70 <= percentage <80:
    print("GRADE: A")
elif 60 <= percentage <70:
    print("GRADE: B")
elif 50 <= percentage <60:
    print(" GRADE: C")
else:
    print("SORRY,YOU ARE FAIL")    