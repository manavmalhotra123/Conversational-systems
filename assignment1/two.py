def compute_income_tax(gross_income, num_dependents):
    # Tax laws
    tax_rate = 0.20
    standard_deduction = 10000
    dependent_deduction = 3000

    # Calculate taxable income
    taxable_income = gross_income - standard_deduction - (num_dependents * dependent_deduction)

    # Calculate tax
    tax = taxable_income * tax_rate

    return tax

# Get input from the user
try:
    gross_income = float(input("Enter your gross income to the nearest penny: "))
    num_dependents = int(input("Enter the number of dependents: "))

    # Compute and display income tax
    income_tax = compute_income_tax(gross_income, num_dependents)
    print(f"Your income tax is: ${income_tax:.2f}")

except ValueError:
    print("Invalid input. Please enter valid numeric values.")
