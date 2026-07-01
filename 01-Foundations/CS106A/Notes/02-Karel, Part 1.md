#### Structure of a .py file

Each .py file is organized like this, from top to bottom:

- Imports — code from others that you use
- Helper functions — your own helper functions
- Main function — def main():, where your program begins
- Magic start function — if __name__ == "__main__": run_karel_program()

Important rule: Functions must be defined before they are used **(analogy: "prep your vegetables before cooking")**

#### for loops

To repeat something a fixed and known number of times.

```
for i in range(N):
    # code to repeat
```

**Class example:** Rewrite turn_right() with for i in range(3): turn_left() instead of repeating the line 3 times.

#### while loops

To repeat something while a condition is true, without knowing in advance how many times (useful when the program must work in "any world", of any size).

```
while condition:
    # code to repeat
```

**Example:** move_to_wall() with while front_is_clear(): move().

#### The "Off-By-One Bug" (OBOB) / Fencepost Problem

Star example from class: place_beepers_in_line():

```
while front_is_clear():
    put_beeper()
    move()
```

**Problem:** This leaves the last square without a beeper, because the while checks the condition before executing the body. When it reaches the wall, it no longer enters

**Solution:** Add an extra put_beeper() after the while

#### for or while

SituationUseYou know how many repetitions (defined)forYou don't know how many repetitions (undefined)while

#### if / if-else statements

To execute code only if a condition is met.

```
if condition:
    # if true
else:
    # if false
```