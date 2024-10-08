import numpy as np

m = [[1,35], [8,94]]
x = np.zeros(2)

for i in range (0,2):
    for j in range (0,2):
        if i == j:
            x[i] = m[i][j]

print(x)