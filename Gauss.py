import numpy as np
from scipy.linalg import solve

def gauss(A, b, x, n):

    L = np.tril(A)
    U = A - L
    sol = np.array([2.4063745019920315, -2.7091633466135456, -0.9163346613545813,  1.195219123505976, 2.326693227091633])
    for k in range(n):
        print(f'k: {k}')
        print(f'x: {x}')
        if k > 0:
            old_error = error

        error = max(sol - x)
        print(f'error: {error}')
        if k > 0:
            print(f'ratio: {error/old_error}')

        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
    return x

'''___MAIN___'''

A = np.array([[4,1,1,0,0], [-1,-3,1,1,0], [2,1,5,-1,-1], [-1,-1,-1,4,0], [0,2,-1,1,4]])
b = [6,6,-6,6,6]
x = [0, 0, 0, 0, 0]

n = 9

gauss(A, b, x, n)