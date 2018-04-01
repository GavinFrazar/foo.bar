"""
| 7
| 4 8
| 2 5 9
| 1 3 6 10

Recognize that:
id(x,1) = sum from 1 to x
id(1,y) = (sum from 1 to y-1) + x
id(2,y) = (sum from 1 to y) + x
id(3,y) = (sum from 1 to y+1) + x
etc

So:
id(x,y) = (sum from 1 to x) + (sum from x to x+y-2)
        = (sum from 1 to x) + (sum from 1 to x+y-2) - (sum from 1 to x-1)
        = (sum from 1 to x+y-2) + x
"""

def sum(n):
    return int(n*((n+1)/2))
def answer(x, y):
    return str(sum(x+y-2) + x)