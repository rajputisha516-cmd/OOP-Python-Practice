# Student Management System (OOP – Python)

## 📌 Problem Statement
A college needs a simple system to manage students and the courses they enroll in.
Each student can enroll in multiple courses, drop courses, view enrolled courses, and calculate total credits.

This project is built to practice **Object-Oriented Programming (OOP)** concepts in Python using a real-life scenario.

---

## 🧠 OOP Concepts Used
- Classes and Objects  
- Composition (Student *HAS* Courses)  
- Encapsulation  
- Object Interaction  
- Real-world business rules  

---

## 🧩 Entities

### Student
**Attributes**
- roll_number
- name
- age
- course_list (list of enrolled Course objects)

**Methods**
- enroll_course(course)
- drop_course(course_id)
- display_courses()
- total_credits()

---

### Course
**Attributes**
- course_id
- course_name
- credits

---

## ⚙️ Features Implemented
- Create students and courses
- Enroll a student in multiple courses
- Drop an enrolled course using course ID
- Display all enrolled courses of a student
- Calculate total credits dynamically
- Handles empty course list cases

---

## ▶️ How to Run the Project

```bash
# Clone the repository
git clone https://github.com/your-username/oop-python-practice.git

# Navigate to the project folder
cd oop-python-practice/student-management-system

# Run the program
python student_management.py

🔮 Future Scope

This project can be extended in the following ways:

-Prevent duplicate course enrollment
-Add multiple students and manage them using a list or dictionary
-Add a menu-driven interface for better user interaction
-Store student and course data using a database (SQLite)
-Add grading system and GPA calculation
-Convert the project into a small REST API or web application

Note : This project uses a small dataset and is designed purely for learning and practicing core OOP concepts in Python.

👩‍💻 Author

Isha Rajput
Python & OOP Practice Project