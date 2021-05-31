import matplotlib.pyplot as plt
import math
import numpy as np


nk = 1.331
nf = 1.346
dx, dy = 0.01, 0.001
y = [-0.99]

fi1k, fi2k, fi1f, fi2f = [], [], [], []  # углы

while y[-1] <= 0.99:
    if y[-1] > 0:
        fi1k.append(4 * math.asin(y[-1] / nk) - 2 * math.asin(y[-1]))
        fi1f.append(4 * math.asin(y[-1] / nf) - 2 * math.asin(y[-1]))
    if y[-1] < 0:
        fi2k.append(math.pi - 6 * math.asin(abs(y[-1]) / nk) + 2 * math.asin(abs(y[-1])))
        fi2f.append(math.pi - 6 * math.asin(abs(y[-1]) / nf) + 2 * math.asin(abs(y[-1])))
    y.append(y[-1]+dy)

plt.subplot(221)
plt.plot(y[((len(y)//2)+1):], list(map(lambda x: x * 180/math.pi, fi1k)), color='#e50000')
plt.title(r'$\phi_1$', fontsize=14)
plt.text(0.5, 0, 'max = {}°'.format(round(max(list(map(lambda x: x * 180/math.pi, fi1k))), 2)))
plt.subplot(222)
plt.plot(list(map(abs, y[:(len(y)//2)])), list(map(lambda x: x * 180/math.pi, fi2k)), color='#e50000')
plt.title(r'$\phi_2$', fontsize=14)
plt.text(0.5, 172, 'min = {}°'.format(round(min(list(map(lambda x: x * 180/math.pi, fi2k))), 2)))
plt.subplot(223)
plt.plot(list(map(abs, y[(len(y)//2)+1:])), list(map(lambda x: x * 180/math.pi, fi1f)), color='#9a0eea')
plt.text(0.5, 0, 'max = {}°'.format(round(max(list(map(lambda x: x * 180/math.pi, fi1f))), 2)))
plt.subplot(224)
plt.plot(list(map(abs, y[:(len(y)//2)])), list(map(lambda x: x * 180/math.pi, fi2f)), color='#9a0eea')
plt.text(0.5, 172, 'min = {}°'.format(round(min(list(map(lambda x: x * 180/math.pi, fi2f))), 2)))
plt.show()

Ifi1k, Ifi1f, Ifi2k, Ifi2f = [], [], [], []  # интенсивности
y = -0.99
while y <= 0.99:
    if y > 0:
        Ifi1k.append(2 / (4 / math.sqrt(nk ** 2 - y ** 2) - 2 / math.sqrt(1 - y ** 2)))  # Формулу интенсивности взял
        Ifi1f.append(1 / (4 / math.sqrt(nf ** 2 - y ** 2) - 2 / math.sqrt(1 - y ** 2)))  # как частную производную
    if y < 0:
        Ifi2k.append(1 / (2 / math.sqrt(1 - y ** 2) - 6 / math.sqrt(nk ** 2 - y ** 2)))  # от угла фи по y (I = dfi/dy)
        Ifi2f.append(1 / (2 / math.sqrt(1 - y ** 2) - 6 / math.sqrt(nf ** 2 - y ** 2)))
    y += dy

plt.plot(list(map(lambda x: x * 180/math.pi, fi1k)), Ifi1k, color='#e50000')
plt.plot(list(map(lambda x: x * 180/math.pi, fi2k)), Ifi2k, color='#e50000')
plt.plot(list(map(lambda x: x * 180/math.pi, fi1f)), Ifi1f, color='#9a0eea')
plt.plot(list(map(lambda x: x * 180/math.pi, fi2f)), Ifi2f, color='#9a0eea')
plt.xlabel(r'$\phi$', fontsize=16)
plt.ylabel(r'$I$', fontsize=16)
plt.text(43, 11, r'$I_1$', fontsize=15)
plt.text(55, 11, r'$I_2$', fontsize=15)
plt.text(42.6, 0.2, '{}'.format(round(fi1k[Ifi1k.index(max(Ifi1k))]*180/math.pi, 2)))
plt.text(48.3, 0.2, '{}'.format(round(fi2k[Ifi2k.index(max(Ifi2k))]*180/math.pi, 2)))
plt.text(38, 0.2, '{}'.format(round(fi1f[Ifi1f.index(max(Ifi1f))]*180/math.pi, 2)))
plt.text(52.25, 0.4, '{}'.format(round(fi2f[Ifi2f.index(max(Ifi2f))]*180/math.pi, 2)))
plt.title(r'$I(\phi)$', fontsize=17)

plt.ylim(0, 12)
plt.xlim(35, 60)
plt.show()


cols = ['r', 'o', 'y', 'g', 'c', 'b', 'p']
n = {'r': 1.331, 'o': 1.333, 'y': 1.335, 'g': 1.337, 'c': 1.339, 'b': 1.341, 'p': 1.343}
x_dict, y_dict = {}, {}

# Задание окружности
circle_x = np.arange(-1, 1, 0.00001)
circle_y1 = np.sqrt(1 - np.power(circle_x, 2))
circle_y2 = -np.sqrt(1 - np.power(circle_x, 2))

y_lessgo = 0.69  # высота луча

for i in cols:
    x_dict[i], y_dict[i] = [], []
    # стартовые параметры
    x = -1.7
    y = y_lessgo
    k = 0  # угловой коэффициент
    while x**2 + y**2 > 1:  # пока луч не вошел в каплю
        x_dict[i].append(x)
        y_dict[i].append(y)
        x += dx

    alpha1 = np.arcsin(y) - np.arcsin(y / n[i])
    k = np.tan(-alpha1)
    while x**2 + y**2 <= 1:  # луч вошел в каплю. первое преломление
        x_dict[i].append(x)
        y_dict[i].append(y)
        x += dx
        y += k * dx
    x -= dx
    y -= k * dx

    alpha2 = np.pi - 2 * np.arcsin(y / n[i])
    k = np.tan(-alpha1 - alpha2)
    while x**2 + y**2 <= 1:  # отразился от стенки капли
        x_dict[i].append(x)
        y_dict[i].append(y)
        x -= dx
        y -= k * dx
    cx = x + dx
    cy = y + k * dx

    alpha3 = np.arcsin(y) - np.arcsin(y / n[i])
    k = np.tan(-alpha1 - alpha2 + alpha3)
    while x >= -2:  # вышел из капли первый раз
        x_dict[i].append(x)
        y_dict[i].append(y)
        x -= dx
        y -= k * dx
    x = cx
    y = cy

    alpha3 = np.pi - 2 * np.arcsin(y / n[i])
    k = np.tan(-alpha1 - alpha2 + alpha3)
    while x**2 + y**2 <= 1:  # третье преломление
        x_dict[i].append(x)
        y_dict[i].append(y)
        x += dx
        y += k * dx

    alpha4 = np.arcsin(y) - np.arcsin(y / n[i])
    k = np.tan(-alpha1 - alpha2 + alpha3 - alpha4)
    while x <= 2:  # окончательно вышел из капли
        x_dict[i].append(x)
        y_dict[i].append(y)
        x += dx
        y += k * dx
plt.title("y = {}".format(y_lessgo))
plt.plot(circle_x, circle_y1, 'C0',
         circle_x, circle_y2, 'C0',
         x_dict['r'], y_dict['r'], 'red',
         x_dict['o'], y_dict['o'], 'orange',
         x_dict['y'], y_dict['y'], 'yellow',
         x_dict['g'], y_dict['g'], 'green',
         x_dict['c'], y_dict['c'], 'cyan',
         x_dict['b'], y_dict['b'], 'blue',
         x_dict['p'], y_dict['p'], 'purple')
plt.grid()
plt.axis("equal")
plt.xlim(-1.5, 1.5)
plt.ylim(-1.25, 1.25)

plt.show()
