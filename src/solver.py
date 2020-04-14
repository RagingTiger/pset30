'''
Author: github.com/RagingTiger
Description: Algorithm for finding the solution to pset30
'''

# libs
import sys
import time
import importlib
from fractions import Fraction

# classes
class Solver:
    def __init__(self, funcfile, start=(1,1)):
        # get functions
        functions = importlib.import_module(funcfile)

        try:
            self.f = functions.F
            self.g = functions.G
        except:
            sys.exit('Problem with importing func file: {}'.format(functions))

        # setup misc
        self.outstr = 'Diff: {} / n,m = {},{} / x1,x2 = {},{}'

    def pfrac(self, decimal):
        # need to convert decimal to string
        dstr = str(decimal)

        # get ratio fraction
        ratio = str(Fraction(dstr))

        # now print out proper ratio fraction
        return ratio

    def increment(x):
        return (1/(1 + x))

    def difference(self, inputs):
        a, b = inputs
        A, B = self.f(a), self.g(b)
        diff = A - B
        print(self.outstr.format(diff, a, b, self.pfrac(A), self.pfrac(B)))

    def run(self):

        # setup loop
        a, b = self.start


if __name__ == '__main__':
    # get fire for CLI
    import fire

    # blast off
    fire.Fire(Solver)
