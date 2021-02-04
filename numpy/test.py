import numpy as np

def f(x):
  print(x)
  a = np.array([1, 1])
  b = np.array([2, 2])
  np.copyto(x, a + b)
  print(x)

x = np.array([0.5, 0.5])

f(x)

print(x)
