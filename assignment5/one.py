def reverse_string(input_string):
    reversed_string = ""

    # Loop through the characters of the input string in reverse order
    for char in input_string[::-1]:
        reversed_string += char

    return reversed_string

def main():
    input_string = input("Enter a string: ")
    reversed_string = reverse_string(input_string)
    print("Reversed string:", reversed_string)

if __name__ == "__main__":
    main()
