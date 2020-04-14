'''
Author: github.com/RagingTiger
Description: Here are defined the equations central to solving pset30

Equation 1: x^2 + 2

Equation 2: x^2 - 2 + x

Equation 3: x^2 + 2xn + n^2

Equation 4: x^2 - 2xm + m^2
'''

# libs
from math import sqrt
from time import sleep

# funcs
def eq1(x):
    return x**2 + 2

def eq2(x):
    return x**2 - (2 + x)

def eq3(x, n):
    return x**2 + 2*x*n + n**2

def eq4(x, m):
    return x**2 + 2*x*m + m**2

def F(n):
    """
    Deriving F(n) from equation 1 and 2:
        x^2 + 2 = x^2 + 2xn + n^2
        x^2 - x^2 + 2 = x^2 - x^2 + 2xn + n^2
        2 = 2xn + n^2
        2 = n(2x + n)
        2/n = n(2x + n)/n
        2/n = 2x + n
        2/n - n = 2x + n - n
        2/n - n = 2x
        2/n - n(n/n) = 2x
        2/n - n^2/n = 2x
        (2 - n^2)/n = 2x
        ((2 - n^2)/n)/2 = 2x/2
        (2 - n^2)/2n = x
    """
    return (2 - n**2)/(2*n)

def G(m):
    """
    Deriving G(m) from equation 3 and 4:
        x^2 - 2 + x = x^2 - 2xm + m^2
        x^2 - x^2 - 2 + x) = x^2 - x^2 - 2xm + m^2
        -2 + x = -2xm + m^2
        -2 + x = -2xm + m^2
        -2 + x - 2xm = -2xm + m^2 + 2xm
        -2 + x(1 - 2m) = m^2
        -2 + 2 + x(1 - 2m) = m^2 + 2
        x(1 - 2m) = m^2 + 2
        x(1 - 2m)/(1 - 2m) = (m^2 + 2)/(1 - 2m)
        x = (m^2 + 2)/(1 - 2m)
    """
    return (m**2 + 2)/(1 - 2*m)

def trials(num, den):
    t1 = num**2 + (2.0*(den**2))
    str1 = 'x^2 + 2:({}/{}) --> ({})^2 = {}'.format(num, den, sqrt(abs(t1)), t1)

    t2 = num**2 - (2.0*(den**2)) + (num*den)
    str2 = 'x^2 - 2 + x:({}/{}) --> ({})^2 = {}'.format(num, den, sqrt(abs(t2)), t2)

    print('{} | {}'.format(str1, str2))


if __name__ == '__main__':

    import fire

    fire.Fire(trials)
