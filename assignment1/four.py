def get_student_info():
    sid = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    gender = input("Enter Gender (F/M/U for Unknown): ").upper()
    course_name = input("Enter Course Name: ")
    cgpa = float(input("Enter CGPA: "))
    return [sid, name, gender, course_name, cgpa]

def display_student_info(student_list):
    print("\nStudent Information:")
    print(f"Student ID: {student_list[0]}")
    print(f"Name: {student_list[1]}")
    print(f"Gender: {student_list[2]}")
    print(f"Course Name: {student_list[3]}")
    print(f"CGPA: {student_list[4]}")

def main():
    students = []
    num_students = int(input("Enter the number of students: "))

    for i in range(num_students):
        print(f"\nEnter details for Student {i + 1}:")
        student_info = get_student_info()
        students.append(student_info)

    print("\nStudent details stored successfully.")
    
    for student in students:
        display_student_info(student)

if __name__ == "__main__":
    main()
