def pallindrome(input,start,end):
    if start >= end:
        return True
    if input[start] != input[end]:
        return False
    return pallindrome(input,start+1,end-1)

# Input a string from the user
string = input("Enter a string: ")
string = string.lower()  # Convert to lowercase for case-insensitive comparison

if pallindrome(string, 0, len(string) - 1):
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")