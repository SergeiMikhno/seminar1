from myclass import Person
from myclass import Student

Student1 = Student()
Student2 = Student()

Student1.set_student('Sergei',29,1)

Student2.set_student('Andrei',30,2)

Student1.description_of_person()
Student2.description_of_person()

print(Student2.get_student_name())
Student2.change_student_name('Pavel')
print(Student2.get_student_name())
print(Student2.get_student_course())
print(Student2.get_student_age())


