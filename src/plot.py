# Import our modules that we are using
import math
import matplotlib.pyplot as plt
import numpy as np

# funcs
def sqradd(x, n):
    return x**2 + 2*x*n + n**2

def sqrsub(x, m):
    return x**2 - 2*x*m + m**2

n = 0.5
m = 0
x = np.array(range(-10, 10))

# x1 = (2 - (n**2))/(2*n)
# x2 = ((m**2) + 2)/((2*m) + 1)
# sqrx1 = (x1)**2
# sqrx2 = (x2)**2
# intersect = sqrx1 - sqrx2
# eq1 = x**2 + 2
# eq2 = x**2 - 2 + x
# ysqr = x**2 + 2*x + 1
y1 = x**2
y2 = x**2 + 2
y3 = x**2 - 2 + x
y4 = x**2 - (2 + x)
y5 = sqradd(x, n)
y6 = sqrsub(x, m)
dy1 = 2*x
dy2 = dy1
dy3 = 2*x + 1
dy4 = 2*x - 1
tst1 = x**2 + 13 + x
tst2 = x**2 - (2 + x)

y7 = sqradd(x, 0)
y8 = sqradd(x, 1)
y9 = sqradd(x, 2)

y10 = sqrsub(x, -1)
y11 = sqrsub(x, 0)
y12 = sqrsub(x, 1)

# Create the plot
# plt.plot(n,x1, label="(2 - ({})^2)/2({})".format(n,n), linestyle='--', marker='+')
# plt.plot(m,x2, label="(({})^2 + 2)/(2({}) + 1)".format(m,m), linestyle='--', marker='+')
# plt.plot(n,sqrx1, label="((2 - ({})^2)/2({}))^2".format(n,n), linestyle='--', marker='+')
# plt.plot(m,sqrx2, label="((({})^2 + 2)/(2({}) + 1))^2".format(m,m), linestyle='--', marker='+')
# plt.plot(n,intersect, label="intersect")
# plt.plot(x, eq1, label="x^2 + 2")
# plt.plot(x, eq2, label="x^2 - 2 + x")
# plt.plot(x, ysqr, label="x^2 + 2x + 1")
# plt.plot(x, y1, label="A: x^2", linestyle='--', marker='o')
# plt.plot(x, y2, label="B: x^2 + 2", linestyle='--', marker='v')
# plt.plot(x, y3, label="C: x^2 - 2 + x", linestyle='--', marker='v')
# plt.plot(x, y4, label="D: x^2 - (2 + x)", linestyle='--', marker='v')
plt.plot(x, tst1, label="G: x^2 + 13 + x", linestyle='--', marker='v')
plt.plot(x, tst2, label="H: x^2 - (2 + x)", linestyle='--', marker='v')
plt.plot(x, y5, label="E: x^2 + 2x({}) + ({})^2".format(n,n), linestyle='--', marker='o')
plt.plot(x, y6, label="E: x^2 - 2x({}) + ({})^2".format(m,m), linestyle='--', marker='o')

# plt.plot(x, y7, label="E: x^2 + 2x({}) + ({})^2".format(0,0), linestyle='--', marker='o')
# plt.plot(x, dy1, label="dA: 2x", linestyle='--', marker='x')
# plt.plot(x, dy2, label="dB: 2x", linestyle='--', marker='x')
# plt.plot(x, dy3, label="dB: 2x + 1", linestyle='--', marker='x')
# plt.plot(x, dy4, label="dB: 2x - 1", linestyle='--', marker='x')

# plt.plot(x, y7, label="E: x^2 + 2x({}) + ({})^2".format(0,0), linestyle='--', marker='o')
# plt.plot(x, y8, label="E: x^2 + 2x({}) + ({})^2".format(1,1), linestyle='--', marker='o')
# plt.plot(x, y9, label="E: x^2 + 2x({}) + ({})^2".format(2,2), linestyle='--', marker='o')

# plt.plot(x, y10, label="E: x^2 + 2x({}) + ({})^2".format(-1,-1), linestyle='--', marker='o')
# plt.plot(x, y11, label="E: x^2 + 2x({}) + ({})^2".format(0,0), linestyle='--', marker='o')
# plt.plot(x, y12, label="E: x^2 + 2x({}) + ({})^2".format(1,1), linestyle='--', marker='o')



# Create labels
# plt.ylabel('x or y^2')
# plt.xlabel('n or x')

# Create legend
plt.legend()

# Show the plot
plt.show()
