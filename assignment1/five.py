def main():
    num_students = 5
    marks = []

    # Input marks for each student
    for i in range(num_students):
        while True:
            try:
                mark = float(input(f"Enter marks for Student {i + 1}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")

        marks.append(mark)

    # Sort the marks in ascending order
    marks.sort()

    # Display the sorted marks
    print("\nSorted Marks:")
    for i, mark in enumerate(marks):
        print(f"Student {i + 1}: {mark}")

if __name__ == "__main__":
    main()
