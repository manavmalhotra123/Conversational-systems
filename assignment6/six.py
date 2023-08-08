class Student:
    pass

class Marks:
    pass

# Creating instances
student_instance = Student()
marks_instance = Marks()

# Checking instances' classes
if isinstance(student_instance, Student):
    print("student_instance is an instance of Student class")
else:
    print("student_instance is not an instance of Student class")

if isinstance(marks_instance, Marks):
    print("marks_instance is an instance of Marks class")
else:
    print("marks_instance is not an instance of Marks class")

# Checking class inheritance
if issubclass(Student, object):
    print("Student class is a subclass of the built-in object class")
else:
    print("Student class is not a subclass of the built-in object class")

if issubclass(Marks, object):
    print("Marks class is a subclass of the built-in object class")
else:
    print("Marks class is not a subclass of the built-in object class")
