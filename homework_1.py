# Create the Student class, so each student instance can store important information
class Student:
    def __init__(self, student_name, gender, email):
        self.student_name = student_name
        self.gender = gender
        self.email = email
# Add a course with the Course class to the student
    def add_course(self, course):
        self.course = course
        course.add_student(self)
# Automatically add the student to the course variable

# Create the Course class, so each course instance can store information
class Course:
    def __init__(self, course_name, trainer, topics, room):
        self.course_name = course_name
        self.trainer = trainer
        self.topics = topics
        self.room = room
        self.students = []

# Add students with the Student class to the course
    def add_student(self, student):
        self.students.append(student)


course1 = Course("Data", "Isabella Jones", ["Business Skills", "Advanced Excel", "Agile", "SQL",
                                      "Tableau", "python"], "Flexibility")

reagan = Student("Reagan Prince", "Male", "RPrince@spartaglobal.com")
reagan.add_course(course1)

mariam = Student("Mariam Aslam", "Female", "MAslam@spartaglobal.com")
mariam.add_course(course1)

alun = Student("Alun Wrighton", "Male", "AWrighton@spartaglobal.com")
alun.add_course(course1)

iman = Student("Iman Ali", "Female", "IAli@spartaglobal.com")
iman.add_course(course1)

laura = Student("Laura Geanta", "Female", "LGeanta@spartaglobal.com")
laura.add_course(course1)

eimantas = Student("Eimantas Alejunas", "Male", "EAlejunas@spartaglobal.com")
eimantas.add_course(course1)

print(reagan.course[0].course_name)
print(mariam.course[0].trainer)
print(alun.gender)
print(course1.students[3].email)