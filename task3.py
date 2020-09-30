#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""

import math
a=input(("Enter a number")).trip()
a=float(a)
b=(a/2)
c=math.floor(b)
while b!=c:
    a=str(a)
    print("That is not an even integer")
    break
while b==c:
    a=str(a)
    print("That is an even integer")
    break 
