def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    
    for char in alphabet:
        if char not in s:
            return False
    
    return True

# Example usage
input_string = "The quick brown fox jumps over the lazy dog"
if is_pangram(input_string):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")
