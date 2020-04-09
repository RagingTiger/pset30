# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np

n = 2
m = 1
x = np.array(range(-20, 20))

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
y4 = x**2 - 2 - x
y5 = x**2 + 2*x*n + n**2
y6 = x**2 - 2*x*m + m**2

# Create the plot
# plt.plot(n,x1, label="(2 - n^2)/2n")
# plt.plot(m,x2, label="(m^2 + 2)/(2n + 1)")
# plt.plot(n,sqrx1, label="((2 - n^2)/2n)^2")
# plt.plot(m,sqrx2, label="((m^2 + 2)/(2n + 1))^2")
# plt.plot(n,intersect, label="intersect")
# plt.plot(x, eq1, label="x^2 + 2")
# plt.plot(x, eq2, label="x^2 - 2 + x")
# plt.plot(x, ysqr, label="x^2 + 2x + 1")
# plt.plot(x, y1, label="A: x^2", linestyle='--', marker='o')
plt.plot(x, y2, label="B: x^2 + 2", linestyle='--', marker='v')
# plt.plot(x, y3, label="C: x^2 - 2 + x", linestyle='--', marker='v')
# plt.plot(x, y4, label="D: x^2 - 2 - x", linestyle='--', marker='v')
plt.plot(x, y5, label="E: x^2 + 2xn + n^2", linestyle='--', marker='o')
# plt.plot(x, y6, label="F: x^2 - 2xn + n^2", linestyle='--', marker='o')

# Create labels
# plt.ylabel('x or y^2')
# plt.xlabel('n or x')

# Create legend
plt.legend()

# Show the plot
plt.show()
