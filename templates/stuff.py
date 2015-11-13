# import requests
# a = requests.get('http://url-riddle-edinburgh.herokuapp.com/riddles/plaintive/primes/challenge')
# val = int(a._content)
# val += 1
#
#
# def is_prime(n):
#     if n == 2:
#         return 1
#     if n % 2 == 0:
#         return 0
#     max = n**0.5+1
#     i = 3
#     while i <= max:
#         if n % i == 0:
#             return 0
#         i+=2
#     return 1
#
# while(not is_prime(val)):
#     val +=1
#
# r = requests.get('http://url-riddle-edinburgh.herokuapp.com/riddles/plaintive/primes/'+str(val))
# print(r._content)

import math
(x,y) = (23, 15)

def translate(x,y,a,b):
    return (round(x+a),round(y+b))

def scale (x,y,a,b,c):
    x_prime = a+(x-a)*c
    y_prime = b+(y-b)*c
    return (round(x_prime),round(y_prime))

def mirror(z):
    if z == 'x':
        return (round(x,-1 * y)
    elif z == 'y':
        return (x*-1, y)

def rotate(x,y,a,b,c):
    rotatedX = math.cos(c) * (x - a) - math.sin(c) * (y-b) + a
    rotatedY = math.sin(c) * (x - a) + math.cos(c) * (y - b) + b;
    return (rotatedX,rotatedY)

(x,y) = translate(x,y, 2, -6)
(x,y) = scale(x, y, 1, 3, 0.5)
(x,y) = rotate(x, y, 3, 2, 1.57079632679)
(x,y) = mirror('x')
(x,y) = translate(x, y ,3, -2)
(x,y) = scale(x,y,-8, 0, 4.5)
(x,y) = rotate(x,y,1, -3, 3.14159265359)
(x,y) = mirror('y')

print(x,y)