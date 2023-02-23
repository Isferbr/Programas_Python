# Questão 1
import matplotlib.pyplot as plt

x = [0, 2, 4, 6, 8]
y = 2 * x
z = x ** 2

plt.plot(x, y, 'go-', label = 'Linha 1')
plt.plot(x, z, 'bs-', label = 'Linha 2')
plt.legend(loc=1)
plt.grid(True)
