def check_word_presence(user_string):
    return "Yes" if "name" in user_string.lower() else "No"

# Get input from the user
user_input = input("Enter a string: ")

# Check if "name" is present in the input string
result = check_word_presence(user_input)

# Print the result
print(result)
