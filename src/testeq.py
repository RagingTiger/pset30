'''
Author: github.com/RagingTiger
Description: Here are defined some test equations and their subsequent functions
             for testing the solver.py utility for pset30

Equation 1: x^2 + 13 + x

Equation 2: x^2 - (2 + x)

Equation 3: x^2 + 2xn + n^2

Equation 4: x^2 - 2xm + m^2
'''

# funcs
def eq1(x):
    return x**2 + 13 + x

def eq2(x):
    return x**2 - (2 + x)

def eq3(x, n):
    return x**2 + 2*x*n + n**2

def eq4(x, m):
    return x**2 + 2*x*m + m**2

def F(n):
    """
    Deriving F(n) from equation 1 and 2:
        x^2 + 13 + x = x^2 + 2xn + n^2
        x^2 - x^2 + 13 + x = x^2 - x^2 + 2xn + n^2
        13 + x = 2xn + n^2
        13 + x - 2xn = -2xn + 2xn + n^2
        13 + x(1 - 2n) = n^2
        13 - 13 + x(1 - 2n) = n^2 - 13
        x(1 - 2n) = n^2 - 13
        x(1 - 2n)/(1 - 2n) = (n^2 - 13)/(1 - 2n)
        x = (n^2 - 13)/(1 - 2n)
    """

    return (n**2 - 13)/(1 - 2*n)

def G(m):
    """
    Deriving G(m) from equation 3 and 4:
        x^2 - (2 + x) = x^2 - 2xm + m^2
        x^2 - x^2 - (2 + x) = x^2 - x^2 - 2xm + m^2
        -(2 + x) = -2xm + m^2
        -2 - x = -2xm + m^2
        -2 - x + 2xm = -2xm + 2xm + m^2
        -2 + x(2m - 1) = m^2
        -2 + 2 + x(2m - 1) = m^2 + 2
        x(2m - 1) = m^2 + 2
        x(2m - 1)/(2m - 1) = (m^2 + 2)/(2m - 1)
        x = (m^2 + 2)/(2m - 1)
    """
    return (m**2 + 2)/(2*m - 1)
