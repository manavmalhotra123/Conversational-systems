def print_numbers_divisible_by(range_start, range_end, divisor):
    divisible_numbers = []

    for num in range(range_start, range_end + 1):
        if num % divisor == 0:
            divisible_numbers.append(num)

    return divisible_numbers

def main():
    try:
        range_start = int(input("Enter the start of the range: "))
        range_end = int(input("Enter the end of the range: "))
        divisor = int(input("Enter the number to check for divisibility: "))

        if divisor == 0:
            print("Cannot divide by zero.")
        else:
            divisible_numbers = print_numbers_divisible_by(range_start, range_end, divisor)

            if divisible_numbers:
                print(f"Numbers in the range divisible by {divisor}: {divisible_numbers}")
            else:
                print(f"No numbers in the range are divisible by {divisor}.")

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    main()
