def gradeing(number):
    if number < 25:
        return 'F'
    if number >= 25 and number < 45:
        return 'E'
    if number >= 45 and number < 50:
        return 'D'
    if number >= 50 and number < 60:
        return 'C'
    if number >= 60 and number < 80:
        return 'B'
    else:
        return 'A'

try:
    number = int(input("Enter the marks: "))

    grade = gradeing(number)
    print(grade)

except ValueError:
    print("Invalid input. Please enter valid numeric marks.")
