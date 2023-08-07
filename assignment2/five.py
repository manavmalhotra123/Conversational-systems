def can_form_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

# Get input from the user
try:
    a = int(input("Enter the first side length: "))
    b = int(input("Enter the second side length: "))
    c = int(input("Enter the third side length: "))

    # Check if the given lengths can form a triangle
    result = can_form_triangle(a, b, c)

    # Print the result
    print("Yes" if result else "No")

except ValueError:
    print("Invalid input. Please enter valid numeric values for side lengths.")
