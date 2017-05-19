import math
import unittest
import cProfile
import re
import sys
import pstats

class KnownValues(unittest.TestCase):
    known_values = ( (10, 11, 0),
            (10, 10, 1),
            (2, 1, 2),
            (5, 2, 10),
            (4, 2, 6))

    def test_binomialCoefficient_known_values(self):
        '''bionamialCoefficient should give known result with known input'''
        for x, y, bn in self.known_values :
            result = binomialCoefficient(x, y)
            self.assertEqual(bn, result)

def binomialCoefficient(x, y):
    x = int(x)
    y = int(y)
    if y == x or y==0:
        return 1
    elif y == 1:
        return x
    elif y > x:
        return 0
    else:
        a = math.factorial(x)
        b = math.factorial(y)
        c = math.factorial(x-y)
        div = a // (b * c)
        return div

def pascal(x):
    x = int(x)
    i = 0
    l = []
    while i<=x:
        l.append(binomialCoefficient(x,i))
        i+=1
    return l

def countingBinomialCoefficient(num, prime):
    i = 0
    l = []
    num = int(num)
    prime = int(prime)
    while i<= num:
        l.extend(pascal(i))
        i+=1
    return len([f for f in l if int(f)%prime!= 0])

if __name__ == '__main__':
    #unittest.main()
    #print(pascal(sys.argv[1]))
    print(countingBinomialCoefficient(sys.argv[1], sys.argv[2]))
