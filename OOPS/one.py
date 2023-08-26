class Employee:
    # constructor of the class
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    # calculate te employees salary by taking worked time 
    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.emp_salary / 50)
            return self.emp_salary + overtime_amount
        return self.emp_salary

    # assign a new department to the employee
    def emp_assign_department(self, new_department):
        self.emp_department = new_department

    # print employee details
    def print_employee_details(self):
        
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")


# Sample Employee Data
adams = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
jones = Employee("JONES", "E7499", 45000, "RESEARCH")
martin = Employee("MARTIN", "E7900", 50000, "SALES")
smith = Employee("SMITH", "E7698", 55000, "OPERATIONS")

# Assign a new department to Adams
adams.emp_assign_department("HR")
# Print Adams' details
adams.print_employee_details()
# Calculate and print the salary of Smith based on 60 hours worked
print(f"Smith's Salary after working 60 hours: {smith.calculate_emp_salary(60)}")
