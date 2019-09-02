import numpy as np
def is_winner(a):
    l = np.array (['X', 'X', 'X'])
    for i in range (0, 2):
        if np.all(a[i] == l) or np.all((a[:, i]) == (l.reshape(3, 1))):
            return True
    if np.all(a[(0, 1, 2), (0, 1, 2)] == l) or np.all (a[(0, 1, 2), (2, 1, 0)] == l):
        return True
    return False


a = np.array([
  ['X', ' ', ' '],
  [' ', 'X', 'O'],
  ['X', ' ', ' ']
])

print(is_winner(a))

