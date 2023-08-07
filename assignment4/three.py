import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2, num1 * num2

def main():
    print("Welcome to the Multiplication Game!")
    score = 0

    for i in range(1, 11):
        num1, num2, correct_answer = generate_question()
        user_answer = int(input(f"Question {i}: {num1} x {num2} = "))

        if user_answer == correct_answer:
            print("Right!")
            score += 1
        else:
            print(f"Wrong. The answer is {correct_answer}.")

    print(f"\nYou got {score} out of 10 questions correct.")

if __name__ == "__main__":
    main()
