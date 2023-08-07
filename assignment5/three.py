def is_valid_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

def main():
    try:
        a = float(input("Enter the length of side 'a': "))
        b = float(input("Enter the length of side 'b': "))
        c = float(input("Enter the length of side 'c': "))

        if is_valid_triangle(a, b, c):
            area = calculate_area(a, b, c)
            print(f"The area of the triangle is: {area:.2f}")
        else:
            print("The given combination of sides does not form a valid triangle.")

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    main()
