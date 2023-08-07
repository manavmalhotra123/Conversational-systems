input_string = "Python is a case sensitive language"

length_of_string = len(input_string)
print("Length of the input string:", length_of_string)

reversed_string = input_string[::-1]
print("Reversed string:", reversed_string)

new_string = input_string[10:26]
print("New string:", new_string)

replaced_string = input_string.replace("a case sensitive", "object oriented")
print("Replaced string:", replaced_string)

index_of_a = input_string.find("a")
print("Index of 'a':", index_of_a)

trimmed_string = input_string.replace(" ", "")
print("Trimmed string:", trimmed_string)
