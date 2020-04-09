# libs
from fractions import Fraction

# funcs
def pfrac(decimal):
    # need to convert decimal to string
    dstr = str(decimal)

    # get ratio fraction
    ratio = str(Fraction(dstr))

    # now print out proper ratio fraction
    print(ratio)

if __name__ == '__main__':
    # get fire for CLI
    import fire

    # blast off
    fire.Fire(pfrac)
