import numpy as np

a = np.arange(0, 3)
i = 0
selected, others = a[i], np.delete(a, i)

print(selected)
print(others)