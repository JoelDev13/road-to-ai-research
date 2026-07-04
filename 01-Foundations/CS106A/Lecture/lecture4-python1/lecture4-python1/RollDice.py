"""
File: RollDice.py
------------------
Simulate rolling two dice
"""
import random
NUM_SIDES = 6

def main():
    dice1 = random.randint(1, NUM_SIDES)
    dice2 = random.randint(1, NUM_SIDES)

    print(f"First dice: {dice1} and second dice: {dice2}")

if __name__ == "__main__":
    main()