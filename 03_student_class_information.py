class Student:
    school_name = "Global English School"

    def __init__(self, name, grade, roll_no, marks):
        self.name = name
        self.grade = grade
        self.roll_no = roll_no
        self.marks = marks

    def display_info(self):
        print(f"{self.name}\nClass {self.grade}\nRoll no. {self.roll_no}\nGot {self.marks}% in Unit Test Exam of {self.school_name}\n")


students = [
    Student("1. Karan singhania", 10, 1, 96),
    Student("2. Mohammed Farhan", 10, 2, 97),
    Student("3. Yashraj Bhivsane", 10, 3, 95),
    Student("4. Shaikh Abu Anzar", 10, 4, 93),
    Student("5. Mohammed Abdullah", 3, 11, 92),
    Student("6. Abdul Rahman", 2, 5, 92)
]


for student in students:
    student.display_info()
