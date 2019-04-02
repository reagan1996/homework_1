# Create the Course class, so each course instance can store information
class Course:
    def __init__(self, course_name, trainer_first_name, trainer_last_name, topics, room):
        self.course_name = course_name
        self.trainer_first_name = trainer_first_name
        self.trainer_last_name = trainer_last_name
        self.topics = topics
        self.room = room
        self.students = []

# Create a method to output the trainer's full name
    def trainer_name(self):
        return self.trainer_first_name + " " + self.trainer_last_name

# Add students with the Student class to the course
    def add_student(self, student):
        self.students.append(student)

# Create a method to list the students on a course
    def list_students(self):
        list_of_students = []
        for student in self.students:
            list_of_students.append(student.student_name())
        return list_of_students


# Create the Student class, so each student instance can store important information
class Student:
    def __init__(self, student_first_name, student_last_name, gender, email):
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name
        self.gender = gender
        self.email = email

# Create a method to return the student's full name
    def student_name(self):
        return self.student_first_name + " " + self.student_last_name


# Add a course with the Course class to the student
    def add_course(self, course):
        self.course = course
        course.add_student(self)
# Automatically add the student to the course variable




course1 = Course("Data", "Isabella", "Jones", ["Business Skills", "Advanced Excel", "Agile", "SQL",
                                      "Tableau", "python"], "Flexibility")

reagan = Student("Reagan", "Prince", "Male", "RPrince@spartaglobal.com")
reagan.add_course(course1)

mariam = Student("Mariam", "Aslam", "Female", "MAslam@spartaglobal.com")
mariam.add_course(course1)

alun = Student("Alun", "Wrighton", "Male", "AWrighton@spartaglobal.com")
alun.add_course(course1)

iman = Student("Iman", "Ali", "Female", "IAli@spartaglobal.com")
iman.add_course(course1)

laura = Student("Laura", "Geanta", "Female", "LGeanta@spartaglobal.com")
laura.add_course(course1)

eimantas = Student("Eimantas", "Alejunas", "Male", "EAlejunas@spartaglobal.com")
eimantas.add_course(course1)

print(reagan.course.course_name)
print(mariam.course.trainer_name())
print(alun.gender)
print(course1.students[3].email)
print(course1.list_students())