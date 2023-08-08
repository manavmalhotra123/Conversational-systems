def is_perfect_number(number):
    if number <= 1:
        return False
    
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    return divisors_sum == number

# Input a number from the user
num = int(input("Enter a number: "))

if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
