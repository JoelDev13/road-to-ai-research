
### What I Did Today

In this lesson, I learned about Karel the Robot

#### Who is Karel?
Karel is a project designed to make learning the fundamentals of programming easier. It was inspired by the work of Karel Čapek (who introduced the word "robot" in his 1923 play, R.U.R.)

During the session, I explored how the game works and learned the basic commands

#### Why python?
We also discussed why Python is the language of choice for this course. Key reasons include:

- easy to read: It has a clean, readable syntax

- Great for data analysis: It is a standard tool in the data science field

- Great for AI: It is the primary language used for artificial intelligence development

- Community support: It has a massive ecosystem of packages and a helpful global community

#### Programming Concepts

##### Composition
Composition is the idea that if you don't have a specific tool (command), you can build one yourself using the ones you already have

##### Example: 
Karel only knows how to turn_left(). If you need to turn right, you can create a turn_right() function by calling turn_left() three times

##### Functions
Using repetitive code (like calling turn_left() three times every time you need to turn right) makes your program confusing and difficult to read. To fix this, we use functions

To define a command (function) in Python, you use the def keyword, followed by the name you want to give the function, and parentheses

##### Python
```
Example of defining a function

def turn_right():
    turn_left()
    turn_left()
    turn_left()
```

- Resource: Chapters 1, 2, and 3 https://compedu.stanford.edu/karel-reader/docs/python/en/intro.html


