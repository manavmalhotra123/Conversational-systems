def print_alphabet_pattern(rows):
    current_alphabet = ord('A')  # ASCII value of 'A'

    for i in range(1, rows + 1):
        for j in range(i):
            print(chr(current_alphabet), end="")
            current_alphabet = (current_alphabet - ord('A') + 1) % 26 + ord('A')
        print()

# Input the number of rows from the user
num_rows = int(input("Enter the number of rows: "))
print_alphabet_pattern(num_rows)
