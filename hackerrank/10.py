import numpy as np

if __name__ == '__main__':
    n = int(input())
    rank = []
    for x in range(n):
        y = input().split()
        rank.append(list(map(float, y)))
    a = np.linalg.det(rank)
    if round(a, 2) == a:
        print('%.1f' % np.linalg.det(rank))
    else:
        print('%.2f' % np.linalg.det(rank))
