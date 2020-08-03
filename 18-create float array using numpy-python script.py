import numpy as np
values = np.array([1,2,3,4],dtype=float)
print(values)
dupe = values
dupe[1]=21;
print(values)
print(dupe)