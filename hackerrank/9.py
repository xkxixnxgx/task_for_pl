import numpy as np

a = list(map(float, input().split()))
x = int(input())

print(np.polyval(a, x))
