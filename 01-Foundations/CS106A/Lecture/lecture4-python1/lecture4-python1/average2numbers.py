"""
File: average2numbers.py
------------------------
This program prompts the user for two numbers,
and displays the average of those two numbers.
"""

def main():
    print("Average2Numbers")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 + num2
    average = result/2
    print(average)

if __name__ == "__main__":
    main()