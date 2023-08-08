def print_pascals_triangle(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end=" ")
        
        num = 1
        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)
        
        print()

# Input the number of rows from the user
num_rows = int(input("Enter the number of rows for Pascal's triangle: "))
print_pascals_triangle(num_rows)
