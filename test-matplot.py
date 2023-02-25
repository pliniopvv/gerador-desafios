import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(-10, 10, 100)
y = 1800*(1-0.2)**n
b = 1800*(0.2)**n

plt.plot(n, y)
plt.plot(n,b)

plt.xlabel("n")
plt.ylabel("y")
plt.title("Gráfico de y = x^2")
plt.show()
