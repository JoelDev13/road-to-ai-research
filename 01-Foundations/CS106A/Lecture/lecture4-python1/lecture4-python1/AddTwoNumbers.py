"""
File: AddTwoNumbers.py
----------------------
This program prompts the user for two numbers,
adds them together, and shows the user the
result.
"""

def main():
    print("This program adds two numbers together!")
    num1 = input("Enter first number: ")
    num1 = int(num1)
    num2 = input("Enter second number: ")
    num2 = int(num2)
    result = num1 + num2
    print(f"The total is {result}")

if __name__ == "__main__":
    main()
