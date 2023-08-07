def decimal_to_binary(number):
    return bin(number)


try:
    num = int(input("Enter the number "))

    binary = decimal_to_binary(num)
    print("Binary number is " + binary)

except ValueError:
    print("Invalid number")