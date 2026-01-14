# Defining Student class
# Each student has a roll number, name, age, and a list of enrolled courses
# Methods: enroll_course(course), display_courses()

class Student :

    def __init__(self , roll_number , name , age ) :
        self.roll_number = roll_number 
        self.name = name 
        self.age = age 
        self.course_list = []

    # function to enroll in a course

    def enroll_course(self , course) :
        self.course_list.append(course)
        print(f"student {self.name} enrolled in course {course.course_name}")

    # function to drop a course

    def drop_course(self , course_id) :
        for course in self.course_list :
            if course.course_id == course_id :
                self.course_list.remove(course)
                print(f"Dropped course {course.course_name} for student {self.name}")   
                return
        print(f"Course with ID {course_id} not found for student {self.name}")

    # function to display all enrolled courses

    def display_courses(self) :
        print(f"Courses enrolled by {self.name} : ")    

        if not self.course_list :
            print("No courses enrolled.")
            return
        else :
            for course in self.course_list :
                print(f"Course ID : {course.course_id} , Course Name : {course.course_name} , Credits : {course.credits}")

    # function to calculate total credits
    def total_credits(self) :
        total = 0 
        for course in self.course_list :
            total += course.credits
        print(f"Total credits for student {self.name} : {total}")               

# Defining Course class
# Each course has an ID, name, and number of credits
# Methods: None

class Course :
    def __init__(self , course_id , course_name , credits ) :
        self.course_id = course_id
        self.course_name = course_name 
        self.credits = credits 
       

# Creating courses
python = Course(101 ,"Python", 4)
ml = Course(102 ,"Machine Learning", 3)
data_science = Course(103 ,"Data Science", 3)
java = Course(104 ,"Java", 4)
data_analysis = Course(105 ,"Data Analysis", 2)

# Creating student
student1 = Student(1 ,"Isha Rajput" , 21)
student2 = Student(2 ,"Aarav Singh" , 22)
student3 = Student(3 ,"Maya Patel" , 20)

# Enrolling courses
student1.enroll_course(python)
student1.enroll_course(ml)

student2.enroll_course(python)
student2.enroll_course(data_science)

student3.enroll_course(java)

# Showing courses
student1.display_courses()    

# Dropping a course
student3.drop_course(104)

# Showing courses after dropping
student3.display_courses()

# Calculating total credits
student1.total_credits()
student2.total_credits()
student3.total_credits()
