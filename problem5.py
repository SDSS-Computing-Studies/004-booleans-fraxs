#! python3

"""
In math, if a quadratic equation is in the format
ax^2 + bx + c = 0, the discriminant can be calculated as
b^2 - 4 * a * c
If the discriminant is a perfect square, the equation can
be factored.  Furthermore, if the discriminant is negative,
then the equation has no solutions (not used in this assignment).
Have the user enter in values for a, b and c and then 
tell them if the equation can be factored.

Inputs:
- 3 numbers (a, b, c)

Outputs:
- "the equation can be factored"
- "the equation can not be factored"

Example:
Enter a: 1
Enter b: 4
Enter c: 4
the equation can be factored

Enter a: 1
Enter b: 4
Enter c: 8
the equation can not be factored

"""
import math
num1 = float( input("Enter first number: "))
num2 = float( input("Enter second number: "))
num3 = float( input("Enter third number: "))
num1 = math.sqrt(num1)
num2 = math.sqrt(num2)
num3 = math.sqrt(num3)
if num1 == int(num1) and num2 == int(num2) and num3 == int(num3):
    print("This equation can be factored.")
else:
    print("This equation cannot be factored.")
    
