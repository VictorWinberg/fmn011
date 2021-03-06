# -*- coding: utf-8 -

import numpy as np

x = np.logspace(-1, -14, num=14)
print('X: ' + ', '.join(map(str, x)) + '\n')

a = (1 - 1/np.cos(x)) / np.tan(x)**2
print('A_1: ' +', '.join(map(str, a)))

a = np.cos(x)*(np.cos(x) - 1) / np.sin(x)**2
print('A_2: ' +', '.join(map(str, a)))

a = 1/np.tan(x)**2 - 1/(np.tan(x)*np.sin(x))
print('A_3: ' +', '.join(map(str, a)))
print("1e-1, 1e-7  -> 8 sign. digits; 1e-8, 1e-14 -> 0 sign. digits\n")

b = (1 - (1-x)**3) / x
print('B_1: ' +', '.join(map(str, b)))
print("1e-1          -> 3 sign. digits")
print("1e-2, 1e-7  -> 4-8 sign. digits")
print("1e-8, 1e-14 -> 9 sign. digits\n")

b = x**2 - 3*x + 3
print('B_2: ' +', '.join(map(str, b)))
