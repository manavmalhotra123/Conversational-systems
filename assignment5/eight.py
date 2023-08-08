# Initialize lists to store positive, negative, odd, and even numbers
positive_numbers = []
negative_numbers = []
odd_numbers = []
even_numbers = []
number_occurrences = {}

# Input 10 integer values from the user
for i in range(10):
    num = int(input(f"Enter integer {i + 1}: "))
    
    # Categorize the number
    if num > 0:
        positive_numbers.append(num)
    elif num < 0:
        negative_numbers.append(num)
    
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
    
    # Count the occurrences of the number
    if num in number_occurrences:
        number_occurrences[num] += 1
    else:
        number_occurrences[num] = 1

# Print the categorized numbers
print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

# Print the occurrences of each number
print("Number occurrences:")
for num, count in number_occurrences.items():
    print(f"{num}: {count} times")
