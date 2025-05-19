import math
x= input('Enter the number: ')
x=float(x)

def countSquares(x):
    sqrt = x**0.5
    result = int(sqrt)
    return result

print('square root:', countSquares(x))

print ('Logarithm:', math.log(x))

print('Sine:', math.sin(x))