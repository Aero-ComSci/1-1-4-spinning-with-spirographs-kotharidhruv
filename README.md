[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SkD24yV8)
# 1.1.4Spirographs

*Complete the following.*

1. Compare and contrast zero-iteration conditions and infinite loops.
2. A link to your code where you solve the following problem. Take the screen size of 800px. Create code or algorithm that always places the object(s), up to 5, in the center an equal distance from one another and from the edges of the screen.
3. Concentric Squares -- Add a screenshot of your result and the code to create it on your repo.
Objective: Write a Python program using the turtle module to draw a pattern of concentric squares. The pattern should be created using nested loops.

Instructions:

Setup the Turtle Environment:
Import the turtle module.
Create a turtle object.
Set the turtle speed to the fastest setting.
Draw Concentric Squares:
Use a nested loop to draw multiple squares.
The outer loop should control the number of squares.
The inner loop should draw each square.
Each square should be slightly larger than the previous one.
Customize the Pattern:
Use different colors for each square.
Ensure the squares are centered on the screen.
Example Output:

The turtle should draw a series of squares, each one larger than the last, creating a pattern of concentric squares.

Hints:

Use the penup() and pendown() methods to move the turtle without drawing.
Use the color() method to change the turtle’s color.
Use the forward() and right() methods to draw the sides of the squares.


4. Complete the steps 17, 18 and 19 from [mypltw use clever to sign on](https://pltw.read.inkling.com/a/b/5310c007377c46e28d745961310f0c2e/p/728c751a6c4145bea0ea83c5058fb9f9#44b0003a2ee14fcc9865e7bb5faec747)
5. Answer to step 21
6. Insert a screenshot or picture of the algorith you used for your tokenizer on the previous activity.
7. Give an example of an undecidable problem, attach code.

## Zero Iteration and Infinite Loops
### Zero Iteration Loops
Zero iteration loops are loops that are never iterated over; hence the name 'Zero Iteration'

For example,
```python
name = "Dhruv"

while name=="Mr. Baez":
   print("Hi, Mr. Baez")
```
In the code above, the name has been set to "Dhruv". The while loop is set to be iterated over when the name is "Mr. Baez". Since the ```while name=="Mr. Baez``` statement returns false, the while loop is never going to be iterated over.

### Infinite Loops
Infinite Loops are loops that get iterated over infinitely many times, until the program is manually terminated.

For example,
```python
name = "Mr. Baez"

while name=="Mr. Baez":
   print("Hi, Mr. Baez")
```
In the code above, the name has been set to "Mr. Baez". As said before, the while loops is set to iterate when the name is "Mr. Baez". Since the while statement is returning ```True```, the statement in the while loop is being executed. Since we are not changing the value of ```name```, the print statement is being executed infinitely many times. That is why this type of loop is called the infinite loop.

## Screen Size Problem
[Link to solution to the problem](https://github.com/Aero-ComSci/1-1-4-spinning-with-spirographs-kotharidhruv/blob/e31ff41addaa5857ae774943b40f421d007f70e5/screensize.py)

## Concentric Squares


