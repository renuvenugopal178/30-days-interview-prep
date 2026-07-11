# Day 7 - Student Management System


class Student:

    def __init__(self, roll_no, name, department, cgpa):
        self.roll_no = roll_no
        self.name = name
        self.department = department
        self.cgpa = cgpa

    # Display student details
    def display(self):
        print("\n------ Student Details ------")
        print("Roll Number :", self.roll_no)
        print("Name        :", self.name)
        print("Department  :", self.department)
        print("CGPA        :", self.cgpa)

    # Update CGPA
    def update_cgpa(self, new_cgpa):
        self.cgpa = new_cgpa
        print(f"\nCGPA updated successfully to {self.cgpa}")

    # Placement Eligibility
    def check_placement(self):
        print("\nPlacement Status")

        if self.cgpa >= 7:
            print("Eligible for Placements")
        else:
            print("Not Eligible for Placements")


# -------------------------
# Creating Student Objects
# -------------------------

student1 = Student(
    101,
    "Renu",
    "Computer Science and Design",
    7.87
)

student2 = Student(
    102,
    "Anu",
    "Computer Science",
    6.45
)

# Display Details
student1.display()
student2.display()

# Placement Check
student1.check_placement()
student2.check_placement()

# Update CGPA
student2.update_cgpa(7.52)

# Check Again
student2.display()
student2.check_placement()