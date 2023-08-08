word_list = input("Enter a list of words separated by spaces: ").split()

word_occurrences = {}
for word in word_list:
    if word in word_occurrences:
        word_occurrences[word] += 1
    else:
        word_occurrences[word] = 1

print("Word occurrences:")
for word, count in word_occurrences.items():
    print(f"'{word}': {count} times")
