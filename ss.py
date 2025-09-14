class Student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
    def __str__(self):
        return f"{self.name}(ID:S{self.student_id})"      
class Course:
    
    def __init__(self,course_name,course_code,max_capacity=10):
        self.course_name=course_name
        self.course_code=course_code
        self.students=[]
        self.max_capacity=max_capacity
    def add_student(self,student):
        for i in self.students:
            if i.student_id==student.student_id:
                return "student already exist"

        if self.is_full() != True:##
            self.students.append(student)
            return "successfully added student"
        else:
            return "course is full"
    def get_student_count(self):
        return len(self.students)
    def is_full(self):
        if self.get_student_count()==self.max_capacity:
            return True
        else:
            return False
    def list_students(self):
        for student in self.students:
            print (student.__str__())
    def __str__(self):
       return (f"{self.course_name} ({self.course_code}) -Enrolled: {self.get_student_count()}/{self.max_capacity} ") 
class School:
    def __init__(self,name):
        self.name=name
        self.students=[]
        self.courses=[]
    def add_student(self,student):
        for i in self.students:
            if i.student_id==student.student_id:
                return "student already exist"
        self.students.append(student)
        return "successfully added student"
    def add_course(self,course):
        for i in self.courses:
            if i.course_code==course.course_code:
                return 'already exist'
        self.courses.append(course)
        return "successfully added course"
    def enroll_student_in_course(self,student_id,course_code):
        studen=self.find_student_by_id(student_id)
        cours=self.find_course_by_code(course_code)
        if studen ==None and cours==None:
            return "student and course does not exist"
        if studen ==None:
            return "student does not exist"
        elif cours==None:
            return "course does not exist"
        else:
            cours.add_student(studen)
            return "student successfully enrolled"
    def show_all_courses(self):
        for course in self.courses:
            print(course)

    def find_student_by_id(self,student_id):
        for student in self.students:
            if student.student_id==student_id:
                return student
    def find_course_by_code(self,course_code):
        for course in self.courses:
            if course.course_code==course_code:
                return course
Bio=Student("Osei Bio Wisdom",2245)
Osei=Student("Father",2545)
Jandra=Student("Jandra",225)
course1=Course("science",400)
course2=Course("Eng",405)
school1=School("Great Koss")
school1.add_student(Bio)
school1.add_student(Osei)
school1.add_student(Jandra)
school1.add_course(course1)
school1.add_course(course2)
print(school1.enroll_student_in_course(225,400))
print(school1.enroll_student_in_course(2245,405))
school1.show_all_courses()
